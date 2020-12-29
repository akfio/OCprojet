import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

url = 'http://books.toscrape.com/catalogue/category/books/young-adult_21/index.html'



def get_lst_products(url):
    lst = []
    reponse = requests.get(url)
    soup = BeautifulSoup(reponse.text, 'html.parser')
    liens = soup.find('ol', {'class': 'row'}).find_all('article', {'class': 'product_pod'})
    for lien in liens:
        a = lien.find('a')
        link = 'http://books.toscrape.com/catalogue/' + a['href']
        links = link.replace('../../../', '')
        lst.append(links)
    if soup.find('li', {'class': 'next'}) is not None:
        np = soup.find('li', {'class': 'next'}).find('a')['href']
        a = urlparse(url).path
        b = a.index('/', 26)
        c = a[:b + 1]
        next_page_url = 'http://books.toscrape.com' + c + np
        data = get_lst_products(next_page_url)
        for d in data:
            lst.append(d)
    return lst
