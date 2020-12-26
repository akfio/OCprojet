import requests
from bs4 import BeautifulSoup

url = 'http://books.toscrape.com/catalogue/its-only-the-himalayas_981/index.html'


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
    book_info = {product_page_url,
                 universal_product_code,
                 title,
                 price_including_tax,
                 price_excluding_tax,
                 number_available,
                 product_description,
                 category,
                 review_rating,
                 image_url}
    return book_info


