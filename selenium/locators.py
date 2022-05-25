from selenium.webdriver.common.by import By

class MainPageLocators(object):
    

    GO_BUTTON = (By.ID, 'submit')
    
    FAV_ICON  = (By.CLASS_NAME, "navbar-brand")
    
    TAG_A = (By.TAG_NAME,  "a")
    
    MENU_TWO_TOP = (By.ID, "navbarDropdown2")
    
    MENU_TWO_TITLES = ["mission", "conduct", "leadership", "positions", "positions"]
    
    MENU_ONE_TOP = (By.ID, "navbarDropdown1")

    MENU_ONE_LINKS = ["//*[@id='navbarResponsive']/ul/li[1]/div/a[1]", 
                 "//*[@id='navbarResponsive']/ul/li[1]/div/a[2]", 
                 "//*[@id='navbarResponsive']/ul/li[1]/div/a[3]",
                 "//*[@id='navbarResponsive']/ul/li[1]/div/a[4]",
                 "//*[@id='navbarResponsive']/ul/li[1]/div/a[5]",
                 "//*[@id='navbarResponsive']/ul/li[2]/a"
                 ]

    MENU_ONE_SEARCH = ["volunteer", "sponsor", "projects", "project_guidelines", "hackathons", "chat"]

    VIDEO_SUB = (By.XPATH, "//track[@label='English']")
    
    MODAL_LINK = (By.CLASS_NAME, 'portfolio-link')
    
    VOLENTEER_TITLES = ["volunteer"]   
    
    BLOG_OBJ = (By.CLASS_NAME, "blog_obj")