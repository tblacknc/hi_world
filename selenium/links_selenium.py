#!/usr/bin/env python

from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
                
    def setUp(self, url, app, page):

        if app == 'Chrome':

            PATH = "C:\Program Files (x86)\chromedriver.exe"
            self.driver = webdriver.Chrome(PATH)

        elif app == 'Firefox':
            #PATH = "C:\Program Files (x86)\geckodriver.exe"
            PATH = "geckodriver.exe"
            #"geckodriver.exe"
            self.driver = webdriver.Firefox(executable_path=PATH)
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
        
        #self.driver.set_page_load_timeout(10)
        self.driver.get(url)
     
        #WebDriverWait(self.driver, 60).until(EC.presence_of_element_located((By.XPATH, ScrapeLocators.XPATHS[page])))
     
     
    def filterTxt(self, txt):
        lnkTxt = re.sub("• ", "", txt)
        lnkTxt = re.sub("‘", "\'", lnkTxt)
        lnkTxt = re.sub("’", "\'", lnkTxt)
        lnkTxt = re.sub("’ ", "\' ", lnkTxt)
        lnkTxt = re.sub("\n", "", lnkTxt)
        lnkTxt = re.sub("\r", "", lnkTxt)
        
        return lnkTxt
     
    def checkURL(self, url):
        urlLink = url.get_attribute('href')
        if url.text == url.text[:10]: return False
        if url.text == url.text[0]: return False
        if url.text == url.text.upper(): return False
        if "C:" in urlLink: return False
        
        cname = url.get_attribute('class')
        if "c-button" in cname: return False
  
        return True

    def getPage(self, page):
        print(f" ----->  page - {page}")
        print(f" ----->  ScrapeLocators.PAGES[page] - {ScrapeLocators.PAGES[page]}")
        print(f" ----->  ScrapeLocators.PAGES_TXT[page] - {ScrapeLocators.PAGES_TXT[page]}")
        loop = 0
        brk = 0
        f = open("links.html", "a")
        f.write(f"<div class='col-md-4  ml-0 mr-0 mt-3 mb-3'>")
        f.write(f"<h5><a href={ScrapeLocators.PAGES[page]} target='_blank'>{ScrapeLocators.PAGES_TXT[page]}</a></h5>\n")
        d = datetime.now()
        date = d.strftime("%Y-%m-%d %H:%M")

        f.write(f"<h6>{date}</h6>\n")
        print(f"XPATH ===== {ScrapeLocators.XPATHS[page]}")
        for link in self.driver.find_elements(By.XPATH, ScrapeLocators.XPATHS[page]) :   
            lnkTxts = link.text.split("\n")
            for lnkTxt in lnkTxts:
                if brk == 1:
                    break
                try:
                    
                    lnkAlt = re.sub("'", "", lnkTxt)
                    lnkAlt = re.sub("`", "", lnkAlt)
                    url = self.driver.find_element(By.PARTIAL_LINK_TEXT  , lnkTxt[:20])
                    
                    if self.checkURL(url):   
                        a = url.get_attribute('href')      
                        lnkTxt = self.filterTxt(lnkTxt)
                        #f.write(f"<a href='{a}' title='{lnkAlt}' target='_blank'>{url.text[:40]}...</a><br>\n")
                        f.write(f"<a href='{a}' title='{lnkAlt}' target='_blank'>{lnkTxt[:40]}...</a><br>\n")
                        print(f" ----->Wrote {url.text[:40]}")
                    else:
                        loop -= 1
                        print(f" ----->FAILED TO WRITE -----> {url.text[:40]}")
                except Exception as e: 
                    print(f"Exception ----- >=>> {e}")

                    print(f"-----> Failed  to write - {lnkTxt} {loop}")
                    loop -= 1
           
                loop += 1   
                if loop == 5:
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
    def headline(self, text):
        f = open("links.html", "a")
        #f.write(f"<div class='col-xl-auto  text-center fw-light text-monospace'><h3>{text}</h3></div><br>\n")
        f.write(f"<br><div class='col-12 col-xl-12 mx-xl-auto  text-center text-light text-monospace'><h1>{text}</h1></div><br>\n")
        

crawl = Crawl()

crawl.setUpFile()
crawl.headline("News Headlines")
crawl.setUp('http://cnn.com', 'Firefox', 0)
crawl.getPage(0)
crawl.setUp('http://foxnews.com', 'Firefox', 1)
crawl.getPage(1)
crawl.setUp('https://www.nationalreview.com/', 'Chrome', 6)
crawl.getPage(6)
crawl.setUp('https://www.msnbc.com/', 'Chrome', 2)
crawl.getPage(2)
crawl.setUp('https://www.nytimes.com/', 'Chrome', 3)
crawl.getPage(3)
crawl.setUp('https://www.reuters.com/', 'Chrome', 4)
crawl.getPage(4)
crawl.headline("Tech Headlines")
crawl.setUp('https://techcrunch.com/', 'Chrome', 7)
crawl.getPage(7)
crawl.setUp('https://www.wired.com/', 'Chrome', 8)
#crawl.getPage(8)
#crawl.setUp('https://mashable.com/tech', 'Chrome', 9)
crawl.getPage(9)
crawl.setUp('https://thenextweb.com/', 'Chrome', 10)
crawl.getPage(10)
crawl.headline("Entertainment Headlines")
crawl.setUp('https://www.rollingstone.com/', 'Chrome', 10)
crawl.getPage(11)
crawl.setUp('https://www.billboard.com/c/music/', 'Chrome', 10)
crawl.getPage(12)
# crawl.setUp('https://pitchfork.com/news/', 'Chrome', 10)
# crawl.getPage(13)
crawl.setUp('https://www.wired.com/', 'Chrome', 10)
crawl.getPage(14)
crawl.cleanFile()

