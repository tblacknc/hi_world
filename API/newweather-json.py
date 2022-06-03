#!/usr/bin/env python

import requests
import json
from numerize import numerize
from datetime import datetime, timedelta

#############################################
# determins location from IP address then
# uses the ip address do get the 3 day forcast
############################################


url = 'https://api.ipify.org/?format=xml'

response = requests.get(url)

ip_address = response.text


url = "http://api.weatherapi.com/v1/forecast.json?"

queryURL = url + f"key=5bfef5467dd54a41a8a113336222805"
queryURL += f"&q={ip_address}"
queryURL += f"&days=3"
queryURL += f"&aqi=no"
queryURL += f"&alerts=no"

response = requests.get(queryURL)

userdata = json.loads(response.text)
try:

    for data in userdata['forecast']['forecastday']:

        for dat in  reversed(data['hour']): 
            print("")    
            print(f"{dat['time']}")
            print(f"-------------------------------")

            print(f"Temperature\t{dat['temp_f']} F")
            print(f"\t\t{dat['condition']['text']}")
            print(f"Wind Speed\t{dat['wind_mph']} MPH")
            print(f"Wind Direction\t{dat['wind_dir']}")
            print(f"Precipitation\t{dat['precip_in']} inch")
            print(f"Humidity\t{dat['humidity']} %")
            print(f"Cloud Cover\t{dat['cloud']} %")

    print(f"")
    print(f"Current Conditions")
    print(f"-------------------------------")
    print(f"{userdata['location']['localtime']}")

    print(f"Temperature\t{userdata['current']['temp_f']} F")
    print(f"\t\t{userdata['current']['condition']['text']}")
    print(f"Wind Speed\t{userdata['current']['wind_mph']} MPH")
    print(f"Wind Direction\t{userdata['current']['wind_dir']}")
    print(f"Precipitation\t{userdata['current']['precip_in']} inch")
    print(f"Humidity\t{userdata['current']['humidity']} %")
    print(f"Cloud Cover\t{userdata['current']['cloud']} %")    
    print(f"")    
    
    for data in userdata['forecast']['forecastday']:
        print(f"")    
        print(f"Date\t\t{data['date']}")
        print(f"Sun Rise\t{data['astro']['sunrise']}")  
        print(f"Sun Set\t\t{data['astro']['sunset']}")    
        print(f"Moon phase\t{data['astro']['moon_phase']}")    

    print(f"")
    print(f"{userdata['location']['name']}")
    print(f"{userdata['location']['region']}")
    print(f"{userdata['location']['tz_id']}")
    print()
    print(f"{queryURL}")

except Exception as e: 
    print(e)

    print("crap-eth")