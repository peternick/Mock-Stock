import yfinance as yf
import pandas as ps
import json

msft = yf.Ticker('msft')
stockInfo = msft.info

# for key,value in stockInfo.items():
#     print(key, ":" , value)


# data = msft.history(period="1d", interval="30m").to_json(date_format="iso")
# obj_data = json.loads(data)

data = msft.info

print(data.keys())


# data = msft.history(start="2021-04-13", end="2021-04-14", interval="15m")

# obj_data = data.to_json(date_format="iso")