from django.shortcuts import render
import yfinance as yf
import pandas as ps

msft = yf.Ticker('msft')


# Create your views here.
def home(request):
    hist = msft.history(period="1mo").to_json(date_format="iso")
    context = {
        'hists': hist
    }
    return render(request, 'homepage.html', context)