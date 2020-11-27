import requests
from bs4 import BeautifulSoup
import csv


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
    with open('allinfos.csv', 'w', newline='') as file:
        csv_writer = csv.writer(file, delimiter='\t')
        csv_writer.writerow(
            ['product_page_url', 'universal_product_code', 'title', 'price_including_tax', 'price_excluding_tax',
             'number_available', 'product_description', 'category', 'review_rating', 'image_url'])
        csv_writer.writerow(
            [product_page_url, universal_product_code, title, price_including_tax, price_excluding_tax,
             number_available,
             product_description, category, review_rating, image_url])
    return book_info


livre = extract_book_infos_from_url('http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html')
print(livre)


