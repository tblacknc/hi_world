#!/usr/bin/env python

import requests
import json
from numerize import numerize
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import re


#############################################
# determins location from IP address,
# uses the ip address do get the forcast
# then plots the Temp, Relative Humidity & 
# feels like temperature
############################################

def graphtemp(x,y1,y2,y3):
    y2.reverse()
    y1.reverse()
    x.reverse()

    plt.subplot(3, 1, 1)
    plt.plot(x, y1)
    plt.ylabel('Temp F')
    plt.gca().axes.get_xaxis().set_visible(False)
    
    plt.subplot(3, 1, 2)
    plt.plot(x, y2)
    plt.ylabel('Humidity')
    plt.gca().axes.get_xaxis().set_visible(False)
    
    plt.subplot(3, 1, 3)
    plt.plot(x, y3)
    plt.ylabel('Feels Like F')

    plt.show()


loop = 0
graphx = []
graphyh = []
graphyt = []
graphyhi = []

url = 'https://api.ipify.org/?format=xml'

response = requests.get(url)

ip_address = response.text


url = "http://api.weatherapi.com/v1/forecast.json?"

queryURL = url + f"key=5bfef5467dd54a41a8a113336222805"
queryURL += f"&q={ip_address}"
queryURL += f"&days=1"
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
            loop += 1
            m = re.search('(?<= )[0-9]+', dat['time'])
            m.group(0)
            
            graphx.append(m.group(0))
            graphyt.append(dat['temp_f'])
            graphyh.append(dat['humidity'])
            
            heatIndex = -42.38 + 2.049 * dat['temp_f'] + 10.14 * dat['humidity'] + -0.2248* dat['temp_f'] * dat['humidity'] +  -0.006838 * dat['temp_f']**2 + -0.05482 * dat['humidity']**2 + 0.001228 * dat['temp_f']**2 * dat['humidity'] + 0.0008528 * dat['temp_f'] * dat['humidity']**2 + -0.00000199 * dat['temp_f']**2 * dat['humidity']**2
            
            graphyhi.append(heatIndex)

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

    graphtemp(graphx,graphyt,graphyh,graphyhi)

except Exception as e: 
    print(e)

    print("crap-eth")