import requests
from datetime import datetime, timedelta
import json
import numpy as np
import pandas as pd
import os
import time
import h5py

endpoint = "https://api.pro.coinbase.com/products/BTC-USD/candles"
granularity = 3600 # i.e. one hour candlesticks
data_save_path = os.path.join(os.getcwd(), "PyTorch\\CustomDataLoaders\\data")
column_headers = [ "time", "low", "high", "open", "close", "volume" ]

# make directory if it does not exist 
os.makedirs(data_save_path)

start = datetime(2020, 1,1)
end = datetime(2020, 6, 15)


#### Notice 
## You will see that we are saving a custom index to each of the csvs
## this will be used in our dataset tutorial so that we can easily get the data loaded from files
data_to_write = []
while start < end:
    print("Download: {} ".format(start))
    # format the end datetime
    working_end = start + timedelta(seconds=granularity*300)
    # format request params
    params = {"start": start, "end": working_end, "granularity": granularity}
    # get the data and format it as a list of lists
    data = json.loads(requests.get(url=endpoint, params=params).content.decode("utf-8"))
    # get the next request start time
    start = datetime.utcfromtimestamp(data[0][0]+granularity)

    # format and save as a pandas df and CSV
    data_to_write.append(data)

    time.sleep(1) # sleep to avoid rate limits

np_arr = np.array(data_to_write)
np_arr = np_arr.reshape(-1, np_arr.shape[-1])
np_arr.shape

# Write the file
with h5py.File("{}\\btc_hdf5_data.hdf5".format(data_save_path), 'w') as f:
    dset = f.create_dataset("default", data=np_arr)


# read the file for testing
f = h5py.File("{}\\btc_hdf5_data.hdf5".format(data_save_path), 'r')
data = f['default']
print(data[0])