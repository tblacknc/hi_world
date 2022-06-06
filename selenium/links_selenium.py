#!/usr/bin/env python

from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
import re 
import os
from datetime import datetime, timedelta
from linkLocators import ScrapeLocators

class Crawl:

    def setUpFile(self):

        if os.path.exists("links.html"):
            os.remove("links.html")

        f = open("links.html", "a")
        f.write(f"{ScrapeLocators.HEADER}")
        f.write(f"<div class='container'>\n")
        f.write(f"<div class='row'>\n")
        #f.write(f"<div class='portfolio-item'\n")
        f.close()
                
    def setUp(self, url, app):

        if app == 'Chrome':

            PATH = "C:\Program Files (x86)\chromedriver.exe"
            self.driver = webdriver.Chrome(PATH)

        elif app == 'Firefox':
            PATH = "C:\Program Files (x86)\geckoself.driver.exe"
            self.driver = webdriver.Firefox(executable_path=r'C:\Program Files (x86)\geckoself.driver.exe')
            #self.driver = webself.driver.Firefox(service=Service(GeckoDriverManager().install()))
        elif app == 'Edge':
            PATH = "C:\Program Files (x86)\msedgeself.driver.exe"
            self.driver = webdriver.Edge(executable_path=r'C:\Program Files (x86)\msedgeself.driver.exe')
        elif app == 'headless':
            PATH = "C:\Program Files (x86)\chromeself.driver.exe"
            chrome_options = Options()
            #chrome_options.add_argument('--headless')
            chrome_options.add_argument('--no-sandbox')  
            chrome_options.add_argument('--disable-dev-shm-usage')        
            self.driver = webdriver.Chrome(executable_path="C:\Program Files (x86)\chromeself.driver.exe", options=chrome_options)
        
        else:
            print(f"Unknown application passed {app}")
        
        self.driver.get(url)
     
    def filterTxt(self, txt):
        lnkTxt = re.sub("• ", "", txt)
        lnkTxt = re.sub("‘", "\'", lnkTxt)
        lnkTxt = re.sub("’", "\'", lnkTxt)
        lnkTxt = re.sub("’ ", "\' ", lnkTxt)
        
        return lnkTxt
     
    def checkURL(self, url):
        if url == url[:10]: return False
        if url == url.upper(): return False
    
        return True

    def getPage(self, page):

        print(f" ----->  page - {page}")
        print(f" ----->  ScrapeLocators.PAGES[page] - {ScrapeLocators.PAGES[page]}")
        print(f" ----->  ScrapeLocators.PAGES_TXT[page] - {ScrapeLocators.PAGES_TXT[page]}")
        loop = 0
        brk = 0
        f = open("links.html", "a")
        f.write(f"<div class='col-md-4  ml-0 mr-0 mt-3 mb-3'>")
        f.write(f"<h5><a href={ScrapeLocators.PAGES[page]}>{ScrapeLocators.PAGES_TXT[page]}</A></h5>\n")
        d = datetime.now()
        date = d.strftime("%Y-%m-%d %H:%M")

        f.write(f"<h6>{date}</h6>\n")
        
        for link in self.driver.find_elements(By.XPATH, ScrapeLocators.XPATHS[page]) :   
            
            lnkTxts = link.text.split("\n")
            for lnkTxt in lnkTxts:
                if brk == 1:
                    break
                try:
                    lnkTxt = self.filterTxt(lnkTxt)
                    lnkAlt = re.sub("'", "", lnkTxt)
                    lnkAlt = re.sub("`", "", lnkAlt)
                    url = self.driver.find_element(By.PARTIAL_LINK_TEXT  , lnkTxt)
                    
                    a = url.get_attribute('href')         
                    
                    if self.checkURL(url.text):                    
                        f.write(f"<a href='{a}' title='{lnkAlt}'>{url.text[:40]}...</a><br>\n")
                        print(f" ----->Wrote {url.text[:40]}")
                    else:
                        loop -= 1
                        print(f" ----->Failed to write {url.text[:40]}")
                except Exception as e: 
                    print(f"Exception ----- >=>> {e}")
                    continue_link = ""
                    url = ""
                    print(f"-----> Failed  to write - {lnkTxt} {loop}")
                    loop -= 1
           
                loop += 1   
                if loop == 10:
                    brk = 1
        
        f.write(f"</div>\n") 
        f.close() 
        self.cleanUp()  

    def cleanUp(self):
        self.driver.close()
    def cleanFile(self):

        bottom = '''
            </div>
            </div>
            </div>
            </body>'''
        f = open("links.html", "a")
        f.write(f"{bottom}")
        f.close()


crawl = Crawl()

crawl.setUpFile()
crawl.setUp('http://cnn.com', 'Chrome')
crawl.getPage(0)
crawl.setUp('http://foxnews.com', 'Chrome')
crawl.getPage(1)
crawl.setUp('https://www.msnbc.com/', 'Chrome')
crawl.getPage(2)
crawl.setUp('https://www.nytimes.com/', 'Chrome')
crawl.getPage(3)
crawl.setUp('https://www.reuters.com/', 'Chrome')
crawl.getPage(4)
# crawl.setUp('https://www.npr.org', 'Chrome')
# crawl.getNational()
crawl.cleanFile()


