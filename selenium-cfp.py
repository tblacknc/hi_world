from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import time
import unittest

        
class TestStringMethods(unittest.TestCase):

    global driver

    def setUp(self):
 
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        #self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        
        #self.driver.get("https://codeforphilly.org/")
        self.driver.get("http://10.0.0.69:9080/")

            
    def test_video(self):
    
        try:
            titles = self.driver.find_element(By.XPATH, "//track[@label='English']")
        except:
            vid = "video with englich subtitles not seen at url - "+ self.driver.current_url
            self.assertEqual(1, 0, "video with english subtitles not seen at url")
    
    
    def test_modal(self):
    
        loop = 0 
        links = self.driver.find_elements(By.CLASS_NAME, "portfolio-link")
        
        for link in links:
            loop += 1
            try:
                time.sleep(1)
                link.click()
                #time.sleep(1)
                return by sending an esc to the modal
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
        
        if "volunteer" not in self.driver.current_url:
            self.assertEqual(1, 0, "volunteer not found in current url")

        time.sleep(1)
        #return by selecting the fav icon
        link = self.driver.find_element(By.CLASS_NAME, "navbar-brand")
        link.click()

    def test_blog(self):    
        loop = 0
        links=[]
        lnks = self.driver.find_elements(By.CLASS_NAME, "blog_obj")
        
        for link in lnks:
            links.append(link.get_attribute('href'))

        for link in links:
            loop +=1
            try:                         
                time.sleep(1)
                self.driver.get(link)
                time.sleep(1)
                    
                #return by selecting the fav icon
                link = self.driver.find_element(By.CLASS_NAME, "navbar-brand")
                link.click()
                #self.driver.back()
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
