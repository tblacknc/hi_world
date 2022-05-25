from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from selenium.webdriver.support.relative_locator import locate_with


import time
import unittest

from locators import MainPageLocators

        
class TestStringMethods(unittest.TestCase):

    global driver

    def setUp(self):
    
        #PATH = "C:\Program Files (x86)\chromedriver.exe"
        #PATH = "C:\Users\tblac\Desktop\work search\amazon\selenium\drivers\chromedriver.exe"  
        #self.driver = webdriver.Chrome(PATH)
        #self.driver = webdriver.Firefox(executable_path=r'C:\Program Files (x86)\geckodriver.exe')

    
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        #self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        
        #self.driver.get("https://codeforphilly.org/")
        self.driver.get("http://10.0.0.69:9080/")
    def rtnFavIcon(self):
        
        #return by selecting the fav icon
        link = self.driver.find_element(*MainPageLocators.FAV_ICON)
        link.click()
        
    def lnkSwap(self, nxtLnk, count):
    
        for x in range(count):
            lnk = nxtLnk
            nxtLnk = self.driver.find_element(locate_with(*MainPageLocators.TAG_A).below(lnk)) 
    
        return nxtLnk
        
    def checkTitle(self, url):
    
        if url not in self.driver.current_url:
            string = url + " not found in url - " + self.driver.current_url
            self.assertEqual(1, 0, string)

    
    def test_menu2(self):
    
        lnk = self.driver.find_element(*MainPageLocators.MENU_TWO_TOP)
        lnk.click()
        time.sleep(2)

        nxtLnk = self.driver.find_element(locate_with(*MainPageLocators.TAG_A).below(lnk))
        webdriver.ActionChains(self.driver).move_to_element(nxtLnk).click().perform()
        
        self.checkTitle(MainPageLocators.MENU_TWO_TITLES[0])
        
        time.sleep(1)
        self.rtnFavIcon()
        
        lnk = self.driver.find_element(*MainPageLocators.MENU_TWO_TOP)
        lnk.click()
        time.sleep(2)

        nxtLnk = self.driver.find_element(locate_with(*MainPageLocators.TAG_A).below(lnk))
        
        nxtLnk = self.lnkSwap(nxtLnk, 1)
        webdriver.ActionChains(self.driver).move_to_element(nxtLnk).click().perform()

        time.sleep(1)
        
        self.checkTitle(MainPageLocators.MENU_TWO_TITLES[1])
        
        self.rtnFavIcon()

        lnk = self.driver.find_element(*MainPageLocators.MENU_TWO_TOP)
        lnk.click()
        time.sleep(2)
        nxtLnk = self.driver.find_element(locate_with(*MainPageLocators.TAG_A).below(lnk))
        
        nxtLnk = self.lnkSwap(nxtLnk, 2)
        
        webdriver.ActionChains(self.driver).move_to_element(nxtLnk).click().perform()

        time.sleep(1)
        
        self.checkTitle(MainPageLocators.MENU_TWO_TITLES[2])
        
        self.rtnFavIcon()        
        
        lnk = self.driver.find_element(*MainPageLocators.MENU_TWO_TOP)
        lnk.click()
        time.sleep(2)
        
        nxtLnk = self.driver.find_element(locate_with(*MainPageLocators.TAG_A).below(lnk))
        
        nxtLnk = self.lnkSwap(nxtLnk, 3)
        
        webdriver.ActionChains(self.driver).move_to_element(nxtLnk).click().perform()        
        
        time.sleep(2)
        
        self.checkTitle(MainPageLocators.MENU_TWO_TITLES[3])
        
        self.rtnFavIcon()
        
        time.sleep(2)
        
        lnk = self.driver.find_element(*MainPageLocators.MENU_TWO_TOP)
        lnk.click()
        time.sleep(2)

        nxtLnk = self.lnkSwap(nxtLnk, 4)
        
        webdriver.ActionChains(self.driver).move_to_element(nxtLnk).click().perform()        
        time.sleep(2)
        
        self.checkTitle(MainPageLocators.MENU_TWO_TITLES[4])
        
        self.rtnFavIcon()
        time.sleep(2)
    
    def test_menu(self):
               
        
        loop = 0
     
        for link in MainPageLocators.MENU_ONE_LINKS:
            
            time.sleep(2)
            lnk = self.driver.find_element(*MainPageLocators.MENU_ONE_TOP)
            lnk.click()

            time.sleep(1)
            
            select = self.driver.find_element(By.XPATH, link)
            select.click()
            time.sleep(1)
            
            self.checkTitle(MainPageLocators.MENU_ONE_SEARCH[loop])            
            self.rtnFavIcon()
            
            loop += 1
            
    def test_video(self):
    
        try:
            titles = self.driver.find_element(*MainPageLocators.VIDEO_SUB)
        except:
            self.assertEqual(1, 0, "video with english subtitles not seen at url")
    
    
    def test_modal(self):
    
        loop = 0 
        #links = self.driver.find_elements(By.CLASS_NAME, 'portfolio-link')
        print("PORTFOLIO LINK --->",MainPageLocators.MODAL_LINK)

        
        for link in self.driver.find_elements(*MainPageLocators.MODAL_LINK):
            loop += 1
            try:
                time.sleep(2)
                link.click()
                time.sleep(1)
                #return by sending an esc to the modal
                webdriver.ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()
            except:
                string = "failed to load modal number" + str(loop)
                self.assertEqual(1, 0, string)
        if loop != 6:
            string = "script only saw "+ str(loop) +" modals"
            self.assertEqual(1, 0, string)

    def test_volenteers(self):

        #playing with the volunteer link
        link = self.driver.find_element(By.CLASS_NAME, "main-volunteer-link")
        
        link.click()
        
        self.checkTitle(*MainPageLocators.VOLENTEER_TITLES)

        time.sleep(1)
        self.rtnFavIcon()

    def test_blog(self):    
        loop = 0
        links=[]
        #lnks = self.driver.find_elements(*MainPageLocators.BLOG_OBJ)
        
        for link in self.driver.find_elements(*MainPageLocators.BLOG_OBJ):
            links.append(link.get_attribute('href'))

        for link in links:
            loop +=1
            try:                         
                time.sleep(1)
                self.driver.get(link)
                time.sleep(1)
                    
                self.rtnFavIcon()
            except:
                string = "failed to load blog number"+ str(loop)
                self.assertEqual(1, 0, string)
        if loop != 4:
            string = "script only saw",loop,"blogs"
            self.assertEqual(1, 0, string)
            
    def tearDown(self):
        
        self.driver.close()
    
if __name__ == '__main__':
    unittest.main()
