import time
from selenium.webdriver import Chrome
from contextlib import closing
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

chrome_options = Options()  
chrome_options.add_argument("--headless")

youtube_link = "https://www.youtube.com/watch?v=kffacxfA7G4"
with closing(Chrome(chrome_options=chrome_options)) as driver:
    wait = WebDriverWait(driver,10)
    driver.get(youtube_link)

    limit = 5 #increase to get more conent
    for item in range(limit): 
        wait.until(EC.visibility_of_element_located((By.TAG_NAME, "body"))).send_keys(Keys.END)
        time.sleep(3)

    for comment in wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#comment #content-text"))):
        print(comment.text)