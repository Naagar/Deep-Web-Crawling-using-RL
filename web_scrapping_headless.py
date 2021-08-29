# requirement 
# pip install selenium

# brew install chromedriver
# import the Webdriver from the Selenium package, configure Chrome with headless=True and set a window size (otherwise it is really small)
# drawback is that Chrome needs lots of memory / CPU power

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()

options.headless = True
options.add_argument("--window-size=1920,1200")
driver = webdriver.Chrome(options=options, executable_path=r'/usr/local/bin/chromedriver')
driver.get("https://news.ycombinator.com/")

# to get all anchors on a page
all_links = driver.find_elements_by_tag_name('a')

# save all the links in a text file to crawl further and extract the data 


driver.save_screenshot('hn_homepage.png')
driver.quit()