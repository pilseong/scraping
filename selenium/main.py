from selenium import webdriver
from selenium.webdriver.common.by import By

website = 'https://www.adamchoi.co.uk/overs/detailed'
# path = '/mnt/c/Users/heops/Downloads/chromedriver_win32/chromedriver'
path = '/home/heops/chromedriver_linux64/chromedriver'
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--disable-infobars')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--no-sandbox')
options.add_argument('--remote-debugging-port=9222')
driver = webdriver.Chrome(path, options=options)
driver.get(website)

all_matches_btn = driver.find_element(
    'xpath', '//label[@analytics-event="All matches" ]')
all_matches_btn.click()

matches = driver.find_elements(By.TAG_NAME, 'tr')

date = []
home_team = []
sccore = []
away_team = []

for match in matches:
    date.append(match.find_element(By.XPATH, '//tr/td[1]').text)
    home_team.append(match.find_element(By.XPATH, '//tr/td[2]').text)
    sccore.append(match.find_element(By.XPATH, '//tr/td[3]').text)
    away_team.append(match.find_element(By.XPATH, '//tr/td[4]').text)

print(date)

driver.quit()
