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


def avito_data(url):
    headers = {
        "user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 YaBrowser/20.9.3.126 Yowser/2.5 Safari/537.36"
    }

    req = requests.get(url, headers=headers)

    soup = BeautifulSoup(req.text, "lxml")
    articles = soup.find_all("div", class_="item__line")
    
    for article in articles:
        import_url = f"https://www.avito.ru{article.find('div', class_='snippet-title-row').find('a').get('href')}"

        import_rooms = article.find('div', class_='snippet-title-row').find('a').get('title')
        import_room = import_rooms.split(' ')[0]

        import_addresses = article.find('div', class_='item-address').find('span').text
        import_address_more = import_addresses.replace('\n ', '')
        import_address = import_address_more.replace(',', '')

        import_room_address = f'{import_room}| {import_address}'

        import_prices = article.find('div', class_='snippet-price-row').find('span').text
        import_price_more = import_prices.replace('\n ', '')
        import_price = import_price_more.replace('  ₽в месяц ', ' Р в месяц')

        result.append(ParseResult(
            url=import_url,
            address=import_room_address,
            price=import_price,
        ))

        path = 'site_parser/avito.csv'
        with open(path, 'w') as f:
            writer = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
            writer.writerow(HEADERS)
            for item in result:
                writer.writerow(item)
