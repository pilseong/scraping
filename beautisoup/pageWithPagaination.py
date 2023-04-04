from bs4 import BeautifulSoup
import requests


root = 'https://subslikescript.com'
website = f'{root}/movies_letter-A'
result = requests.get(website)
soup = BeautifulSoup(result.text, 'lxml')

# 마지막 페이지를 찾는다.
pagination = soup.find('ul', class_="pagination")
pages = pagination.find_all('li', class_="page-item")
last_page = pages[-2].text

# 각 페이지를 돌면서 안에 있는 정보를 가져온다.

last_page = 2
for page in range(1, last_page + 1):
    result = requests.get(f'{website}?page={page}')
    soup = BeautifulSoup(result.text, 'lxml')

    box = soup.find('article', class_="main-article")

    # 각 페이지에 포함된 링크를 가져온다.
    links = []
    for link in box.find_all('a', href=True):
        links.append(link['href'])

    # 각 링크의 정보를 가져온다.
    for link in links:
        try:
            each_result = requests.get(f'{root}/{link}')
            print(f'{root}/{link}')
            soup = BeautifulSoup(each_result.text, 'lxml')

            box = soup.find('article', class_="main-article")

            title = box.find('h1').get_text()
            script = box.find(
                'div', class_="full-script").get_text(strip=True, separator=' ')

            title = title.replace('/', '')

            with open(f'./scripts/{title}.txt', 'w') as file:
                file.write(script)
        except:
            print('--------------- Link is not working ----------------------')
            print(link)
