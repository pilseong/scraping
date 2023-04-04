from bs4 import BeautifulSoup
import requests


root = 'https://kogle.tistory.com'
result = requests.get(root)
soup = BeautifulSoup(result.text, 'lxml')


# 마지막 페이지를 찾는다.
pagination = soup.find('span', class_="inner_paging")
pages = pagination.find_all('a', class_="link_page")
last_page = int(pages[-1].text)


# 각 페이지를 돌면서 안에 있는 정보를 가져온다.

# last_page = 2
for page in range(1, last_page + 1):
    result = requests.get(f'{root}?page={page}')
    soup = BeautifulSoup(result.text, 'lxml')

    box = soup.find('div', id="cMain")
    box = box.find_all('a', class_="link_post")
    # articles = box.find_all('a', href=True)
    # 각 페이지에 포함된 링크를 가져온다.
    links = []
    for link in box:
        links.append(link['href'])

    # print(links)
    # # 각 링크의 정보를 가져온다.
    for link in links:
        try:
            each_result = requests.get(f'{root}{link}')
            print(f'{root}{link}')
            soup = BeautifulSoup(each_result.text, 'lxml')

            box = soup.find('div', class_="skin_view")

            titleBox = box.find('h3', class_="tit_post")
            title = titleBox.find('a').get_text()

            script = box.find(
                'div', class_="tt_article_useless_p_margin contents_style").get_text(strip=True, separator=' ')

            title = title.replace('/', '')

            with open(f'./tistory/{title}.txt', 'w') as file:
                file.write(script)
        except:
            print('--------------- Link is not working ----------------------')
            print(link)
