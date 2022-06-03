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
    
        PATH = "C:\Program Files (x86)\chromedriver.exe"
 
        self.driver = webdriver.Chrome(PATH)
        #self.driver = webdriver.Firefox(executable_path=r'C:\Program Files (x86)\geckodriver.exe')

    
        #self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
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
            print("                       FAIL                    ")
            string = url + " not found in url - " + self.driver.current_url
            self.assertEqual(1, 0, string)
        
    def switchTabs(self):

        #get window handle
        currentWin = self.driver.current_window_handle

        #get child window
        handles = self.driver.window_handles

        for nextWin in handles:
            #switch focus to child window
            if(nextWin != currentWin):
                self.driver.switch_to.window(nextWin)
                break
    
    def login(self):
    
        link = self.driver.find_element(By.ID, "navbarDropdown4")
        link.click()

        self.driver.find_element(*MainPageLocators.LOGIN_USER).send_keys(*MainPageLocators.USER)
        self.driver.find_element(*MainPageLocators.LOGIN_PASS).send_keys(*MainPageLocators.PASS)

        enter = self.driver.find_element(*MainPageLocators.LOGIN_BUTTON)
        enter.click()
        
        txt = self.driver.find_element(*MainPageLocators.LOGIN_TXT)    
    
    
    def test_menu2(self):
    
        print(
        '''
        =======================================
        |           Test Menu 2               |
        =======================================
        '''
        )
    
        
        self.login()
        
        lnk = self.driver.find_element(*MainPageLocators.MENU_TWO_TOP)
        lnk.click()

        for loop in range(MainPageLocators.MENU_TWO_LOOP):
            nxtLnk = self.driver.find_element(locate_with(*MainPageLocators.TAG_A).below(lnk))
            
            nxtLnk = self.lnkSwap(nxtLnk, loop)
            
            if loop >= 2:
                time.sleep(1)
                nxtLnk = self.driver.find_element(locate_with(*MainPageLocators.TAG_A).above(nxtLnk))
                time.sleep(1)

            
            webdriver.ActionChains(self.driver).move_to_element(nxtLnk).click().perform()
            
            self.checkTitle(MainPageLocators.MENU_TWO_TITLES[loop])
            
            self.rtnFavIcon()

            lnk = self.driver.find_element(*MainPageLocators.MENU_TWO_TOP)
            lnk.click()
            
        print("                       PASS                    ")
        
    def tst_menu1(self):
    
        print(
        '''
        =======================================
        |           Test Menu 1               |
        =======================================
        '''
        )

        self.login()
        
        lnk = self.driver.find_element(*MainPageLocators.MENU_ONE_TOP)
        lnk.click()
        time.sleep(1)

        for loop in range(MainPageLocators.MENU_ONE_LOOP):

            nxtLnk = self.driver.find_element(locate_with(*MainPageLocators.TAG_A).below(lnk))
            
            nxtLnk = self.lnkSwap(nxtLnk, loop)
            if loop >= 2:
                time.sleep(1)
                nxtLnk = self.driver.find_element(locate_with(*MainPageLocators.TAG_A).above(nxtLnk))
                time.sleep(1)
            time.sleep(2)
            webdriver.ActionChains(self.driver).move_to_element(nxtLnk).click().perform()
            
            self.checkTitle(MainPageLocators.MENU_ONE_TITLES[loop])
            
            self.rtnFavIcon()

            lnk = self.driver.find_element(*MainPageLocators.MENU_ONE_TOP)
            lnk.click()
            
        print("                       PASS                    ")

 
    def tst_search(self):

        print(
        '''
        =======================================
        |           Test search               |
        =======================================
        '''
        )
    
        self.login()
        time.sleep(1)
        link = self.driver.find_element(*MainPageLocators.SEARCH_BOX)
        webdriver.ActionChains(self.driver).move_to_element(link).click().perform()
        time.sleep(1)
        webdriver.ActionChains(self.driver).send_keys(*MainPageLocators.SEARCH).perform()
        time.sleep(1)
        link = self.driver.find_element(*MainPageLocators.SEARCH_TOP)
        
        webdriver.ActionChains(self.driver).move_to_element(link).click().perform()
        time.sleep(1)
        self.checkTitle(MainPageLocators.SEARCH_FIRST_RESULT)
        self.rtnFavIcon()
        
        link = self.driver.find_element(*MainPageLocators.SEARCH_BOX)
        webdriver.ActionChains(self.driver).move_to_element(link).click().perform()
        time.sleep(1)
        webdriver.ActionChains(self.driver).send_keys(*MainPageLocators.SEARCH).perform()
        time.sleep(1)
        link = self.driver.find_element(*MainPageLocators.SEARCH_SECOND)
        
        webdriver.ActionChains(self.driver).move_to_element(link).click().perform()
        time.sleep(1)
        self.checkTitle(MainPageLocators.SEARCH_SECOND_RESULT)
        self.rtnFavIcon()        
        
        print("                       PASS                    ")
        
    def tst_good_login(self):

        print(
        '''
        =======================================
        |         Test good login             |
        =======================================
        '''
        )
        link = self.driver.find_element(By.ID, "navbarDropdown4")
        link.click()

        self.driver.find_element(*MainPageLocators.LOGIN_USER).send_keys(*MainPageLocators.USER)
        self.driver.find_element(*MainPageLocators.LOGIN_PASS).send_keys(*MainPageLocators.PASS)

        enter = self.driver.find_element(*MainPageLocators.LOGIN_BUTTON)
        enter.click()
        
        txt = self.driver.find_element(*MainPageLocators.LOGIN_TXT)
        
        if txt.text != MainPageLocators.USER_NAME:
            print("                       FAIL                    ")
            self.assertEqual(1, 0, "Test failed to login")
        
        print("                       PASS                    ")
        
    def tst_bad_login(self):

        print(
        '''
        =======================================
        |         Test bad login              |
        =======================================
        '''
        )
        
        link = self.driver.find_element(By.ID, "navbarDropdown4")
        link.click()

        self.driver.find_element(*MainPageLocators.LOGIN_USER).send_keys(*MainPageLocators.USER)
        self.driver.find_element(*MainPageLocators.LOGIN_PASS).send_keys(*MainPageLocators.BAD_PASS)

        enter = self.driver.find_element(*MainPageLocators.LOGIN_BUTTON)
        enter.click()
        
        txt = self.driver.find_element(*MainPageLocators.BAD_TXT)
        
        if MainPageLocators.BAD_USER not in txt.text:
            print("                       FAIL                    ")
            self.assertEqual(1, 0, "Test failed to fail login")
        
        print("                       PASS                    ")        
        
    def tst_video(self):
        
        print(
        '''
        =======================================
        |           Test Video                |
        =======================================
        '''
        )
        
        self.login()
        
        try:
            titles = self.driver.find_element(*MainPageLocators.VIDEO_SUB)
        except:
            print("                       FAIL                    ")
            self.assertEqual(1, 0, "video with english subtitles not seen at url")
            
        print("                       PASS                    ")

    def tst_volenteers(self):

        print(
        '''
        =======================================
        |         Test Volenteers             |
        =======================================
        '''
        )
        
        self.login()
        
        #playing with the volunteer link
        link = self.driver.find_element(*MainPageLocators.VOLENTEER_LINK)
        
        link.click()
        
        self.checkTitle(*MainPageLocators.VOLENTEER_TITLES)

        self.rtnFavIcon()
        print("                       PASS                    ")
    

    def tst_modal(self):
    
        print(
        '''
        =======================================
        |           Test Modals               |
        =======================================
        '''
        )
        
        self.login()
        
        loop = 0 
        
        for link in self.driver.find_elements(*MainPageLocators.MODAL_LINK):
            loop += 1
            try:
                time.sleep(2)
                link.click()
                time.sleep(3)
                #return by sending an esc to the modal
                webdriver.ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()
                
            except:
                print("                       FAIL                    ")
                string = "failed to load modal number" + str(loop)
                self.assertEqual(1, 0, string)
        if loop != MainPageLocators.MODAL_COUNT:
            print("                       FAIL                    ")
            string = "script only saw "+ str(loop) +" modals"
            self.assertEqual(1, 0, string)
            
        print("                       PASS                    ")


    def tst_blog(self):    
    
        print(
        '''
        =======================================
        |           Test Blogs                |
        =======================================
        '''
        )
        
        self.login()
        
        loop = 0
        links=[]
        
        for link in self.driver.find_elements(*MainPageLocators.BLOG_OBJ):
            links.append(link.get_attribute('href'))

        for link in links:
            loop +=1
            try:                         
                self.driver.get(link)
                    
                self.rtnFavIcon()
            except:
                string = "failed to load blog number"+ str(loop)
                print("                       FAIL                    ")
                self.assertEqual(1, 0, string)
        if loop != 4:
            string = "script only saw",loop,"blogs"
            print("               FAIL                    ")
            self.assertEqual(1, 0, string)
            
        print("                       PASS                    ")    
        
    def tst_involved(self):
    
        print(
        '''
        =======================================
        |      Test get involved Lnks         |
        =======================================
        '''
        )
    
        self.login()
    
        for x in range(3):
              
            enter = self.driver.find_element(By.XPATH, MainPageLocators.INVOLVED_LINK[x])
            
            webdriver.ActionChains(self.driver).move_to_element(enter).click().perform()

            if x == 1:
                self.switchTabs()
                
            self.checkTitle(MainPageLocators.INVOLVED_Title[x])

            if x == 1:
                self.switchTabs()

            self.rtnFavIcon()
        print("                       PASS                    ")

    def tst_bottom(self):
    
        print(
        '''
        =======================================
        |         Test Bottom Links           |
        =======================================
        '''
        )
    
        self.login()
        
        for x in range(9):

            enter = self.driver.find_element(By.LINK_TEXT, MainPageLocators.BOTTOM_LINK[x])
            
            webdriver.ActionChains(self.driver).move_to_element(enter).click().perform()
                
            self.checkTitle(MainPageLocators.BOTTOM_Title[x])

            self.driver.back()
            
        print("                       PASS                    ")
    
    def tst_social(self):
        
        print(
        '''
        =======================================
        |         Test Social Links           |
        =======================================
        '''
        )
        
        self.login()
        
        for x in range(5):
              
            enter = self.driver.find_element(By.XPATH, MainPageLocators.SOCIAL_LINK[x])
            
            webdriver.ActionChains(self.driver).move_to_element(enter).click().perform()
                
            self.checkTitle(MainPageLocators.SOCIAL_Title[x])

            self.driver.back()
        print("                       PASS                    ")
    
    
    def tearDown(self):
        
        self.driver.close()
    
if __name__ == '__main__':
    unittest.main()
