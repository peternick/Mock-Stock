from django.shortcuts import render
import yfinance as yf
import pandas as ps
import json

sp500 = yf.Ticker('^gspc')
dow = yf.Ticker('^dji')
nasdaq = yf.Ticker('^ixic')

sp_period = "less_than_days"
dow_period = "less_than_days"
nasdaq_period = "less_than_days"
interval_unit_lst = [sp_period, dow_period, nasdaq_period]


# Create your views here.
def home(request):
    
    hist_sp = sp500.history(period="1d", interval="1m").to_json(date_format="iso")
    hist_dow = dow.history(period="1d", interval="1m").to_json(date_format="iso")
    hist_nasdaq = nasdaq.history(period="1d", interval="1m").to_json(date_format="iso")
    
    time_prd_chngd = request.POST
    if(len(time_prd_chngd) > 1):
        new_data_lst = _update_graph_data(time_prd_chngd)
        index_name = new_data_lst[2] if len(new_data_lst) > 1 else ""
        if(index_name == "hist_sp"):
            hist_sp = new_data_lst[0]
        elif(index_name == "hist_dow"):
            hist_dow = new_data_lst[0]
        elif(index_name == "hist_nasdaq"):
            hist_nasdaq = new_data_lst[0]


    context = {
        # 'hists': [hist_sp, hist_dow, hist_nasdaq],
        'hist_sp': hist_sp,
        'hist_dow': hist_dow,
        'hist_nasdaq': hist_nasdaq,
        'interval_unit': interval_unit_lst
    }
    return render(request, 'homepage.html', context)


def ticker_page(request):
    searched_input = request.POST['searched_text']

    try:
        specified_ticker = yf.Ticker(searched_input)
        ticker_hist = json.loads(specified_ticker.history(period="1d", interval="1m").to_json(date_format="iso"))
        ticker_info = specified_ticker.info
    except KeyError as err:
        return render(request, 'error_page.html')
    except ImportError as err:
        return render(request, 'error_page.html')
    # print(specified_ticker.history(period="1d", interval="30m").to_json(date_format="iso"))
    
    dic = {"hist": ticker_hist, "info": ticker_info, "time_interval": "less_than_days"}
    context = {
        "ticker_data" : dic 
    }
    return render(request, 'specified_stock.html', context)

def _update_graph_data(request_post_dict):
    SP = 'hist_sp'
    DOW = 'hist_dow'
    NASDAQ = 'hist_nasdaq'
    new_data_lst = []
    if(request_post_dict.__contains__("sp_graph_period_btn")):
        new_data_lst = _obtain_interval_data(request_post_dict["sp_graph_period_btn"], sp500, SP)
        interval_unit_lst[0] = new_data_lst[1]
    elif(request_post_dict.__contains__("dow_graph_period_btn")):
        new_data_lst = _obtain_interval_data(request_post_dict["dow_graph_period_btn"], dow, DOW)
        interval_unit_lst[1] = new_data_lst[1]
    elif(request_post_dict.__contains__("nasdaq_graph_period_btn")):
        new_data_lst = _obtain_interval_data(request_post_dict["nasdaq_graph_period_btn"], nasdaq, NASDAQ)
        interval_unit_lst[2] = new_data_lst[1]
    
    return new_data_lst


def _obtain_interval_data(time_period, tikr_data, index_data_key):
    interv = "1d"
    interval_unit = "more_than_days"
    if(time_period == "1d"):
        interv = "1m"
        interval_unit = "less_than_days"
    elif(time_period == "5d"):
        interv = "5m"
    elif(time_period == "1mo"):
        interv = "30m"
    elif(time_period == "3mo"):
        interv = "60m"
    elif(time_period == "6mo"):
        interv = "60m"
    elif(time_period == "1y"):
        interv = "1d"
    else:
        interv = "1mo"
    hist = tikr_data.history(period=time_period, interval=interv).to_json(date_format="iso")
    data_lst = []
    data_lst.append(hist)
    data_lst.append(interval_unit)
    data_lst.append(index_data_key)

    return data_lst
    
