from selenium.webdriver.common.by import By

class ScrapeLocators(object):

    PAGES = ['http://cnn.com', 'http://foxnews.com', 'http://msnbc.com',
             'http://nyt.com', 'http://routers.com', 'https://news.google.com/', 'https://www.nationalreview.com/', 
             'https://techcrunch.com/', 'https://www.wired.com/', 'https://mashable.com/tech', 'https://thenextweb.com/', 'https://www.rollingstone.com/', 'https://www.billboard.com/c/music/', 'https://pitchfork.com/news/', 'http://wired.com/']

    PAGES_TXT =['CNN', 'Fox News', 'MSNBC', 'New York Times', 'Routers', 
                'Google', 'National Review', 'Tech Crunch', 'wired', 'mashable',
                'The Next Web', 'Rolling Stone', 'BillBoard', 'Pitchfork', 'Wired']
    
    XPATHS = ["//*[@id='homepage1-zone-1']",
              "//*[@id='wrapper']/div/div[2]/div[1]/main/div/div",
              "//*[@id='content']/div[6]/div/div[2]/div/div[1]",
              "//*[@id='site-content']/div/div[1]/div[2]/div",
              "//*[@id='main-content']/div[1]/div/div[1]",
              "//*[@id='yDmH0d']/c-wiz[1]/div/div[2]/div[2]/div/main/c-wiz/div[1]",
              "//*[@id='main']/section[1]/div[1]",
              "//*[@id='tc-main-content']/div[3]/div/div",
              "//*[@id='main-content']/div[1]/div[2]/div/div[2]",
              "/html/body/div[1]/div[3]/div[2]",
              "//*[@id='nextHome']/section[1]/div/div/div",
              "//*[@id='site_wrap']/div[2]/div[1]/div[1]/section",
              "//*[@id='main-wrapper']/main/div[2]/div/div[2]/div[2]/div[1]/div/ul", 
              "//*[@id='news-page']/div[1]/section",
              "//*[@id='main-content']/div[1]/div[1]/section/div[2]"]

              
    HEADER = '''
            <!DOCTYPE html>

            <html lang="en">

            <head>
                <meta charset="utf-8">
                <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                        
                <meta name="description" content="Some links">
                <title>Top Tens</title>

                <link rel="icon" type="image/x-icon" href="/favicon.ico">
                <!-- Font Awesome icons (free version)-->
                <script src="https://use.fontawesome.com/releases/v5.15.1/js/all.js" crossorigin="anonymous">
                </script>
                <!-- Google fonts-->
                <link href="https://fonts.googleapis.com/css?family=Montserrat:400,700" rel="stylesheet" type="text/css">
                <link href="https://fonts.googleapis.com/css?family=Droid+Serif:400,700,400italic,700italic" rel="stylesheet" type="text/css">
                <link href="https://fonts.googleapis.com/css?family=Roboto+Slab:400,100,300,700" rel="stylesheet" type="text/css">
                <!-- Core theme
                CSS (includes Bootstrap)-->
                <link rel='stylesheet' type='text/css' href='./styles.css'>
            </head>'''
              