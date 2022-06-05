import requests
from bs4 import BeautifulSoup

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
queryURL += f"&days=2"
queryURL += f"&aqi=no"
queryURL += f"&alerts=no"

response = requests.get(queryURL)

soup = BeautifulSoup(response.text, 'lxml')

first_child = soup.find("forecast").find("forecastday")
kids = first_child.find_all("hour")
for kid in kids:
    wind_dir = kid.find("wind_dir").text
    print(f"wind_dir = {wind_dir}")

    time = kid.find("time").text
    print(f"{time}")
    print(f"-------------------------------")
    temp_f = kid.find("temp_f").text
    print(f"Temperature\t{temp_f} F")
 
    cond = kid.find_all("condition")
    for c in cond:
        condition = c.find('text').text
        print(f"\t\t{condition}")
    wind_mph = kid.find("wind_mph").text
    print(f"Wind Speed\t{wind_mph} MPH")
    wind_dir = kid.find("wind_dir").text
    print(f"Wind Direction\t{wind_dir}")
    precip_in = kid.find("precip_in").text
    print(f"Precipitation\t{precip_in} inch")
    humidity = kid.find("humidity").text
    print(f"Humidity\t{humidity} %")
    cloud = kid.find("humidity").text
    print(f"Cloud Cover\t{cloud} %")
    print(f"")
print(f"Current Conditions")
print(f"-------------------------------")

curr = soup.find_all("current")

# curr = dom.findall('current')
for c in curr:
    last_updated = c.find('last_updated').text
    print(f"Last Updated\t{last_updated}")
    
    temp_f = c.find('temp_f').text
    print(f"Temperature\t{temp_f} F")
    
    cond = c.find_all("condition")
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
    
    astroDate = soup.find("forecast").find("forecastday")
    kids = astroDate.find_all("date")
 
    for kid in kids:  
        print(f"")
        print(f"Date\t\t{kid.text}")
        astro = astroDate.find_all('astro')
        for ass in astro:
            sunrise = ass.find('sunrise').text
            print(f"Sunrise\t\t{sunrise}")
            sunset = ass.find('sunset').text
            print(f"Sunset\t\t{sunset}")
            moon_phase = ass.find('moon_phase').text
            print(f"Moon Phase\t{moon_phase}")           
    
    location = soup.find("location")
    loc = location.find("name").text
    print(f"")
    name = location.find("name").text
    print(f"{name}")
    region = location.find('region').text
    print(f"{region}")
    tz_id = location.find('tz_id').text
    print(f"{tz_id}")
    print()
    print(f"{queryURL}")








