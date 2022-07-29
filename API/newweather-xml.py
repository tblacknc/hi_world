#!/usr/bin/env python
from xml.etree.ElementTree import Element

import requests
from xml.etree import ElementTree
import re
from datetime import datetime, timedelta
from locators import WeatherLocators
import mysql.connector
from datetime import datetime

#############################################
# determins location from IP address then
# uses the IP address to get the 3 day forcast
############################################


url = 'https://api.ipify.org/?format=xml'

response = requests.get(url)

ip_address = response.text


url = "http://api.weatherapi.com/v1/forecast.xml?"

queryURL = url + f"key=5bfef5467dd54a41a8a113336222805"
queryURL += f"&q={ip_address}"
queryURL += f"&days=3"
queryURL += f"&aqi=no"
queryURL += f"&alerts=no"

response = requests.get(queryURL)

dom = ElementTree.fromstring(response.text)

datas = dom.findall('forecast/forecastday')

print("Content-type:text/html\r\n\r\n")
print('<html>')
print('<head>')
try:

    for data in datas:
        ds = data.findall('hour')
        #ds = data.findall('hour')
        dat: Element
        for dat in reversed(ds):
            print("")
            time = dat.find('time').text
            print(f"{time}")
            print(f"-------------------------------")
            temp_f = dat.find('temp_f').text
            print(f"Temperature\t{temp_f} F")
            cond = dat.findall('condition')
            for c in cond:
                condition = c.find('text').text
                print(f"\t\t{condition}")
                
            wind_mph = dat.find('wind_mph').text
            print(f"Wind Speed\t{wind_mph} MPH")
            wind_dir = dat.find('wind_dir').text
            print(f"Wind Direction\t{wind_dir}")
            precip_in = dat.find('precip_in').text
            print(f"Precipitation\t{precip_in} inch")
            humidity = dat.find('humidity').text
            print(f"Humidity\t{humidity} %")
            cloud = dat.find('cloud').text
            print(f"Cloud Cover\t{cloud} %")

    print(f"")
    print(f"Current Conditions")
    print(f"-------------------------------")
    
    curr = dom.findall('current')
    for c in curr:
        last_updated = c.find('last_updated').text
        print(f"Last Updated\t{last_updated}")
        temp_f = c.find('temp_f').text
        print(f"Temperature\t{temp_f} F")
        cond = dat.findall('condition')
        for co in cond:
            condition = co.find('text').text
            print(f"\t\t{condition}")
        wind_mph = c.find('wind_mph').text
        print(f"Wind Speed\t{wind_mph} MPH")
        wind_dir = c.find('wind_dir').text
        print(f"Wind Direction\t{wind_dir}")
        precip_in = c.find('precip_in').text
        print(f"Precipitation\t{precip_in} inch")
        humidity = c.find('humidity').text
        print(f"Humidity\t{humidity} %")
        cloud = c.find('cloud').text
        print(f"Cloud Cover\t{cloud} %")    
        print(f"")    
        for data in datas:  
            date = data.find('date').text
            print(f"")
            print(f"Date\t\t{date}")
            astro = data.findall('astro')
            for ass in astro:
                sunrise = ass.find('sunrise').text
                print(f"Sunrise\t\t{sunrise}")
                sunset = ass.find('sunset').text
                print(f"Sunset\t\t{sunset}")
                moon_phase = ass.find('moon_phase').text
                print(f"Moon Phase\t{moon_phase}")           
        
        location = dom.findall('location')    
        for loc in location:
            print(f"")
            name = loc.find('name').text
            print(f"{name}")
            region = loc.find('region').text
            print(f"{region}")
            tz_id = loc.find('tz_id').text
            print(f"{tz_id}")
            print()
            print(f"{queryURL}")

except Exception as e: 
    print(e)

    print("crap-eth")