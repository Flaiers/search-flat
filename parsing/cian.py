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

def cian_data(url):
    headers = {
        "user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 YaBrowser/20.9.3.126 Yowser/2.5 Safari/537.36"
    }

    req = requests.get(url, headers=headers)

    soup = BeautifulSoup(req.text, "lxml")

    offers = soup.find("div", class_="_93444fe79c--wrapper--E9jWb")

    articles = offers.find_all("article", class_="_93444fe79c--container--2pFUD _93444fe79c--cont--1Ddh2")

    import_urls = []

    for article in articles:
        import_url = article.find('div', class_='_93444fe79c--general--2SDGY').find('a').get('href')
        import_urls.append(import_url)

        import_rooms = article.find('div', class_='_93444fe79c--container--JdWD4').find('span').text
        import_room_more = import_rooms.split(".")[0]
        import_room_big = import_room_more.replace("омн", "")

        try:
            if import_room_big.split("-")[1] == 'к':
                import_room = import_room_big
        except Exception:
            pass

        import_addresses = article.find('div', class_='_93444fe79c--labels--1J6M3').text
        import_address_more = import_addresses.split(", ")[3:7]
        import_address = " ".join(import_address_more)

        import_room_address = f'{import_room}| {import_address}'

        for import_url in import_urls:
            req1 = requests.get(import_url, headers=headers)
            soup_next = BeautifulSoup(req1.text, "lxml")

            import_prices = soup_next.find("div", class_="a10a3f92e9--terms--3V3cz").find("span").find("span").get("content")
            import_price = import_prices.replace("₽/мес.", "Р в месяц")

            result.append(ParseResult(
                url=import_url,
                address=import_room_address,
                price=import_price,
            ))

            path = 'site_parser/cian.csv'
            with open(path, 'w') as f:
                writer = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
                writer.writerow(HEADERS)
                for item in result:
                    writer.writerow(item)
