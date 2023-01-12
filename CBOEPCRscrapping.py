

def CBOEPCR():
    # Importing libraries
    import sys
    import datetime
    import time
    import pandas as pd
    import requests
    import pickle
    import random
    import matplotlib.pyplot as plt
    import matplotlib.ticker as mtick
    from pandas.plotting import register_matplotlib_converters
    from datetime import datetime, timedelta

    register_matplotlib_converters()

    # Adding in filepath and file location to facilitate load and save
    filepath = r'C:/Users/15572890/Desktop/StockPrediction/Coding/CorrelacionStocks/APIS-StockPlatforms/APIs'
    pickle_file = filepath + r'\CBOE_options_data.pkl'


    # URL address of CBOE site where I would like to scrape
    url_main = "https://markets.cboe.com/us/options/market_statistics/daily/?mkt=cone&dt="



    """Scraping from CBOE website
    - Enter the date from when to update the pickle file
    Original file saved under pickle format, with dictionary format
    First valid data = '2019-10-07     80497922.0'
    """
    # Over here I have to manually incorporate the holidays so to delete them after downloading, for these dates the scraped data are incorrect
    # This procedure works after the pickle file is created and run for subsequent times.
    # For first time download, this module here will have error and exited - please continue to next module for the scraping.
    # opt_out_days: Opting out public holidays
    opt_out_days = ['2019-11-28', '2019-12-25', '2020-01-01', '2020-01-20', '2020-02-17', '2020-04-10',
                    '2020-05-25', '2020-07-03', '2020-09-07']
    weekdays =[]
    scrapeDict ={}

    def get(url):
        headers = {}
        resp = requests.get(url)
        if resp.ok:
            return resp.text

    """The following to check if there is existing pickle file already stored and available, program will
    open it and continue to download from the last date.
    If there is no existing file, program will continue with the download"""


    #"""This part is to scrape from CBOE website and save the file"""
    #inputStartDate = input('Enter starting date (YYYYMMDD) or <enter> for the last date in file : ')
    today= datetime.today()
    start_date = today - timedelta(days=1)
    end_date = datetime.today()
    delta = timedelta(days=1)

    run_date=start_date
    while run_date < end_date:
        if run_date.weekday() not in [5,6]: #ie. Mon-Fri only
            weekdays.append(run_date)
        elif run_date.weekday()==5: #Saturday, we get the day before
            weekdays.append(run_date - timedelta(days=1))
        else: #Sunday, we get two days before
            weekdays.append(run_date - timedelta(days=2))
        run_date += delta

    print('Running:') 
    print(weekdays)
    for get_date in weekdays:
        html_date = datetime.strftime(get_date, '%Y-%m-%d')
        data = get(url_main+html_date)

        # As I mentioned above this is an easy site, I can just use Pandas read_html to extract the tables efficiently
        scrapeDict[get_date] = pd.read_html(data)
        print(get_date, end='|')
        # Putting in random pauses so not to overwhelm the website and got blacklisted and banned
        time.sleep(round(random.random()*3,1))

    outfile = open(pickle_file,'wb')
    pickle.dump(scrapeDict,outfile)
    outfile.close()
    print('Done!')

    """Here we just get a look of how the tables are stacked up"""
    pd.read_html(data)
    print(pd.read_html(data))
    a=pd.read_html(data)[0]
    #print(a["RATIOS.1"][0])

    return a["RATIOS.1"][3]
