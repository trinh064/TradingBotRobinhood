import robin_stocks.robinhood as rh
import robin_stocks.gemini as gem
import robin_stocks.tda as tda
import sys
import os

import pyotp
import robin_stocks as robin
import pandas as pd
#lines = open('./cred.txt').read().splitlines()
#KEY = lines[0]
EMAIL = input("Email:")
PASSWD = input("Password:")
#CODE = lines[3]
#totp = pyotp.TOTP(KEY).now()

login = rh.login(EMAIL,PASSWD)
def QUOTE(ticker):
    r = rh.get_latest_price(ticker)
    print('Latest ',ticker,r)
    return r[0]
def HIST(ticker):
    data= pd.DataFrame(rh.get_stock_historicals(ticker, interval="10minute", span="week"))
    print(data)
    return data
def SELL(ticker, ammount):
    r = rh.order_sell_market(ticker,ammount)
    print(r)

def BUY(ticker, ammount):
    r = rh.order_buy_market(ticker,ammount)
    print(r)

while(1):
    TICKER = input("Check Stock:")
    QUOTE(TICKER)
    HIST(TICKER)
# Here are some example calls
#print(gem.get_pubticker("btcusd")) # gets ticker information for Bitcoin from Gemini
#rh.get_all_open_crypto_orders() # gets all cypto orders from Robinhood
#tda.get_price_history("tsla") # get price history from TD
