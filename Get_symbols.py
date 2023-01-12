from fastquant import backtest, get_stock_data
from fastquant import get_yahoo_data, get_bt_news_sentiment
import matplotlib.pyplot as plt
import numpy as np
import pandas
import investpy
import yfinance as yf
import pandas_ta as ta
from fastquant import backtest, get_stock_data
import matplotlib.pyplot as plt


def get_symbols_US():
    import pandas as pd
    from yahoo_fin import stock_info as si


    # gather stock symbols from major US exchanges
    df1 = pd.DataFrame( si.tickers_sp500() )
    df2 = pd.DataFrame( si.tickers_nasdaq() )
    df3 = pd.DataFrame( si.tickers_dow() )
    df4 = pd.DataFrame( si.tickers_other() )

    # convert DataFrame to list, then to sets
    sym1 = set( symbol for symbol in df1[0].values.tolist() )
    sym2 = set( symbol for symbol in df2[0].values.tolist() )
    sym3 = set( symbol for symbol in df3[0].values.tolist() )
    sym4 = set( symbol for symbol in df4[0].values.tolist() )

    # join the 4 sets into one. Because it's a set, there will be no duplicate symbols
    symbols = set.union( sym1)#, sym2, sym3, sym4 )

    # Some stocks are 5 characters. Those stocks with the suffixes listed below are not of interest.
    my_list = ['W', 'R', 'P', 'Q']
    del_set = set()
    sav_set = set()

    for symbol in symbols:
        if len( symbol ) > 4 and symbol[-1] in my_list:
            del_set.add( symbol )
        else:
            sav_set.add( symbol )

    print( f'Removed {len( del_set )} unqualified stock symbols...' )
    print( f'There are {len( sav_set )} qualified stock symbols...' )
    #print(symbols)
    return symbols




def get_symbols_ES():
    data = investpy.get_stocks(country='spain')
    data_fin=[]
    #print(data['symbol'])
    counter=0
    for symbol in data['symbol']:
        #print("SIMBOLO")
        #print(symbol)
        if symbol!="GRLS" and symbol!="ENAG":
            name=symbol+str(".MC")
        if symbol=="OHL":
            name="OHLA.MC"
        if symbol=="TUBA":
            name="TUB.MC"
        if symbol=="ENOR":
            name="ENO.MC"
        if symbol=="PHMR":
            name="PHM.MC"
        if symbol=="SGREEN":
            name="SGREE.MC"
        if symbol=="SABE":
            name="SAB.MC"
        if symbol=="ICAG":
            name="IAG.MC"
        if symbol=="AMA":
            name="AMS.MC"
        if symbol=="SLRS":
            name="SLR.MC"
        if symbol=="ALNTA":
            name="ALNT.MC"
        if symbol=="EZEN":
            name="EZE.MC"    
        data_fin.append(name)

    return data_fin

#data_fin=get_symbols_ES()
#print(data_fin)
#data_fin=get_symbols_US()
#print(data_fin)

def get_symbols_US_per_size(mktcap_min,mktcap_max):
    import yfinance as yf, pandas as pd, shutil, os
    #from get_all_tickers import get_tickers as gt
    #from get_all_tickers.get_tickers import Region
    import get_ticket as gt
    # tickers of all exchanges
    #tickers = gt.get_tickers()
    #print(tickers[:5])

    #SMALL CAPS: 300M-2000M
    #tickers = gt.get_tickers_filtered(mktcap_min=300, mktcap_max=2000, sectors=gt.SectorConstants.ENERGY)
    tickers = gt.get_tickers_filtered(mktcap_min=mktcap_min, mktcap_max=mktcap_max)
    print("The amount of stocks chosen to observe: " + str(len(tickers)))
    #print(tickers)

    return tickers