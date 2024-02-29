#!/usr/bin/env python

import requests
from xml.etree import ElementTree
import re
from datetime import datetime, timedelta
from locators import WeatherLocators

#############################################
# determins location from IP address then
# uses the lat/long do get the 3 day forcast
############################################


url = 'https://api.ipify.org/?format=xml'

response = requests.get(url)

ip_address = response.text

url = 'http://ip-api.com/xml/'
url += ip_address
response = requests.get(url)

dom = ElementTree.fromstring(response.text)
data = dom.findall('query')

lat = dom.find('lat')
lon = dom.find('lon')
city = dom.find('city')
state = dom.find('regionName')
zipc = dom.find('zip')

url = "http://www.7timer.info/bin/api.pl?"

queryURL = url + f"lon={lon}/"
queryURL += f"&lat={lat}"
queryURL += f"&product=astro"
queryURL += f"&output=xml"

#lon=75.0149&lat=40.0115&product=astro&output=xml"
response = requests.get(queryURL)

dom = ElementTree.fromstring(response.text)

data = dom.findall('dataseries/data')

for c in reversed(data):

    print()
    time = c.get('timepoint')
    time = str.replace("h", "", time)
    d = datetime.now() + timedelta(hours=int(time))
    date = d.strftime("%Y-%m-%d %H:%M")
    print(f"Date\t\t{date}")
    print(f"------------------------------")
    cc = c.find('cloudcover').text
    print(f"cloudcover\t{WeatherLocators.CLOUDCOVER[int(cc)]}")
    vis = c.find('seeing').text
    print(f"Visibility\t{WeatherLocators.SEEING[int(vis)]}[km]")
    hum = c.find('rh2m').text
    print(f"Humidity\t{WeatherLocators.RH[int(hum)]}")

    print(f"Wind Dir\t{c.find('wind10m_direction').text}")
    ws = int(c.find('wind10m_speed').text)
    wsm = ws / 1.609
    wsm = "{:.2f}".format(wsm)

    print(f"Wind Speed\t{WeatherLocators.WINDSP[int(ws)]}")
    tempc = c.find('temp2m').text
    tempf = (int(tempc) * 9/5) + 32
    print(f"Temperature\t{tempc}[c] {tempf}[f]")
    print(f"Precip Type\t{c.find('prec_type').text}")

print()
print(f"{city.text}")
print(f"{state.text}, {zipc.text}")
print(f" Latitude = {lat.text}")
print(f" Longitude = {lon.text}")
