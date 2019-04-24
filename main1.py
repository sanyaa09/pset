import urllib
import requests

def initialize(context):
    set_symbol_lookup_date('2008-01-01')
    context.stocks= symbol('amzn','csco','yhoo','msft','g')

def fetch_data(symbol):
    

    data = requests.get('https://www.quandl.com/api/v3/datasets/WIKI/AAPL.csv')                         # write code to fetch data  # and save it in data variable
    
    data.json()
    data.current('last traded')


               # set it to None if symbol invalid
    
                    # setting it to None for now


    # handling function for when data is actually None
    if data is None:
        return None
    else:
        return process_data(data)


def process_data(raw_data):
    processed_data = None
       
    price_history = data.history(context.securities, fields="price", bar_count=2, frequency="1d")
    for s in context.securities:
        prev_bar = price_history[s][-2]
        curr_bar = price_history[s][-1]
        if curr_bar > prev_bar:
            order(s, 20)
# write code here to process data
        # store it in processed_data variable
        #
            # setting it to None for now

    return processed_data
