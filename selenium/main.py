from selenium import webdriver
from selenium.webdriver.common.by import By

website = 'https://www.adamchoi.co.uk/overs/detailed'
# path = '/mnt/c/Users/heops/Downloads/chromedriver_win32/chromedriver'
path = '/home/pilseong/chromedriver_linux64/chromedriver'
chrome_options = webdriver.ChromeOptions()

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5615.49 Safari/537.36'
chrome_options.add_argument(f'user-agent={user_agent}')
chrome_options.add_argument('headless')
chrome_options.add_argument('--disable-infobars')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--remote-debugging-port=9222')
driver = webdriver.Chrome(path, options=chrome_options)
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
