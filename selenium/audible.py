from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
import pandas as pd
import time

website = 'https://www.adamchoi.co.uk/overs/detailed'
path = '/home/pilseong/chromedriver_linux64/chromedriver'
chrome_options = Options()
chrome_options.headless = True
chrome_options.add_argument('window-size=1920x1080')

driver = webdriver.Chrome(path, options=chrome_options)
driver.get(website)

all_matches_btn = driver.find_element(
    'xpath', '//label[@analytics-event="All matches" ]')
all_matches_btn.click()

country_drop_down = Select(driver.find_element(By.ID, 'country'))
country_drop_down.select_by_visible_text('Japan')

time.sleep(3)

matches = driver.find_elements(By.TAG_NAME, 'tr')

date = []
home_team = []
sccore = []
away_team = []

for match in matches:
    date.append(match.find_element(By.XPATH, './td[1]').text)
    home_team.append(match.find_element(By.XPATH, './td[2]').text)
    sccore.append(match.find_element(By.XPATH, './td[3]').text)
    away_team.append(match.find_element(By.XPATH, './td[4]').text)

driver.quit()

df = pd.DataFrame({
    'data': date,
    'home_team': home_team,
    'score': sccore,
    'away_team': away_team
})
df.to_csv('japan_data.csv', index=False)



