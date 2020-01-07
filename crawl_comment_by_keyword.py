import time
import urllib.request
import urllib.parse
import re
from selenium.webdriver import Chrome
from contextlib import closing
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup

chrome_options = Options()  
chrome_options.add_argument("--headless")

# youtube_link = "https://www.youtube.com/watch?v=kffacxfA7G4"

ls = []
def crawl_you(youtube_link):
    with closing(Chrome(chrome_options=chrome_options)) as driver:
        wait = WebDriverWait(driver,10)
        driver.get(youtube_link)

        limit = 5 #increase to get more conent
        for item in range(limit): 
            wait.until(EC.visibility_of_element_located((By.TAG_NAME, "body"))).send_keys(Keys.END)

        element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"h1.title yt-formatted-string"))).text

        # ls.append(element)
        with open('comment','w+',encoding='utf-8') as f:
        for comment in wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#comment #content-text"))):
        f.write(comment.text)
            print(comment.text)

# # crawl_you("https://www.youtube.com/watch?v=kffacxfA7G4")

# query_string = urllib.parse.urlencode({"keywords: " : input('input:')})
# html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
# search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
# print(search_results[:10])

# for i in search_results[:top]:
#     # with open(i,'w+',encoding='utf-8') as f:
#         crawl_you('http://www.youtube.com/watch?v='+i)

top = int(input('Amount video return:'))
textToSearch = input("Topic:")
query = urllib.parse.quote(textToSearch)
url = "https://www.youtube.com/results?search_query=" + query
response = urllib.request.urlopen(url)
html = response.read()
soup = BeautifulSoup(html, 'html.parser')

# ls = []
for vid in soup.findAll(attrs={'class':'yt-uix-tile-link'}):
    if not vid['href'].startswith("https://googleads.g.doubleclick.net/"):
        youtube_link = 'https://www.youtube.com' + vid['href']
        crawl_you(youtube_link)
           
