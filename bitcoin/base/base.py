# 1.py

# setting 
# pip install pybithumb
# pip install -U pybithumb

## module import 
import pybithumb 
import pandas as pd
import time 

# tickers -- list of coins name
tickers = pybithumb.get_tickers()
print(tickers)

# save names of coins in coin_df 
coin_df = pd.DataFrame({'coins': tickers})

# get Present price
# ## first df setting 
coin_df["price"] = 0
coin_df.set_index("coins", inplace = True)
# get price from each ticker save in coin_df 
for ticker in tickers:
    price = pybithumb.get_current_price(ticker)
    coin_df.loc[ticker]["price"] = price 
    time.sleep(0.1)

# Stock quotes(ask, bid)

# save coin_df
coin_df.to_csv('./coin_df.csv')