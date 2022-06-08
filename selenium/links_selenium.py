#!/usr/bin/env python

from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


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
        f.close()
                
    def setUp(self, url, app, page):

        if app == 'Chrome':
        
            caps = DesiredCapabilities().CHROME
            #   caps["pageLoadStrategy"] = "normal"  #  Waits for full page load
            caps["pageLoadStrategy"] = "none"   # Do not wait for full page load

            self.driver = webdriver.Chrome(desired_capabilities=caps)

        elif app == 'Firefox':
            
            caps = DesiredCapabilities().FIREFOX
            #   caps["pageLoadStrategy"] = "normal"  #  Waits for full page load
            caps["pageLoadStrategy"] = "none"   # Do not wait for full page load
            self.driver = webdriver.Firefox(desired_capabilities=caps)
            #self.driver = webself.driver.Firefox(service=Service(GeckoDriverManager().install()))
        elif app == 'Edge':
        
            caps = DesiredCapabilities().EDGE
            #   caps["pageLoadStrategy"] = "normal"  #  Waits for full page load
            caps["pageLoadStrategy"] = "none"   # Do not wait for full page load
            
            #Edge driver doesn't appear to be allowing desired_capabilities to be passes
            #self.driver = webdriver.Edge(desired_capabilities=caps)
            self.driver = webdriver.Edge()
        elif app == 'headless':
                    
            caps = DesiredCapabilities().CHROME
            #   caps["pageLoadStrategy"] = "normal"  #  Waits for full page load
            caps["pageLoadStrategy"] = "none"   # Do not wait for full page load

            chrome_options = Options()
            
            #Headless is unstable
            #chrome_options.add_argument('--headless')
            chrome_options.add_argument('--no-sandbox')  
            chrome_options.add_argument('--disable-dev-shm-usage')        
            self.driver = webdriver.Chrome( options=chrome_options, desired_capabilities=caps )
        
        else:
            print(f"Unknown application passed {app}")
        
        #self.driver.set_page_load_timeout(10)
        self.driver.get(url)
     
        WebDriverWait(self.driver, 60).until(EC.presence_of_element_located((By.XPATH, ScrapeLocators.XPATHS[page])))
     
     
    def filterTxt(self, txt):
        #Filter out chars that were causing H&D with the output
        lnkTxt = re.sub("• ", "", txt)
        lnkTxt = re.sub("‘", "\'", lnkTxt)
        lnkTxt = re.sub("’", "\'", lnkTxt)
        lnkTxt = re.sub("’ ", "\' ", lnkTxt)
        lnkTxt = re.sub("\n", "", lnkTxt)
        lnkTxt = re.sub("\r", "", lnkTxt)
        
        return lnkTxt
     
    def checkURL(self, url):
    
        #Filters for unwanted links
        urlLink = url.get_attribute('href')
        if url.text == url.text[:10]: return False
        if url.text == url.text[0]: return False
        if url.text == url.text.upper(): return False
        if "C:" in urlLink: return False
                
        site = re.search('\w+\.com', urlLink)
        cname = url.get_attribute('class')
        if "c-button" in cname: return False
        if (cname == "") and ("billboard" in site.group()): return False
        if ("vibe" in site.group()): return False
  
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
        f.write(f"<br><div class='col-12 col-xl-12 mx-xl-auto  text-center text-light text-monospace'><h1>{text}</h1></div><br>\n")
        f.close()
        

crawl = Crawl()

crawl.setUpFile()
crawl.headline("News Headlines")
crawl.setUp('http://cnn.com', 'headless', 0)
crawl.getPage(0)
crawl.setUp('http://foxnews.com', 'Chrome', 1)
crawl.getPage(1)
crawl.setUp('https://www.nationalreview.com/', 'Edge', 6)
crawl.getPage(6)
crawl.setUp('https://www.msnbc.com/', 'Firefox', 2)
crawl.getPage(2)
crawl.setUp('https://www.nytimes.com/', 'headless', 3)
crawl.getPage(3)
crawl.setUp('https://www.reuters.com/', 'headless', 4)
crawl.getPage(4)
crawl.headline("Tech Headlines")
crawl.setUp('https://techcrunch.com/', 'headless', 7)
crawl.getPage(7)
crawl.setUp('https://www.wired.com/', 'headless', 8)
crawl.getPage(8)
crawl.setUp('https://thenextweb.com/', 'headless', 9)
crawl.getPage(9)
crawl.headline("Entertainment Headlines")
crawl.setUp('https://www.rollingstone.com/', 'headless', 10)
crawl.getPage(10)
crawl.setUp('https://www.billboard.com/c/music/', 'headless', 11)
crawl.getPage(11)
crawl.setUp('https://pitchfork.com/news/', 'headless', 12)
crawl.getPage(12)
crawl.setUp('https://www.wired.com/', 'headless', 13)
crawl.getPage(13)
crawl.cleanFile()

