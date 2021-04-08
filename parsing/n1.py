import requests
import collections
import csv
from bs4 import BeautifulSoup

ParseResult = collections.namedtuple(
    'ParseResult',
    (
        'url',
        'address',
        'price',
    ),
)

HEADERS = (
    'Ссылка',
    'Адрес',
    'Цена',
)

result = []

def n1_data(url):
    headers = {
        "user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 YaBrowser/20.9.3.126 Yowser/2.5 Safari/537.36"
    }

    req = requests.get(url, headers=headers)

    soup = BeautifulSoup(req.text, "lxml")
    articles = soup.find_all("article", class_="living-search-item__card _show")

    for article in articles:
        import_url = f"https://ekaterinburg.n1.ru{article.find('div', class_='card-title living-list-card__inner-block').find('a').get('href')}"

        import_prices = article.find('div', class_='living-list-card-price__item _object').text
        import_price = import_prices.replace("\xa0/мес.", " Р в месяц")
        import_rooms_addresses = article.find('div', class_='card-title living-list-card__inner-block').find('span', class_='link-text').text
        import_room_address_more = import_rooms_addresses.replace('к,', 'к|')
        import_room_address = import_room_address_more.replace(',', '')

        result.append(ParseResult(
            url=import_url,
            address=import_room_address,
            price=import_price,
        ))

        path = '/Projects/Bot_parser/n1.csv'
        with open(path, 'w') as f:
            writer = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
            writer.writerow(HEADERS)
            for item in result:
                writer.writerow(item)
