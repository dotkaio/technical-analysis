import json
import requests as qsts
import matplotlib.pyplot as plt
#import pandas
#import trulio api
#truluo account

class Get(object):
  """
     this is the simple version
     you asked me for. 
     
     
     *receive requests with sms
     *pattern - symbol, timeframe, etc.
     
     - Loop starts at 09:45 and stops at 13:00
       (EST UTC-05:00). The program is lighter
       because it's fetiching only the previous
       24 hours, which tou said is what counts
       for this operation.
     
     - The object work as the follow:
       - Go over the Adjusted Close 5min TimeFrame
         filtering close values and checking for
         previous crosses with EMA 9.
       - Regardless the Bullish or Bearish signal,
         the program will triguer a text message
         with the confirmation
         
  """
  
  #function=EMA&
  #symbol=IBM&
  #interval=weekly&
  #time_period=10&
  #series_type=open&apikey=demo
 
   
  def __init__(self, *args, **kwargs):
    self.fetch = fetch
    self.sms = sms
    self.email = email
    
    
  def fetch_data(self):
    """Fetch specific data from API:
       the 5min intraday of the given
       symbol and the EMAs"""
       
    def get_intraday(self):
      
      api_url = "https://www.alphavantage.co"
      
      #check if API server is online
      get_ = _r.get(api_url)
      if not get_.status_code:
        response = get_.status_code
        print("Bad connection. Error:"+str(response))
      
      else:
        data_ = _rq.get(url).json()
      
      return data_
    
    # filter 
    def filter(data, meta_data):
      return data, meta_data
      
    def filter(symbol)
      
       '1: Symbol': 'IBM',
       '2: Indicator': ' Moving Average',
       '3: Last Refreshed': '2020-10-28',
       '4: Interval': 'weekly',
       '5: Time Period': 10, 
       '6: Series Type': 'open',
       '7: Time Zone': 'US/Eastern'}
