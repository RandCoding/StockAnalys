from alpha_vantage.timeseries import TimeSeries
import matplotlib.pyplot as plt
import pandas as pd
import json
from alpha_vantage.techindicators import TechIndicators

api_key = open("api_stocks.txt","r").read()
api_key

tss = TimeSeries(key=api_key, output_format='pandas')
data, meta_data = tss.get_intraday(symbol='MSFT',interval='1min', outputsize='full')
# print(data)
ti = TechIndicators(key=api_key, output_format='pandas')
d_macd, meta_d_macd = ti.get_macd(symbol='MSFT', interval='1min')
# print(d_macd)

ti = TechIndicators(key=api_key, output_format='pandas')
d_sma, meta_d_sma = ti.get_sma(symbol='MSFT', interval='1min')

ti = TechIndicators(key=api_key, output_format='pandas')
d_ema, meta_d_ema = ti.get_ema(symbol='MSFT', interval='1min')


frames = [data, d_macd,d_sma,d_ema]
result = pd.concat(frames, axis=1, join='inner')


# result.plot(y=['MACD','MACD_Signal'],figsize=(15,5))
# plt.grid()
# result.plot(y=['EMA','SMA','4. close'],figsize=(15,7))
# plt.grid()
# plt.show()


worker = result[result["MACD"] == result["MACD_Signal"]]
# index_sell = worker[worker["MACD"] >= worker["MACD_Hist"]].index
# index_buy = worker[worker["MACD"] < worker["MACD_Hist"]].index
index_sell = worker[worker["MACD"] > 0].index
index_buy = worker[worker["MACD"] < 0].index

sell = result.loc[index_sell]
buy = result.loc[index_buy]

ax = plt.axes()

sell.plot(y=['4. close'],color='red', marker='o',markerfacecolor='red',style='.',ax=ax,markersize=12)
buy.plot(y=['4. close'],color='green', marker='o',markerfacecolor='green',style='.',ax=ax,markersize=12)

result.plot(y=['MACD','MACD_Signal'],figsize=(15,5))
plt.grid()
result.plot(y=['EMA','SMA','4. close'],figsize=(15,7),ax=ax)
plt.grid()
plt.show()



 





 





 





 





 





 




