from django.shortcuts import render
import yfinance as yf
import pandas as ps

sp500 = yf.Ticker('^gspc')

# Create your views here.
def home(request):
    hist = sp500.history(period="1d", interval="1m").to_json(date_format="iso")
    context = {
        'hists': hist,
        'interval_unit': 'less_than_days'
    }
    return render(request, 'homepage.html', context)

def update_spfivehundred_data(request):
    time_period = request.POST["new_graph_period"]
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
    hist = sp500.history(period=time_period, interval=interv).to_json(date_format="iso")
    context = {
        'hists':hist,
        'interval_unit': interval_unit
    }
    return render(request, 'homepage.html', context)
