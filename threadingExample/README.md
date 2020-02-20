# Multithreading in Python 


The global interpretter lock is something that I first learned when I started developing in Python. It was never really an issue as I was typically working in sequential and single threaded applications. Then I realized how great the multi threading library in python is for calling and saving data from REST APIs. I provide a simple [example](./threadingAPIData.py) of how to call a rest api and save the data to a csv using the built in threading library. 


The general setup of the solutions involves creating a data collection function that is run on a separate thread. The purpose of this function is to collect data as it is available or on a regular cadence. As the thread is collecting data, it is dumping the requested information into a queue for the main function to access and process. 

To get started import the following libraries. 
```python
import requests
import threading
import queue
import os
import datetime 
import time
import pandas as pd 
import json
```


Next we will create a function that collects data from [openweathermap rest APIs](https://openweathermap.org/current). To access the APIs simply create a free account and request and API key. Please note that it may take a few minutes for the API to activate on their system. I was receiving 401 errors for a few minutes before it started returning data.  

The following function runs on a continuous loops but only gets data one time each hour between the first six minutes of each hour. 
```python

def request_data(city_name):
    current_hour = datetime.datetime.utcnow().hour
    while True:
        # only gets data once an hour 
        if datetime.datetime.utcnow().minute >= 0 and datetime.datetime.utcnow().minute <= 6:
            print("Getting Data")
            api_key = os.environ.get('weather_api_key')

            api_url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(city_name, api_key)

            data = requests.get(api_url)
            rest_call = False
            q.put(json.loads(data.content.decode("utf-8")))

        # thread stays in this loop until the next hour
        while datetime.datetime.utcnow().hour == current_hour:
            print("Waiting {} minutes..{}".format(60-datetime.datetime.utcnow().minute, "."*datetime.datetime.utcnow().minute), end="\r")
            time.sleep(300) # wait 5 minutes - don't want to wait to short since it will always be executing
            continue

```


Next we will have our code entrypoint and pick data up off our queue and save it to a pandas dataframe. 
```python

if __name__ == "main":
    # create variables
    city_name = "Seattle"
    q = queue.Queue()

    # execute thread
    x = threading.Thread(target=request_data, args=(city_name,))
    x.start()

    # get data and write to pandas 
    while True: 
        # if there is data in the queue then we will format at it as a flat dictionary and write to csv
        if not q.empty():
            row = q.get(block=False, timeout=2)
            row_parsed = {
                'longitude': row.get("coord").get("lon"), 
                'latitude': row.get("coord").get("lat"), 
                'weather_id': row.get("weather")[0].get("id"), 
                'main': row.get("weather")[0].get("main"), 
                'description': row.get("weather")[0].get("description"), 
                'icon': row.get("weather")[0].get("icon"), 
                'base': row.get("base"), 
                'temp': row.get("main").get("temp"), 
                'feels_like': row.get("main").get("feels_like"), 
                'temp_min': row.get("main").get("temp_min"), 
                'temp_max': row.get("main").get("temp_max"), 
                'pressure': row.get("main").get("pressure"), 
                'humidity': row.get("main").get("humidity"),
                'visibility': row.get("visibility"),
                'wind_speed': row.get("wind").get('speed'),
                'wind_deg': row.get("wind").get('deg'), 
                'clouds': row.get("clouds").get("all"), 
                'datetime': row.get("dt"),
                'sys_type': row.get("sys").get("type"),
                'id': row.get("sys").get("id"),
                'country': row.get("sys").get("country"),
                'sunrise': row.get("sys").get("sunrise"),
                'sunset': row.get("sys").get("sunset"), 
                'timezone': row.get("timezone"),
                "id": row.get("id"),
                "City": row.get("name"),
                "cod": row.get("cod")
            }
            
            pd.DataFrame(data=[row_parsed]).to_csv("threadingExample/output.csv", header=False, mode="a")
```


Note that we could create another Python thread that automatically formats our data and returns a flatten dictionary. 
```python

def format_data():
    if not q.empty():
        row = q.get(block=False, timeout=2)
        row_parsed = {
            'longitude': row.get("coord").get("lon"), 
            'latitude': row.get("coord").get("lat"), 
            'weather_id': row.get("weather")[0].get("id"), 
            'main': row.get("weather")[0].get("main"), 
            'description': row.get("weather")[0].get("description"), 
            'icon': row.get("weather")[0].get("icon"), 
            'base': row.get("base"), 
            'temp': row.get("main").get("temp"), 
            'feels_like': row.get("main").get("feels_like"), 
            'temp_min': row.get("main").get("temp_min"), 
            'temp_max': row.get("main").get("temp_max"), 
            'pressure': row.get("main").get("pressure"), 
            'humidity': row.get("main").get("humidity"),
            'visibility': row.get("visibility"),
            'wind_speed': row.get("wind").get('speed'),
            'wind_deg': row.get("wind").get('deg'), 
            'clouds': row.get("clouds").get("all"), 
            'datetime': row.get("dt"),
            'sys_type': row.get("sys").get("type"),
            'id': row.get("sys").get("id"),
            'country': row.get("sys").get("country"),
            'sunrise': row.get("sys").get("sunrise"),
            'sunset': row.get("sys").get("sunset"), 
            'timezone': row.get("timezone"),
            "id": row.get("id"),
            "City": row.get("name"),
            "cod": row.get("cod")
        }
        format_queue.put(row_parsed)
```


So then our main function would be something like the following:  
```python
if __name__ == "main":
    # create variables
    city_name = "Seattle"
    q = queue.Queue()
    format_queue = queue.Queue()

    # execute thread
    x = threading.Thread(target=request_data, args=(city_name,))
    x.start()

    y = threading.Thread(target=request_data))
    y.start()

    # get data and write to pandas 
    while True: 
        # if there is data in the queue then we will format at it as a flat dictionary and write to csv
        if not format_queue.empty():
            row = format_queue.get(block=False, timeout=2)
            pd.DataFrame(data=[row]).to_csv("threadingExample/output.csv", header=False, mode="a")

```


If we create all three functions then it opens our main function up to complete other actions, like sending alerts or mananging even more threads! There are a few things worth noting about threading: 
1. Threading does not bypass the global interpretter lock. Each function will execute sequentially, and completely before starting the work of another thread. 
    - This means that high volume data collection applications are not a great use case as data may pile up in the queue as you are trying to write to the database. 
    - The benefit of this is that threads can share variables, for example our queue is shared between the main entrypoint and the threading function. 

1. The `time.sleep` command halts execution on a thread. The command actually stops the execution of current thread and will pickup where it left off. 
    - Please check the [hello world example](threadingHelloWorld.py) to see this in action. You will notice that the second thread prints much more often than the first thread and doesn't have to wait for the first thread to complete the second print. 



