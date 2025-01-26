import pandas as pd
import numpy as np
import plotly.graph_objects as go
from plotly.offline import plot
import matplotlib.pyplot as plt
import datetime
from pycoingecko import CoinGeckoAPI
from mplfinance.original_flavor import candlestick2_ohlc

cg = CoinGeckoAPI()
bitcoin_data = cg.get_coin_market_chart_by_id(id = 'bitcoin', vs_currency = 'usd', days = 30)
print(bitcoin_data)                 #///1st argument is timestamp & 2nd is price
bitcoin_price_data = bitcoin_data['prices']

data = pd.DataFrame(bitcoin_price_data, columns=["TimeStamp", "Price"])           #convert given data to dataframe
print(data)
data['Date'] = pd.to_datetime(data['TimeStamp'], unit='ms')

candlestick_data = data.groupby(data.Date.dt.date).agg({'Price':['min', 'max', 'first', 'last']})
print(candlestick_data)

fig = go.Figure(data=[go.Candlestick(x = candlestick_data.index,
                                     open = candlestick_data['Price']['first'],
                                     high = candlestick_data['Price']['max'],
                                     low = candlestick_data['Price']['min'],
                                     close = candlestick_data['Price']['last'])
                                     ])
fig.update_layout(xaxis_rangeslider_visible=False, xaxis_title='Date',
                  yaxis_title='Price (USD $)', title='Bitcoin Candlestick Chart Over Past 30 Days')

plot(fig, filename = 'bitcoin_candlestick_graph.html')

fig.show()
