import requests
import json
from numerize import numerize

def stockDate():
    url = "https://api.polygon.io/v1/open-close/"

    ticker = input("Enter Symbol:")
    date = input("Enter date:")

    if not ticker:
        ticker = "CSCO"
        date = "2020-10-14"
        
    key = "s2_m3Ptpdhop0_1IHLI6OuRQiKUmxZBZ"

    ticker = ticker.upper()

    queryURL = url + f"{ticker}/"
    queryURL += f"{date}"
    queryURL += f"?adjusted=true"
    queryURL += f"&apiKey={key}"
     
    response = requests.get(queryURL)
    
    userdata = json.loads(response.text)
    try:
        print()
        print(f"Symbol\t\t{userdata['symbol']}")
        print("-----------------------------")  
        print(f"Date\t\t{date}")
        print(f"Opening\t\t{userdata['open']}")
        print(f"High\t\t{userdata['high']}")
        print(f"Low\t\t{userdata['low']}")
        print(f"After Hours\t{userdata['afterHours']}")
        print()
        print(queryURL)
    except:
        print("An error occured")
        print(queryURL)
        print(response.text)
        
def stockYesterday():

    url = "https://api.polygon.io/v2/aggs/ticker/"
    
    ticker = "CSCO"
    key = "s2_m3Ptpdhop0_1IHLI6OuRQiKUmxZBZ"

    queryURL = url + f"{ticker}"
    queryURL += f"/prev?adjusted=true"
    queryURL += f"&apiKey={key}"
     
    response = requests.get(queryURL)
    userdata = json.loads(response.text)
    results = userdata["results"]

    prnVol = "Volume"
    prnOpen = "Open"
    prnClose = "Close"
    prnHigh = "High"
    prnLow = "Low"

    for data in range(int(userdata['count'])):
        vol = numerize.numerize(results[data]['v'])    
        prnVol += f"\t{vol}"  
        prnOpen += f"\t{results[data]['o']}"
        prnClose += f"\t{results[data]['c']}"
        prnHigh += f"\t{results[data]['h']}"
        prnLow += f"\t{results[data]['l']}"
   
    print()
    print("Yesterday")
    print("-----------------------------")
    print(prnVol)
    print(prnOpen)
    print(prnClose)
    print(prnHigh)
    print(prnLow)
    print()
    print(queryURL)

stockDate()
stockYesterday()