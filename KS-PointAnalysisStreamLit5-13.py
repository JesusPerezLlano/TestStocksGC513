import Get_symbols as GS
import pandas_ta as ta
import pandas as pd
import matplotlib.pyplot as plt
import CBOEPCRscrapping as SC
#import ReadExcel as RE
import time
#import ReadExcel_parameters as REp
#import WriteExcel as WE
#import Pivots as PP

###################################
#THIS CODE EMULATES THE KEN STRATEGY JUST FOR THE 5/13 CROSS IN STREAMLIT FORMAT, SO WE CAN TEST IT ONLINE
#THE REST OF PARAMETERS HAVE BEEN REMOVED
###################################
import streamlit as st
import pandas as pd
import altair as alt



from PIL import Image
#image = Image.open('C:/Users/15572890/Desktop/I+D/ProyectosPython/KYB/KYB.png')
#st.image(image, caption='Powered by TedCas')


#tic = time.perf_counter()
##############################################
#0) READ PARAMETERS
##############################################
#trend_param,stockMarket,minCAP,maxCAP=REp.ExcelReader('parameters.xlsx')
#print(trend_param,stockMarket,minCAP,maxCAP)

    
##############################################
#1) WE GET THE DATA
##############################################
def Cross513():
    US_Stocks=True
    minCAP=100	
    maxCAP=500


    if US_Stocks:
        #stocks_US=RE.ExcelReader('C:/Users/15572890/Desktop/StockPrediction/Coding/CorrelacionStocks/APIS-StockPlatforms/APIs/listofstocks.xlsx')
        stocks_US=pd.read_excel("listofstocks.xlsx", sheet_name='Sheet_name_1', engine='openpyxl')
        #print(stocks_US)
        stocks=stocks_US.iloc[:,1] #We get just the name of the stock
        stocks=GS.get_symbols_US()
        #print(stocks)
        agg_dict = {'Open': 'first',
                  'High': 'max',
                  'Low': 'min',
                  'Close': 'last',
                  #'Adj Close': 'last',
                  'Volume': 'mean'}
        stocks=GS.get_symbols_US_per_size(minCAP,maxCAP)
        stocks = list(dict.fromkeys(stocks))







        Points=0
        #RecommendationDataFramedf=pd.Series("STOCK", dtype="string")
        for symb in stocks:
            print("Symbol:" + str(symb))
            st.write("Testing stock: "+str(symb))
            tic = time.perf_counter()
            #toc = time.perf_counter()
            Points_Bullish = []
            TimeFrame=2
            try:
                df = pd.DataFrame().ta.ticker(symb) 
                #df = pd.concat([df,df.ta.thermo(length=22, long=3, short=7)], axis=1)
          
                toc = time.perf_counter()
                print("Toc-tic"+str(toc-tic))
                ################################################################
                #TREND (GOLEND CROSS and MACD uptick)
                ################################################################
                # Create the "Golden Cross" 
                df["GC"] = df.ta.sma(5, append=True) >= df.ta.sma(13, append=True)
                #df["Points"]=0.0
                GC=False
                i=0
                toc2 = time.perf_counter()
                print(toc2-toc)
                for j in range(TimeFrame):
                    if df["GC"][-1-j]==True and df["GC"][-2-j]==False and GC==False:
                        #df["Points"][-1]=df["Points"][-1]+1
                        #Points_Bullish.append("Golden Cross "+str(j))
                        GC=True
                        #print(df)
                        toc3 = time.perf_counter()
                        print(toc3-toc2)           
           


                if GC==True: 
                    print("GC")
                    st.write("GC for stock: "++str(symb))
                    print("For stock: "+str(symb)+ " Points=" + str(df["Points"][-1-i]) + " out of 8 "  + str(i) + " days ago")
                

            except:
                print("Fallo en stock: "+str(symb))


if st.button('Execute algorithm'):
    Cross513()

