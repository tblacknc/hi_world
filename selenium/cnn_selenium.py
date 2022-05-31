from selenium import webdriver
from selenium.webdriver.common.by import By
import re 
import os



def setUpFile():
    if os.path.exists("links.html"):
        os.remove("links.html")

def setUpCNN():

    global driver
    PATH = "C:\Program Files (x86)\chromedriver.exe"
    # PATH = "C:\Users\tblac\Desktop\work search\amazon\selenium\drivers\chromedriver.exe"  
    driver = webdriver.Chrome(PATH)
    # self.driver = webdriver.Firefox(executable_path=r'C:\Program Files (x86)\geckodriver.exe')


    # self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    # self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    
    # self.driver.get("https://codeforphilly.org/")
    driver.get("https://www.cnn.com/")
 
def setUpFox():

    global driver
    PATH = "C:\Program Files (x86)\chromedriver.exe"
    # PATH = "C:\Users\tblac\Desktop\work search\amazon\selenium\drivers\chromedriver.exe"  
    driver = webdriver.Chrome(PATH)
    # self.driver = webdriver.Firefox(executable_path=r'C:\Program Files (x86)\geckodriver.exe')


    # self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    # self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    
    # self.driver.get("https://codeforphilly.org/")
    driver.get("https://www.foxnews.com/")
 
def getRowCNN():
    loop = 0
    f = open("links.html", "a")
    f.write(f"<h3><a href='http://cnn.com'>CNN</A></h3>\n")

    for link in driver.find_elements(By.CLASS_NAME, "zn-homepage1-zone-1 ") :   
        #print(link.text, loop)
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
    driver.close()

def getRowFox():
    loop = 0
    f = open("links.html", "a")
    f.write(f"<h3><a href='https://www.foxnews.com/'>Fox News</A></h3>\n")

    for link in driver.find_elements(By.CLASS_NAME, "main-primary") :   
        #print(link.text, loop)
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
    #print(heads)
    f.close() 
    driver.close()

setUpFile()
setUpCNN()
getRowCNN()
setUpFox()
getRowFox()