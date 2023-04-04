from bs4 import BeautifulSoup
import requests


root = 'https://subslikescript.com'
website = f'{root}/movies'
result = requests.get(website)
soup = BeautifulSoup(result.text, 'lxml')

box = soup.find('article', class_="main-article")

links = []
for link in box.find_all('a', href=True):
  links.append(link['href'])

for link in links:  
  each_result = requests.get(f'{root}/{link}')
  print(f'{root}/{link}')
  soup = BeautifulSoup(each_result.text, 'lxml')
  
  box = soup.find('article', class_="main-article")
  
  title = box.find('h1').get_text()
  script = box.find('div', class_="full-script").get_text(strip=True, separator=' ')

  title = title.replace('/', '')
  with open(f'{title}.txt', 'w') as file:
      file.write(script)