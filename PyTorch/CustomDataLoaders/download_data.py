import requests
from datetime import datetime, timedelta
import json
import pandas as pd
import os
import time

endpoint = "https://api.pro.coinbase.com/products/BTC-USD/candles"
granularity = 3600 # i.e. one hour candlesticks
data_save_path = "PyTorch/CustomDataLoaders/data"
column_headers = [ "time", "low", "high", "open", "close", "volume" ]

# make directory if it does not exist 
os.makedirs(data_save_path)

start = datetime(2020, 1,1)
end = datetime(2020, 6, 15)
counter = 0

while start < end:
    print("Parition Download: {} | {}".format(counter, start))
    # format the end datetime
    working_end = start + timedelta(seconds=granularity*300)
    # format request params
    params = {"start": start, "end": working_end, "granularity": granularity}
    # get the data and format it as a list of lists
    data = json.loads(requests.get(url=endpoint, params=params).content.decode("utf-8"))
    # get the next request start time
    start = datetime.utcfromtimestamp(data[0][0]+granularity)

    # format and save as a pandas df and CSV
    df = pd.DataFrame(data, columns=column_headers)
    df.to_csv("{}/btc_parition_{}.csv".format(data_save_path, counter), index=False)
    counter+=1

    time.sleep(1) # sleep to avoid rate limits
