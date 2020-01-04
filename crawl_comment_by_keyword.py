import time
import urllib.request
import urllib.parse
import re
from selenium.webdriver import Chrome
from contextlib import closing
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

chrome_options = Options()  
chrome_options.add_argument("--headless")

# youtube_link = "https://www.youtube.com/watch?v=kffacxfA7G4"

def crawl_you(youtube_link):
    with closing(Chrome(chrome_options=chrome_options)) as driver:
        wait = WebDriverWait(driver,10)
        driver.get(youtube_link)

        limit = 5 #increase to get more conent
        for item in range(limit): 
            wait.until(EC.visibility_of_element_located((By.TAG_NAME, "body"))).send_keys(Keys.END)

        with open('comment','w+',encoding='utf-8') as f:
            for comment in wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#comment #content-text"))):
                f.write(comment.text)

# crawl_you("https://www.youtube.com/watch?v=kffacxfA7G4")

top = int(input('Amount video return:'))

query_string = urllib.parse.urlencode({"keywords: " : input()})
html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
print(search_results[:10])

for i in search_results[:top]:
    with open(i,'w+',encoding='utf-8') as f:
        crawl_you('http://www.youtube.com/watch?v='+i)
