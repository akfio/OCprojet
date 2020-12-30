#Ensemble des fonctions comprises dans le process de scaping du site BookToScrap, activé par la fonction process.

def get_category_link():
    lks = []
    url = 'http://books.toscrape.com/catalogue/category/books_1/index.html'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    liens = soup.find('div', {'class': 'side_categories'}).find('ul', {'class': 'nav nav-list'}).find('li').find(
        'ul').find_all('li')
    for lien in liens:
        a = lien.find('a')
        link = 'http://books.toscrape.com/catalogue/category/' + a['href']
        links = link.replace('../', '')
        lks.append(links)
    return lks


def get_category_name():
    noms_cat = []
    url = 'http://books.toscrape.com/catalogue/category/books_1/index.html'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    noms = soup.find('div', {'class': 'side_categories'}).find('ul', {'class': 'nav nav-list'}).find('li').find(
        'ul').find_all('li')
    for nom in noms:
        i = str.strip(nom.find('a').text)
        noms_cat.append(i)
    return noms_cat


def get_lst_products(url):
    lst = []
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
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


def dl_img(url, file_path, file_name):
    full_path = file_path + file_name.replace('/', '') + '.jpeg'
    urllib.request.urlretrieve(url, full_path)


def write_in_file(dico):
    img = []
    title = []
    dico4 = dict()
    for key, value in dico.items():
        p = pathlib.Path(key + "/")
        p.mkdir(parents=True, exist_ok=True)
        c = key + '.csv'
        filepath = p / c
        with filepath.open("w", encoding="utf-8") as file:
            csv_writer = csv.writer(file, delimiter='\t')
            csv_writer.writerow(
                ['product_page_url', 'universal_product_code', 'title', 'price_including_tax',
                 'price_excluding_tax',
                 'number_available', 'product_description', 'category', 'review_rating', 'image_url'])
            for data in value:
                csv.writer(file).writerow(data)
                img.append(data[-1])
                title.append(data[2])
    for i in range(len(img)):
        dico4[title[i]] = img[i]
    os.mkdir('Images/')
    for key, value in dico4.items():
        dl_img(value, 'Images/', key)


def process():
    lst_names = get_category_name()
    lst_url_categories = get_category_link()
    dico = dict()
    dico2 = dict()
    for i in range(len(lst_names)):
        dico[lst_names[i]] = lst_url_categories[i]
    for key, value in dico.items():
        lst_products_urls = get_lst_products(value)
        dico2[key] = lst_products_urls
    dico3 = dict()
    for key, value in dico2.items():
        dico3[key] = []
        for v in value:
            dico3[key].append(get_product_data(v))
    write_in_file(dico3)


process()
