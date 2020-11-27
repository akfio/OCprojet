import requests
from bs4 import BeautifulSoup

#url= 'http://books.toscrape.com/catalogue/category/books/poetry_23/index.html'
url = 'http://books.toscrape.com/catalogue/category/books/young-adult_21/index.html'
base_url = url.replace('index.html', '')
lst = []

def books_category_parse_page(url):
    reponse = requests.get(url)
    soup = BeautifulSoup(reponse.text, 'html.parser')
    liens = soup.find('ol', {'class': 'row'}).find_all('article', {'class': 'product_pod'})
    for lien in liens:
        a = lien.find('a')
        link = 'http://books.toscrape.com/catalogue/' + a['href']
        links = link.replace('../../../', '')
        print(links)
        lst.append(links)
    if soup.find('li', {'class': 'next'}) != None :
        np = soup.find('li', {'class': 'next'}).find('a')['href']
        next_page_url = base_url + np
        books_category_parse_page(next_page_url)
    else:
        ''

books_category_parse_page(url)
