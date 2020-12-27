#Ensemble des fonctions

import requests
from bs4 import BeautifulSoup
import csv

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


def get_product_data(url):
    response = requests.get(url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'html.parser')
    td = soup.find_all('td')
    product_page_url = url
    universal_product_code = td[0].text
    title = soup.find('h1').text
    price_including_tax = td[2].text.replace('Â', '')
    price_excluding_tax = td[3].text.replace('Â', '')
    number_available = td[5].text.replace('In stock', '').replace('(', '').replace('available)', '')
    product_description = soup.find_all('p')[3].text
    category = str.strip(soup.find_all('li')[2].text)
    review_rating = soup.find("p", "star-rating")["class"][-1]
    image_url = 'http://books.toscrape.com/' + soup.find("img")["src"].replace('../../', '')
    book_info = [product_page_url, universal_product_code, title, price_including_tax, price_excluding_tax,
                 number_available, product_description, category, review_rating, image_url]
    return book_info
