from django.shortcuts import render
import yfinance as yf
import pandas as ps

sp500 = yf.Ticker('^gspc')
dow = yf.Ticker('^dji')
nasdaq = yf.Ticker('^ixic')


# Create your views here.
def home(request):
    hist_sp = sp500.history(period="1d", interval="1m").to_json(date_format="iso")
    hist_dow = dow.history(period="1d", interval="1m").to_json(date_format="iso")
    hist_nasdaq = nasdaq.history(period="1d", interval="1m").to_json(date_format="iso")
    context = {
        # 'hists': [hist_sp, hist_dow, hist_nasdaq],
        'hist_sp': hist_sp,
        'hist_dow': hist_dow,
        'hist_nasdaq': hist_nasdaq,
        'interval_unit': 'less_than_days'
    }
    return render(request, 'homepage.html', context)

def update_graph_data(request):
    sp_time_period = request.POST["sp_graph_period_btn"]
    dow_time_period = request.POST["dow_graph_period_btn"]
    nasdaq_time_period = request.POST["nasdaq_graph_period_btn"]

    context = None
    if(len(sp_time_period) > 1):
        context = _obtain_interval_data(sp_time_period, sp500)
    elif(len(dow_time_period) > 1):
        context = _obtain_interval_data(dow_time_period, dow)
    else:
        context = _obtain_interval_data(nasdaq_time_period, nasdaq)
    
    return render(request, 'homepage.html', context)

def _obtain_interval_data(time_period, tikr_data):
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
    context = {
        'hists': [hist],
        'interval_unit': interval_unit
    }
    return context
    
