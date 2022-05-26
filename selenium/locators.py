from selenium.webdriver.common.by import By

class MainPageLocators(object):

    FAV_ICON  = (By.CLASS_NAME, "navbar-brand")
    
    TAG_A = (By.TAG_NAME,  "a")
    
    MENU_ONE_TOP = (By.ID, "navbarDropdown1")
    MENU_ONE_TITLES = ["volunteer", "sponsor", "projects", "project_guidelines", "hackathons", "chat"]
    MENU_ONE_LOOP = 5

    MENU_TWO_TOP = (By.ID, "navbarDropdown2")
    MENU_TWO_TITLES = ["mission", "conduct", "leadership", "positions", "contact"]
    MENU_TWO_LOOP = 4

    VIDEO_SUB = (By.XPATH, "//track[@label='English']")
    
    MODAL_LINK = (By.CLASS_NAME, 'portfolio-link')
    MODAL_COUNT = 6
    
    VOLENTEER_TITLES = ["volunteer"]  
    VOLENTEER_LINK = (By.CLASS_NAME, "main-volunteer-link")
    
    BLOG_OBJ = (By.CLASS_NAME, "blog_obj")
    
    SEARCH = "phlask"
    SEARCH_BOX = (By.ID, "js-site-search")
    SEARCH_TOP = (By.XPATH, "//*[@id='navbarSearchBarDropdown']/div[2]/a")
    SEARCH_FIRST_RESULT = "phlask"
    SEARCH_SECOND = (By.XPATH, "//*[@id='navbarSearchBarDropdown']/div[3]/a")
    SEARCH_SECOND_RESULT = "phlask_appeared"
   
    LOGIN_USER = (By.XPATH, "//*[@id='login']/div[1]/input")
    LOGIN_PASS = (By.XPATH, "//*[@id='login']/div[2]/input")
    USER = "test"
    PASS = "Test123!"
    LOGIN_BUTTON = (By.XPATH, "//*[@id='login']/div[3]/button")
    LOGIN_TXT = (By.XPATH, "//*[@id='navbarDropdown3']")
    USER_NAME = "TEST"
    
    BAD_PASS = "Test123"
    BAD_TXT = (By.CLASS_NAME, "text-danger")
    BAD_USER = "Login Failed"
                      
    INVOLVED_LINK = ["//*[@data-icon='hand-holding-medical']",
                     "//*[@data-icon='laptop-code']",
                     "//*[@data-icon='hands-helping']" ]
    INVOLVED_Title =["sponsor", "partnerships", "volunteer"]
    
    BOTTOM_LINK = ["Active Projects",
                   "Start a Project",
                   "Hackathons",
                   "Mission",
                   "Code Of Conduct",
                   "Leadership",
                   "Weekly Meetups",
                   "Contact",
                   "Slack"]
    BOTTOM_Title =["projects", "first-steps", "hackathons", "mission", "code_of_conduct",
                    "leadership", "hack_night_program_details", "contact", "slack"]    
    
    SOCIAL_LINK = ["//*[@data-icon='twitter']",
                   "//*[@data-icon='linkedin-in']",
                   "//*[@data-icon='facebook-f']", 
                   "//*[@data-icon='meetup']",
                   "//*[@data-icon='slack']"]
    SOCIAL_Title =["twitter", "linkedin", "facebook",
                   "meetup", "slack"]