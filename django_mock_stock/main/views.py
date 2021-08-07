from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from userAccounts.models import Account, Stock
import decimal
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

    user = request.session['username']
    accnt_obj = Account.objects.get(username=user)
    accnt_info = json.dumps({"balance": accnt_obj.get_balance(), "account_value": accnt_obj.get_account_val()})
    context = {
        'hists': json.dumps({"hist_sp": hist_sp, "hist_dow": hist_dow, "hist_nasdaq": hist_nasdaq}),
        'interval_unit': interval_unit_lst,
        'account_info': accnt_info
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
    
    user = request.session['username']
    accnt_obj = Account.objects.get(username=user)
    accnt_info = json.dumps({"balance": accnt_obj.get_balance(), "account_value": accnt_obj.get_account_val()})

    owned_stock_ctxt = {}
    try:
        stock_obj = accnt_obj.owned_stocks.get(stock_ticker=searched_input)
        owned_stock_ctxt["num_shares"] = stock_obj.get_num_stocks()
        owned_stock_ctxt["total_val"] = stock_obj.get_total_val()
        owned_stock_ctxt = json.dumps(owned_stock_ctxt)
        print("wtf")
    except ObjectDoesNotExist as err:
        print(searched_input)
        pass

    dic = json.dumps({"hist": ticker_hist, "info": ticker_info, "time_interval": "less_than_days"})
    context = {
        "ticker_data" : dic,
        "account_info": accnt_info,
        "owned_stock_info": owned_stock_ctxt
    }
    return render(request, 'specified_stock.html', context)

def alter_user_stock(request):
    user = request.session['username']
    ticker = request.POST['searched_text']
    accnt_obj = Account.objects.get(username=user)

    stock_price = request.POST['stock_price']
    num_stocks = int(request.POST['quantity_shares'])
    total_val = num_stocks * float(stock_price)
    try:
        stock_obj = accnt_obj.owned_stocks.get(stock_ticker=ticker)
        stock_obj.number_stocks = stock_obj.number_stocks + num_stocks
        stock_obj.total_value = stock_obj.total_value + decimal.Decimal(total_val)
        stock_obj.save()
    except ObjectDoesNotExist as err:
        company = request.POST['company_name']
        stock_obj = accnt_obj.owned_stocks.create(stock_ticker=ticker, company_name=company, number_stocks=num_stocks, total_value=total_val)
    
    return ticker_page(request)

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
    
