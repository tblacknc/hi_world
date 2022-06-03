#!/usr/bin/env python


from selenium import webdriver
from selenium.webdriver.common.by import By
import re 
import os
from datetime import datetime, timedelta


def setUpFile():
    if os.path.exists("links.html"):
        os.remove("links.html")

def setUp(url, app):
    
    global driver
    PATH = "C:\Program Files (x86)\chromedriver.exe"
    
    if app == 'Chrome':
        PATH = "C:\Program Files (x86)\chromedriver.exe"
        driver = webdriver.Chrome(executable_path=PATH)
        #driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    elif app == 'Firefox':
        PATH = "C:\Program Files (x86)\geckodriver.exe"
        driver = webdriver.Firefox(executable_path=r'C:\Program Files (x86)\geckodriver.exe')
        #driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    elif app == 'Edge':
        PATH = "C:\Program Files (x86)\msedgedriver.exe"
        driver = webdriver.Edge(executable_path=r'C:\Program Files (x86)\msedgedriver.exe')
    
    
    else:
        print(f"Unknown application passed {app}")
    
    driver.get(url)
 
def getCNN():
    loop = 0
    f = open("links.html", "a")
    f.write(f"<h3><a href='http://cnn.com'>CNN</A></h3>\n")
    d = datetime.now()
    date = d.strftime("%Y-%m-%d %H:%M")
    f.write(f"<h4>{date}</h4>\n")
    
    for link in driver.find_elements(By.CLASS_NAME, "zn-homepage1-zone-1 ") :   
        
        lnkTxts = link.text.split("\n")
        for lnkTxt in lnkTxts:
            try:
                lnkTxt = re.sub("• ", "", lnkTxt)
                url = driver.find_element(By.PARTIAL_LINK_TEXT  , lnkTxt)
                a = url.get_attribute('href')
                
                print(f"  {url.text} - {a}")
                print()
                
                f.write(f"<a href='{a}'>{url.text[:80]}</a><br>\n")
                
            except:
                continue_link = ""
                url = ""
                print(f"link failed----->{lnkTxt}")
       
    f.close() 
    cleanUp()

def getFox():
    loop = 0
    f = open("links.html", "a")
    f.write(f"<h3><a href='https://www.foxnews.com/'>Fox News</A></h3>\n")
    d = datetime.now()
    date = d.strftime("%Y-%m-%d %H:%M")
    f.write(f"<h4>{date}</h4>\n")

    for link in driver.find_elements(By.CLASS_NAME, "main-primary") :           
        lnkTxts = link.text.split("\n")
        for lnkTxt in lnkTxts:
            try:
                lnkTxt = re.sub("• ", "", lnkTxt)
                url = driver.find_element(By.PARTIAL_LINK_TEXT  , lnkTxt)
                a = url.get_attribute('href')         
                x = url.text.upper()
                
                if x != url.text:
                    print(f"  {url.text} - {a}")
                    print()
                    
                    f.write(f"<a href='{a}'>{url.text[:80]}</a><br>\n")                   
            except:
                continue_link = ""
                url = ""
                print(f"link failed----->{lnkTxt}")
    print()
    
    f.close() 
    cleanUp()   
    
def cleanUp():
    driver.close()

setUpFile()
setUp('http://cnn.com', 'Edge')
getCNN()
setUp('http://foxnews.com', 'Edge')
getFox()
