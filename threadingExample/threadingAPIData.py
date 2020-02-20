import requests
import threading
import queue
import os
import datetime 
import time
import pandas as pd 
import json



def request_data(city_name):
    current_hour = datetime.datetime.utcnow().hour
    while True:
        if datetime.datetime.utcnow().minute >= 0 and datetime.datetime.utcnow().minute <= 60:
            print("Getting Data")
            api_key = os.environ.get('weather_api_key')

            api_url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(city_name, api_key)

            data = requests.get(api_url)
            rest_call = False
            q.put(json.loads(data.content.decode("utf-8")))

        while datetime.datetime.utcnow().hour == current_hour:
            print("Waiting {} minutes..{}".format(60-datetime.datetime.utcnow().minute, "."*datetime.datetime.utcnow().minute), end="\r")
            time.sleep(300) # wait 5 minutes
            continue



if __name__ == "main":
    city_name = "Seattle"
    q = queue.Queue()

    x = threading.Thread(target=request_data, args=(city_name,))
    x.start()

    # get data and write to pandas 
    while True: 
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



