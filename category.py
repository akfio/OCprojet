import requests
from bs4 import BeautifulSoup


def get_category_link():
    lks = []
    url = 'http://books.toscrape.com/catalogue/category/books_1/index.html'
    reponse = requests.get(url)
    soup = BeautifulSoup(reponse.text, 'html.parser')
    liens = soup.find('div', {'class': 'side_categories'}).find('ul', {'class': 'nav nav-list'}).find('li').find('ul').find_all('li')
    for lien in liens:
        a = lien.find('a')
        link = 'http://books.toscrape.com/catalogue/category/' + a['href']
        links = link.replace('../', '')
        lks.append(links)
    return lks

def get_category_name():
    noms_cat = []
    url = 'http://books.toscrape.com/catalogue/category/books_1/index.html'
    reponse = requests.get(url)
    soup = BeautifulSoup(reponse.text, 'html.parser')
    noms = soup.find('div', {'class': 'side_categories'}).find('ul', {'class': 'nav nav-list'}).find('li').find('ul').find_all('li')
    for nom in noms:
        i = str.strip(nom.find('a').text)
        noms_cat.append(i)
    return noms_cat
