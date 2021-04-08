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


def dragee_data(url):
    headers = {
        "user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 YaBrowser/20.9.3.126 Yowser/2.5 Safari/537.36"
    }

    req = requests.get(url, headers=headers, verify=False)

    soup = BeautifulSoup(req.text, "lxml")
    articles = soup.find_all("li", class_="b-find__item i-inline")

    for article in articles:
        import_url = f"https://arenda.dragee.ru{article.find('div', class_='b-offer__center').find('a').get('href')}"

        import_addresses = article.find('div', class_='b-offer__center').find('div', class_="b-offer__address").text
        import_address_more = import_addresses.replace('\n            \n            \n                ', '| ')
        import_address_big = import_address_more.replace('\n            \n        ', '')
        import_address_long = import_address_big.replace('\n            ', '')
        import_address = import_address_long.replace(',', '')

        import_rooms = article.find('div', class_='b-offer__center').find('div', class_="b-offer__title-block").find("a", class_="b-link b-offer__title i-inline").text
        import_room_more = import_rooms.replace('\n                ', '')
        import_room_big = import_room_more.replace('\n', '')
        import_room_long = import_room_big.replace('            ', '')
        import_room = import_room_long.replace('КОМН.КВАРТИРА', 'к')

        import_room_address = import_room + '| ' + import_address

        import_prices = article.find('div', class_='b-offer__right').find('div', class_="b-offer__price").text
        import_price_more = import_prices.replace('\n            ', '')
        import_price_big = import_price_more.replace('\xa0', ' ')
        import_price = import_price_big.replace('\nв месяц\n', ' Р в месяц')


        result.append(ParseResult(
            url=import_url,
            address=import_room_address,
            price=import_price,
        ))

        path = '/Projects/Bot_parser/dragee.csv'
        with open(path, 'w') as f:
            writer = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
            writer.writerow(HEADERS)
            for text in result:
                writer.writerow(text)
