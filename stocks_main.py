import yfinance as yf
import pandas as ps

msft = yf.Ticker('msft')
stockInfo = msft.info

# for key,value in stockInfo.items():
#     print(key, ":" , value)

# print(msft.history(period="5d"))
fiveD = msft.history(period="5d").to_json(date_format="iso")
print(fiveD)
# print(type(msft.dividends))