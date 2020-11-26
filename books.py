#Ensemble des fonctions

import requests
from bs4 import BeautifulSoup
import csv

def liens_categories():
    url = 'http://books.toscrape.com/catalogue/category/books_1/index.html'
    reponse = requests.get(url)
    soup = BeautifulSoup(reponse.text, 'html.parser')
    liens = soup.find('div', {'class': 'side_categories'}).find('ul', {'class': 'nav nav-list'}).find('li').find('ul').find_all('li')
    for lien in liens:
        a = lien.find('a')
        link = 'http://books.toscrape.com/catalogue/category/' + a['href']
        links = link.replace('../', '')
        print(links)

def categories_names():
    names = []
    url = 'http://books.toscrape.com/catalogue/category/books_1/index.html'
    reponse = requests.get(url)
    soup = BeautifulSoup(reponse.text, 'html.parser')
    noms = soup.find('div', {'class': 'side_categories'}).find('ul', {'class': 'nav nav-list'}).find('li').find('ul').find_all('li')
    for nom in noms:
        i = str.strip(nom.find('a').text)
        names.append(i)
    print(names)

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


def extract_book_infos_from_url(url):
    reponse = requests.get(url)
    soup = BeautifulSoup(reponse.text, 'html.parser')
    td = soup.find_all('td')
    product_page_url = url
    universal_product_code = td[0].text
    title = soup.find('h1').text
    price_including_tax = (td[2].text).replace('Â', '')
    price_excluding_tax = (td[3].text).replace('Â', '')
    number_available = (td[5].text).replace('In stock', '').replace('(', '').replace('available)', '')
    product_description = soup.find_all('p')[3].text
    category = str.strip(soup.find_all('li')[2].text)
    review_rating = soup.find("p", "star-rating")["class"][-1]
    image_url = 'http://books.toscrape.com/' + soup.find("img")["src"]
    book_info = {'product_page_url': product_page_url,
            'universal_product_code': universal_product_code,
            'title': title,
            'price_including_tax': price_including_tax,
            'price_excluding_tax': price_excluding_tax,
            'number_available': number_available,
            'product_description': product_description,
            'category': category,
            'review_rating': review_rating,
            'image_url': image_url}
    return book_info


livre = extract_book_infos_from_url('http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html')
print(livre)
