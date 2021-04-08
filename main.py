import time
import telebot
import kb

from parsing.n1 import n1_data
from parsing.dragee import dragee_data
from parsing.avito import avito_data
from parsing.cian import cian_data

from config import TOKEN
bot = telebot.TeleBot(TOKEN)

district = ''
room = ''
max_price = ''
min_price = ''
start_file = ''

district_n1 = ''
url_n1 = ''

district_dragee = ''
url_dragee = ''

district_avito = ''
url_avito = ''


district_cian = ''
url_cian = ''

# создание хэндлера старта
@bot.message_handler(commands=['start'])
def start_message(message):
	bot.send_message(message.chat.id, 'Пройди проверку на то, что ты не робот 🤖\n'
		'PS: Нажми ➡️ /main')

# создание хэндлера главное меню
@bot.message_handler(commands=['main'])
def main(message):
	bot.send_message(message.chat.id, 'Ты находишься в Главном меню, для поиска объявлений по аренде недвижимости в городе Екатеринбург, нажми соответствующую кнопку',
		reply_markup=kb.search)

# создание хэндлера сообщений
@bot.message_handler(content_types=['text'])
def messages(message):
	if message.text == '🏠 Главное меню':
		bot.send_message(message.chat.id, 'Ты находишься в Главном меню, для поиска объявлений по аренде недвижимости в городе Екатеринбург, нажми соответствующую кнопку',
			reply_markup=kb.search)

	elif message.text == '🔍 Поиск объявлений':
		bot.send_message(message.chat.id, 'Введи мне некоторые данные для поиска объявленией\n'
			'1) Выбери район, они представлены на кнопках, хочешь искать квартиры во всех районах, нажми соответствующую кнопку\n'
			'Если хочешь отменить поиск, нажми Отмена',
			reply_markup=kb.district_cancel)
		bot.register_next_step_handler(message, district_handler)

def district_handler(message):
	global district, district_n1, district_dragee, district_avito, district_cian
	district = message.text
	if district == '❌ Отмена':
		bot.send_message(message.chat.id, 'Ты возвращён в Главное меню, для поиска объявлений по городу Екатеринбург, нажми соответствующую кнопку',
			reply_markup=kb.search)

	elif district == 'Верх-Исетский':
		district_n1 = 'district-Verh-Isetskiy-rayon/'
		district_dragee = '&area=4&area=10&area=26'
		district_avito = '&district=787'
		district_cian = '&district%5B0%5D=286'
		bot.send_message(message.chat.id, f'Ты выбрал район - {district}\n'
			'2) Пришли мне количество комнат (1-4), если вариантов несколько, то напиши мне их слитно в порядке возрастания\n\n'
			'Пример: "Хочу только однокомнатную квартиру" — 1\n'
			'Пример: "Хочу однокомнатную, двухкомнатную квартиру" — 12\n'
			'Не правильно ввёл район, нажми ✏️ Редактровать\n'
			'Если хочешь отменить поиск, нажми Отмена',
			reply_markup=kb.edit_cancel)
		bot.register_next_step_handler(message, room_handler)

	elif district == 'Железнодорожный':
		district_n1 = 'district-Zheleznodorozhnyi-rayon/'
		district_dragee = '&area=3&area=13&area=18'
		district_avito = '&district=788'
		district_cian = '&district%5B0%5D=287'
		bot.send_message(message.chat.id, f'Ты выбрал район - {district}\n'
			'2) Пришли мне количество комнат (1-4), если вариантов несколько, то напиши мне их слитно в порядке возрастания\n\n'
			'Пример: "Хочу только однокомнатную квартиру" — 1\n'
			'Пример: "Хочу однокомнатную, двухкомнатную квартиру" — 12\n'
			'Не правильно ввёл район, нажми ✏️ Редактровать\n'
			'Если хочешь отменить поиск, нажми Отмена',
			reply_markup=kb.edit_cancel)
		bot.register_next_step_handler(message, room_handler)

	elif district == 'Кировский':
		district_n1 = 'district-Kirovskiy-rayon/'
		district_dragee = '&area=49&area=7&area=9&area=15&area=23'
		district_avito = '&district=789'
		district_cian = '&district%5B0%5D=289'
		bot.send_message(message.chat.id, f'Ты выбрал район - {district}\n'
			'2) Пришли мне количество комнат (1-4), если вариантов несколько, то напиши мне их слитно в порядке возрастания\n\n'
			'Пример: "Хочу только однокомнатную квартиру" — 1\n'
			'Пример: "Хочу однокомнатную, двухкомнатную квартиру" — 12\n'
			'Не правильно ввёл район, нажми ✏️ Редактровать\n'
			'Если хочешь отменить поиск, нажми Отмена',
			reply_markup=kb.edit_cancel)
		bot.register_next_step_handler(message, room_handler)

	elif district == 'Ленинский':
		district_n1 = 'district-Leninskiy-rayon/'
		district_dragee = '&area=29&area=20&area=28'
		district_avito = '&district=790'
		district_cian = '&district%5B0%5D=292'
		bot.send_message(message.chat.id, f'Ты выбрал район - {district}\n'
			'2) Пришли мне количество комнат (1-4), если вариантов несколько, то напиши мне их слитно в порядке возрастания\n\n'
			'Пример: "Хочу только однокомнатную квартиру" — 1\n'
			'Пример: "Хочу однокомнатную, двухкомнатную квартиру" — 12\n'
			'Не правильно ввёл район, нажми ✏️ Редактровать\n'
			'Если хочешь отменить поиск, нажми Отмена',
			reply_markup=kb.edit_cancel)
		bot.register_next_step_handler(message, room_handler)

	elif district == 'Октябрьский':
		district_n1 = 'district-Oktyabrskiy-rayon/'
		district_dragee = '&area=42&area=11&area=12&area=36&area=14&area=17'
		district_avito = '&district=791'
		district_cian = '&district%5B0%5D=290'
		bot.send_message(message.chat.id, f'Ты выбрал район - {district}\n'
			'2) Пришли мне количество комнат (1-4), если вариантов несколько, то напиши мне их слитно в порядке возрастания\n\n'
			'Пример: "Хочу только однокомнатную квартиру" — 1\n'
			'Пример: "Хочу однокомнатную, двухкомнатную квартиру" — 12\n'
			'Не правильно ввёл район, нажми ✏️ Редактровать\n'
			'Если хочешь отменить поиск, нажми Отмена',
			reply_markup=kb.edit_cancel)
		bot.register_next_step_handler(message, room_handler)

	elif district == 'Орджоникидзевский':
		district_n1 = 'district-Ordzhonikidzevskiy-rayon/'
		district_dragee = '&area=21&area=27'
		district_avito = '&district=792'
		district_cian = '&district%5B0%5D=288'
		bot.send_message(message.chat.id, f'Ты выбрал район - {district}\n'
			'2) Пришли мне количество комнат (1-4), если вариантов несколько, то напиши мне их слитно в порядке возрастания\n\n'
			'Пример: "Хочу только однокомнатную квартиру" — 1\n'
			'Пример: "Хочу однокомнатную, двухкомнатную квартиру" — 12\n'
			'Не правильно ввёл район, нажми ✏️ Редактровать\n'
			'Если хочешь отменить поиск, нажми Отмена',
			reply_markup=kb.edit_cancel)
		bot.register_next_step_handler(message, room_handler)

	elif district == 'Чкаловский':
		district_n1 = 'district-Chkalovskiy-rayon/'
		district_dragee = '&area=1&area=48&area=30&area=6&area=8&area=19&area=22'
		district_avito = '&district=793'
		district_cian = '&district%5B0%5D=291'
		bot.send_message(message.chat.id, f'Ты выбрал район - {district}\n'
			'2) Пришли мне количество комнат (1-4), если вариантов несколько, то напиши мне их слитно в порядке возрастания\n\n'
			'Пример: "Хочу только однокомнатную квартиру" — 1\n'
			'Пример: "Хочу однокомнатную, двухкомнатную квартиру" — 12\n'
			'Не правильно ввёл район, нажми ✏️ Редактровать\n'
			'Если хочешь отменить поиск, нажми Отмена',
			reply_markup=kb.edit_cancel)
		bot.register_next_step_handler(message, room_handler)

	elif district == 'Все районы':
		district_n1 = ''
		district_dragee = ''
		district_avito = ''
		district_cian = ''
		bot.send_message(message.chat.id, f'Ты выбрал все районы\n'
			'2) Пришли мне количество комнат (1-4), если вариантов несколько, то напиши мне их слитно в порядке возрастания\n\n'
			'Пример: "Хочу только однокомнатную квартиру" — 1\n'
			'Пример: "Хочу однокомнатную, двухкомнатную квартиру" — 12\n'
			'Не правильно ввёл район, нажми ✏️ Редактровать\n'
			'Если хочешь отменить поиск, нажми Отмена',
			reply_markup=kb.edit_cancel)
		bot.register_next_step_handler(message, room_handler)

	else:
		bot.send_message(message.chat.id, 'Ты вводишь не правильный район 🙃\n'
			'Нужно начать сначала, нажми Главное меню',
			reply_markup=kb.main)


def room_handler(message):
	global room, url_n1, url_dragee, url_avito, url_cian
	room = message.text
	if room == '❌ Отмена':
		bot.send_message(message.chat.id, 'Ты возвращён в Главное меню, для поиска объявлений по городу Екатеринбург, нажми соответствующую кнопку',
			reply_markup=kb.search)

	elif room == '✏️ Редактровать':
		bot.send_message(message.chat.id, 'Вижу, ты решил отредактировать район Екатеринбурга\n'
			'1) Выбери снова район, они представлены на кнопках, хочешь искать квартиры во всех районах, нажми соответствующую кнопку\n'
			'Если хочешь отменить поиск, нажми Отмена',
			reply_markup=kb.district_cancel)
		bot.register_next_step_handler(message, district_handler)

	elif room == '1':
		url_n1 = f'https://ekaterinburg.n1.ru/snyat/dolgosrochno/kvartiry/rooms-odnokomnatnye/{district_n1}?include_suburbs=false&limit=200&sort=-date'
		url_dragee = 'https://arenda.dragee.ru/offer/list/?autoscroll=.b-map-block&period=0&flat_type=0&cities=0&build_year=&sort=actual&novelty=4&rooms=1'
		url_avito = 'https://www.avito.ru/ekaterinburg/kvartiry/sdam/na_dlitelnyy_srok/1-komnatnye-ASgBAQICAkSSA8gQ8AeQUgFAzAgUjlk?cd=1&s=104'
		url_cian = 'https://ekb.cian.ru/cat.php?deal_type=rent&engine_version=2&offer_type=flat&region=4743&room1=1&type=4&with_neighbors=0&sort=creation_date_desc'
		bot.send_message(message.chat.id, 'Ты выбрал однокомнатную квартиру!\n'
			'3) Отправь максимальную цену аренды квартиры в месяц, валюта рубли\n'
			'Не правильно ввёл количество комнат, нажми ✏️ Редактровать\n'
			'Если хочешь отменить поиск, нажми Отмена',
			reply_markup=kb.edit_cancel)
		bot.register_next_step_handler(message, max_price_handler)

	elif room == '2':
		url_n1 = f'https://ekaterinburg.n1.ru/snyat/dolgosrochno/kvartiry/rooms-dvuhkomnatnye/{district_n1}?include_suburbs=false&limit=200&sort=-date'
		url_dragee = 'https://arenda.dragee.ru/offer/list/?autoscroll=.b-map-block&period=0&flat_type=0&cities=0&build_year=&sort=actual&novelty=4&rooms=2'
		url_avito = 'https://www.avito.ru/ekaterinburg/kvartiry/sdam/na_dlitelnyy_srok/2-komnatnye-ASgBAQICAkSSA8gQ8AeQUgFAzAgUkFk?cd=1&s=104'
		url_cian = 'https://ekb.cian.ru/cat.php?deal_type=rent&engine_version=2&offer_type=flat&region=4743&room2=1&type=4&with_neighbors=0&sort=creation_date_desc'
		bot.send_message(message.chat.id, 'Ты выбрал двухкомнатную квартиру!\n'
			'3) Отправь максимальную цену аренды квартиры в месяц, валюта рубли\n'
			'Не правильно ввёл количество комнат, нажми ✏️ Редактровать\n'
			'Если хочешь отменить поиск, нажми Отмена',
			reply_markup=kb.edit_cancel)
		bot.register_next_step_handler(message, max_price_handler)

	elif room == '3':
		url_n1 = f'https://ekaterinburg.n1.ru/snyat/dolgosrochno/kvartiry/rooms-trehkomnatnye/{district_n1}?include_suburbs=false&limit=200&sort=-date'
		url_dragee = 'https://arenda.dragee.ru/offer/list/?autoscroll=.b-map-block&period=0&flat_type=0&cities=0&build_year=&sort=actual&novelty=4&rooms=3'
		url_avito = 'https://www.avito.ru/ekaterinburg/kvartiry/sdam/na_dlitelnyy_srok/3-komnatnye-ASgBAQICAkSSA8gQ8AeQUgFAzAgUklk?cd=1&s=104'
		url_cian = 'https://ekb.cian.ru/cat.php?deal_type=rent&engine_version=2&offer_type=flat&region=4743&room3=1&type=4&with_neighbors=0&sort=creation_date_desc'
		bot.send_message(message.chat.id, 'Ты выбрал трёхкомнатную квартиру!\n'
			'3) Отправь максимальную цену аренды квартиры в месяц, валюта рубли\n'
			'Не правильно ввёл количество комнат, нажми ✏️ Редактровать\n'
			'Если хочешь отменить поиск, нажми Отмена',
			reply_markup=kb.edit_cancel)
		bot.register_next_step_handler(message, max_price_handler)

	elif room == '4':
		url_n1 = f'https://ekaterinburg.n1.ru/snyat/dolgosrochno/kvartiry/rooms-chetyrehkomnatnye/{district_n1}?include_suburbs=false&limit=200&sort=-date'
		url_dragee = 'https://arenda.dragee.ru/offer/list/?autoscroll=.b-map-block&period=0&flat_type=0&cities=0&build_year=&sort=actual&novelty=4&rooms=4'
		url_avito = 'https://www.avito.ru/ekaterinburg/kvartiry/sdam/na_dlitelnyy_srok/4-komnatnye-ASgBAQICAkSSA8gQ8AeQUgFAzAgUlFk?cd=1&s=104'
		url_cian = 'https://ekb.cian.ru/cat.php?deal_type=rent&engine_version=2&offer_type=flat&region=4743&room4=1&type=4&with_neighbors=0&sort=creation_date_desc'
		bot.send_message(message.chat.id, 'Ты выбрал четырёхкомнатную квартиру!\n'
			'3) Отправь максимальную цену аренды квартиры в месяц, валюта рубли\n'
			'Не правильно ввёл количество комнат, нажми ✏️ Редактровать\n'
			'Если хочешь отменить поиск, нажми Отмена',
			reply_markup=kb.edit_cancel)
		bot.register_next_step_handler(message, max_price_handler)

	elif room == '12':
		url_n1 = f'https://ekaterinburg.n1.ru/search/{district_n1}?include_suburbs=false&rubric=flats&deal_type=rent_out&rooms=1%2C2&rent_period=month&limit=200&sort=-date'
		url_dragee = 'https://arenda.dragee.ru/offer/list/?autoscroll=.b-map-block&period=0&flat_type=0&cities=0&build_year=&sort=actual&novelty=4&rooms=1&rooms=2'
		url_avito = 'https://www.avito.ru/ekaterinburg/kvartiry/sdam/na_dlitelnyy_srok-ASgBAgICAkSSA8gQ8AeQUg?cd=1&f=ASgBAQICAkSSA8gQ8AeQUgFAzAgkkFmOWQ&s=104'
		url_cian = 'https://ekb.cian.ru/cat.php?deal_type=rent&engine_version=2&offer_type=flat&region=4743&room1=1&room2=1&type=4&with_neighbors=0&sort=creation_date_desc'
		bot.send_message(message.chat.id, 'Ты выбрал однокомнатную и двухкомнатную квартиру!\n'
			'3) Отправь максимальную цену аренды квартиры в месяц, валюта рубли\n'
			'Не правильно ввёл количество комнат, нажми ✏️ Редактровать\n'
			'Если хочешь отменить поиск, нажми Отмена',
			reply_markup=kb.edit_cancel)
		bot.register_next_step_handler(message, max_price_handler)

	elif room == '13':
		url_n1 = f'https://ekaterinburg.n1.ru/search/{district_n1}?include_suburbs=false&rubric=flats&deal_type=rent_out&rooms=1%2C3&rent_period=month&limit=200&sort=-date'
		url_dragee = 'https://arenda.dragee.ru/offer/list/?autoscroll=.b-map-block&period=0&flat_type=0&cities=0&build_year=&sort=actual&novelty=4&rooms=1&rooms=3'
		url_avito = 'https://www.avito.ru/ekaterinburg/kvartiry/sdam/na_dlitelnyy_srok-ASgBAgICAkSSA8gQ8AeQUg?cd=1&f=ASgBAQICAkSSA8gQ8AeQUgFAzAgkklmOWQ&s=104'
		url_cian = 'https://ekb.cian.ru/cat.php?deal_type=rent&engine_version=2&offer_type=flat&region=4743&room1=1&room3=1&type=4&with_neighbors=0&sort=creation_date_desc'
		bot.send_message(message.chat.id, 'Ты выбрал однокомнатную и трёхкомнатную квартиру!\n'
			'3) Отправь максимальную цену аренды квартиры в месяц, валюта рубли\n'
			'Не правильно ввёл количество комнат, нажми ✏️ Редактровать\n'
			'Если хочешь отменить поиск, нажми Отмена',
			reply_markup=kb.edit_cancel)
		bot.register_next_step_handler(message, max_price_handler)

	elif room == '14':
		url_n1 = f'https://ekaterinburg.n1.ru/search/{district_n1}?include_suburbs=false&rubric=flats&deal_type=rent_out&rooms=1%2C4&rent_period=month&limit=200&sort=-date'
		url_dragee = 'https://arenda.dragee.ru/offer/list/?autoscroll=.b-map-block&period=0&flat_type=0&cities=0&build_year=&sort=actual&novelty=4&rooms=1&rooms=4'
		url_avito = 'https://www.avito.ru/ekaterinburg/kvartiry/sdam/na_dlitelnyy_srok-ASgBAgICAkSSA8gQ8AeQUg?cd=1&f=ASgBAQICAkSSA8gQ8AeQUgFAzAgklFmOWQ&s=104'
		url_cian = 'https://ekb.cian.ru/cat.php?deal_type=rent&engine_version=2&offer_type=flat&region=4743&room1=1&room4=1&type=4&with_neighbors=0&sort=creation_date_desc'
		bot.send_message(message.chat.id, 'Ты выбрал однокомнатную и четырёхкомнатную квартиру!\n'
			'3) Отправь максимальную цену аренды квартиры в месяц, валюта рубли\n'
			'Не правильно ввёл количество комнат, нажми ✏️ Редактровать\n'
			'Если хочешь отменить поиск, нажми Отмена',
			reply_markup=kb.edit_cancel)
		bot.register_next_step_handler(message, max_price_handler)

	elif room == '23':
		url_n1 = f'https://ekaterinburg.n1.ru/search/{district_n1}?include_suburbs=false&rubric=flats&deal_type=rent_out&rooms=2%2C3&rent_period=month&limit=200&sort=-date'
		url_dragee = 'https://arenda.dragee.ru/offer/list/?autoscroll=.b-map-block&period=0&flat_type=0&cities=0&build_year=&sort=actual&novelty=4&rooms=2&rooms=3'
		url_avito = 'https://www.avito.ru/ekaterinburg/kvartiry/sdam/na_dlitelnyy_srok-ASgBAgICAkSSA8gQ8AeQUg?cd=1&f=ASgBAQICAkSSA8gQ8AeQUgFAzAgkkFmSWQ&s=104'
		url_cian = 'https://ekb.cian.ru/cat.php?deal_type=rent&engine_version=2&offer_type=flat&region=4743&room2=1&room3=1&type=4&with_neighbors=0&sort=creation_date_desc'
		bot.send_message(message.chat.id, 'Ты выбрал двухкомнатную и трёхкомнатную квартиру!\n'
			'3) Отправь максимальную цену аренды квартиры в месяц, валюта рубли\n'
			'Не правильно ввёл количество комнат, нажми ✏️ Редактровать\n'
			'Если хочешь отменить поиск, нажми Отмена',
			reply_markup=kb.edit_cancel)
		bot.register_next_step_handler(message, max_price_handler)

	elif room == '24':
		url_n1 = f'https://ekaterinburg.n1.ru/search/{district_n1}?include_suburbs=false&rubric=flats&deal_type=rent_out&rooms=2%2C4&rent_period=month&limit=200&sort=-date'
		url_dragee = 'https://arenda.dragee.ru/offer/list/?autoscroll=.b-map-block&period=0&flat_type=0&cities=0&build_year=&sort=actual&novelty=4&rooms=2&rooms=4'
		url_avito = 'https://www.avito.ru/ekaterinburg/kvartiry/sdam/na_dlitelnyy_srok-ASgBAgICAkSSA8gQ8AeQUg?cd=1&f=ASgBAQICAkSSA8gQ8AeQUgFAzAgklFmQWQ&s=104'
		url_cian = 'https://ekb.cian.ru/cat.php?deal_type=rent&engine_version=2&offer_type=flat&region=4743&room2=1&room4=1&type=4&with_neighbors=0&sort=creation_date_desc'
		bot.send_message(message.chat.id, 'Ты выбрал двухкомнатную и четырёхкомнатную квартиру!\n'
			'3) Отправь максимальную цену аренды квартиры в месяц, валюта рубли\n'
			'Не правильно ввёл количество комнат, нажми ✏️ Редактровать\n'
			'Если хочешь отменить поиск, нажми Отмена',
			reply_markup=kb.edit_cancel)
		bot.register_next_step_handler(message, max_price_handler)

	elif room == '34':
		url_n1 = f'https://ekaterinburg.n1.ru/search/{district_n1}?include_suburbs=false&rubric=flats&deal_type=rent_out&rooms=3%2C4&rent_period=month&limit=200&sort=-date'
		url_dragee = 'https://arenda.dragee.ru/offer/list/?autoscroll=.b-map-block&period=0&flat_type=0&cities=0&build_year=&sort=actual&novelty=4&rooms=3&rooms=4'
		url_avito = 'https://www.avito.ru/ekaterinburg/kvartiry/sdam/na_dlitelnyy_srok-ASgBAgICAkSSA8gQ8AeQUg?cd=1&f=ASgBAQICAkSSA8gQ8AeQUgFAzAgkklmUWQ&s=104'
		url_cian = 'https://ekb.cian.ru/cat.php?deal_type=rent&engine_version=2&offer_type=flat&region=4743&room3=1&room4=1&type=4&with_neighbors=0&sort=creation_date_desc'
		bot.send_message(message.chat.id, 'Ты выбрал трёхкомнатную и четырёхкомнатную квартиру!\n'
			'3) Отправь максимальную цену аренды квартиры в месяц, валюта рубли\n'
			'Не правильно ввёл количество комнат, нажми ✏️ Редактровать\n'
			'Если хочешь отменить поиск, нажми Отмена',
			reply_markup=kb.edit_cancel)
		bot.register_next_step_handler(message, max_price_handler)

	elif room == '123':
		url_n1 = f'https://ekaterinburg.n1.ru/search/{district_n1}?include_suburbs=false&rubric=flats&deal_type=rent_out&rooms=1%2C2%2C3&rent_period=month&limit=200&sort=-date'
		url_dragee = 'https://arenda.dragee.ru/offer/list/?autoscroll=.b-map-block&period=0&flat_type=0&cities=0&build_year=&sort=actual&novelty=4&rooms=1&rooms=2&rooms=3'
		url_avito = 'https://www.avito.ru/ekaterinburg/kvartiry/sdam/na_dlitelnyy_srok-ASgBAgICAkSSA8gQ8AeQUg?cd=1&f=ASgBAQICAkSSA8gQ8AeQUgFAzAg0kFmOWZJZ&s=104'
		url_cian = 'https://ekb.cian.ru/cat.php?deal_type=rent&engine_version=2&offer_type=flat&region=4743&room1=1&room2=1&room3=1&type=4&with_neighbors=0&sort=creation_date_desc'
		bot.send_message(message.chat.id, 'Ты выбрал однокомнатную, двухкомнатную и трёхкомнатную квартиру!\n'
			'3) Отправь максимальную цену аренды квартиры в месяц, валюта рубли\n'
			'Не правильно ввёл количество комнат, нажми ✏️ Редактровать\n'
			'Если хочешь отменить поиск, нажми Отмена',
			reply_markup=kb.edit_cancel)
		bot.register_next_step_handler(message, max_price_handler)

	elif room == '134':
		url_n1 = f'https://ekaterinburg.n1.ru/search/{district_n1}?include_suburbs=false&rubric=flats&deal_type=rent_out&rooms=4%2C1%2C3&rent_period=month&limit=200&sort=-date'
		url_dragee = 'https://arenda.dragee.ru/offer/list/?autoscroll=.b-map-block&period=0&flat_type=0&cities=0&build_year=&sort=actual&novelty=4&rooms=1&rooms=3&rooms=4'
		url_avito = 'https://www.avito.ru/ekaterinburg/kvartiry/sdam/na_dlitelnyy_srok-ASgBAgICAkSSA8gQ8AeQUg?cd=1&f=ASgBAQICAkSSA8gQ8AeQUgFAzAg0klmUWY5Z&s=104'
		url_cian = 'https://ekb.cian.ru/cat.php?deal_type=rent&engine_version=2&offer_type=flat&region=4743&room1=1&room3=1&room4=1&type=4&with_neighbors=0&sort=creation_date_desc'
		bot.send_message(message.chat.id, 'Ты выбрал однокомнатную, трёхкомнатную и четырёхкомнатную квартиру!\n'
			'3) Отправь максимальную цену аренды квартиры в месяц, валюта рубли\n'
			'Не правильно ввёл количество комнат, нажми ✏️ Редактровать\n'
			'Если хочешь отменить поиск, нажми Отмена',
			reply_markup=kb.edit_cancel)
		bot.register_next_step_handler(message, max_price_handler)

	elif room == '124':
		url_n1 = f'https://ekaterinburg.n1.ru/search/{district_n1}?include_suburbs=false&rubric=flats&deal_type=rent_out&rooms=4%2C1%2C2&rent_period=month&limit=200&sort=-date'
		url_dragee = 'https://arenda.dragee.ru/offer/list/?autoscroll=.b-map-block&period=0&flat_type=0&cities=0&build_year=&sort=actual&novelty=4&rooms=1&rooms=2&rooms=4'
		url_avito = 'https://www.avito.ru/ekaterinburg/kvartiry/sdam/na_dlitelnyy_srok-ASgBAgICAkSSA8gQ8AeQUg?cd=1&f=ASgBAQICAkSSA8gQ8AeQUgFAzAg0lFmQWY5Z&s=104'
		url_cian = 'https://ekb.cian.ru/cat.php?deal_type=rent&engine_version=2&offer_type=flat&region=4743&room1=1&room2=1&room4=1&type=4&with_neighbors=0&sort=creation_date_desc'
		bot.send_message(message.chat.id, 'Ты выбрал однокомнатную, двухкомнатную и четырёхкомнатную квартиру!\n'
			'3) Отправь максимальную цену аренды квартиры в месяц, валюта рубли\n'
			'Не правильно ввёл количество комнат, нажми ✏️ Редактровать\n'
			'Если хочешь отменить поиск, нажми Отмена',
			reply_markup=kb.edit_cancel)
		bot.register_next_step_handler(message, max_price_handler)

	elif room == '234':
		url_n1 = f'https://ekaterinburg.n1.ru/search/{district_n1}?include_suburbs=false&rubric=flats&deal_type=rent_out&rooms=2%2C3%2C4&rent_period=month&limit=200&sort=-date'
		url_dragee = 'https://arenda.dragee.ru/offer/list/?autoscroll=.b-map-block&period=0&flat_type=0&cities=0&build_year=&sort=actual&novelty=4&rooms=2&rooms=3&rooms=4'
		url_avito = 'https://www.avito.ru/ekaterinburg/kvartiry/sdam/na_dlitelnyy_srok-ASgBAgICAkSSA8gQ8AeQUg?cd=1&f=ASgBAQICAkSSA8gQ8AeQUgFAzAg0kFmSWZRZ&s=104'
		url_cian = 'https://ekb.cian.ru/cat.php?deal_type=rent&engine_version=2&offer_type=flat&region=4743&room2=1&room3=1&room4=1&type=4&with_neighbors=0&sort=creation_date_desc'
		bot.send_message(message.chat.id, 'Ты выбрал двухкомнатную, трёхкомнатную и четырёхкомнатную квартиру!\n'
			'3) Отправь максимальную цену аренды квартиры в месяц, валюта рубли\n'
			'Не правильно ввёл количество комнат, нажми ✏️ Редактровать\n'
			'Если хочешь отменить поиск, нажми Отмена',
			reply_markup=kb.edit_cancel)
		bot.register_next_step_handler(message, max_price_handler)

	elif room == '1234':
		url_n1 = f'https://ekaterinburg.n1.ru/search/{district_n1}?include_suburbs=false&rubric=flats&deal_type=rent_out&rooms=1%2C2%2C3%2C4&rent_period=month&limit=200&sort=-date'
		url_dragee = 'https://arenda.dragee.ru/offer/list/?autoscroll=.b-map-block&period=0&flat_type=0&cities=0&build_year=&sort=actual&novelty=4&rooms=1&rooms=2&rooms=3&rooms=4'
		url_avito = 'https://www.avito.ru/ekaterinburg/kvartiry/sdam/na_dlitelnyy_srok-ASgBAgICAkSSA8gQ8AeQUg?cd=1&f=ASgBAQICAkSSA8gQ8AeQUgFAzAhEjlmQWZJZlFk&s=104'
		url_cian = 'https://ekb.cian.ru/cat.php?deal_type=rent&engine_version=2&offer_type=flat&region=4743&room1=1&room2=1&room3=1&room4=1&type=4&with_neighbors=0&sort=creation_date_desc'
		bot.send_message(message.chat.id, 'Ты выбрал все возможные варианты квартир!\n'
			'3) Отправь максимальную цену аренды квартиры в месяц, валюта рубли\n'
			'Не правильно ввёл количество комнат, нажми ✏️ Редактровать\n'
			'Если хочешь отменить поиск, нажми Отмена',
			reply_markup=kb.edit_cancel)
		bot.register_next_step_handler(message, max_price_handler)

	else:
		bot.send_message(message.chat.id, 'Ты вводишь не правильное количество комнат 🙃\n'
			'Нужно начать сначала, нажми Главное меню',
			reply_markup=kb.main)

def max_price_handler(message):
	global max_price
	max_price = message.text
	if max_price == '❌ Отмена':
		bot.send_message(message.chat.id, 'Ты возвращён в Главное меню, для поиска объявлений по городу Екатеринбург, нажми соответствующую кнопку',
			reply_markup=kb.search)

	elif max_price == '✏️ Редактровать':
		bot.send_message(message.chat.id, 'Вижу, ты решил отредактировать количество комнат\n'
			'2) Пришли мне количество комнат (1-4) снова, если вариантов несколько, то напиши мне их слитно в порядке возрастания\n\n'
			'Пример: "Хочу только однокомнатную квартиру" — 1\n'
			'Пример: "Хочу однокомнатную, двухкомнатную квартиру" — 12\n'
			'Если хочешь отменить поиск, нажми Отмена',
			reply_markup=kb.cancel)
		bot.register_next_step_handler(message, room_handler)

	else:
		bot.send_message(message.chat.id, f'Ты указал максимальную цену — {max_price} руб.\n'
			'4) Отправь минимальную цену аренды квартиры в месяц, валюта рубли\n'
			'Если минимальные рамки тебе не нужны, напиши 0\n'
			'Не правильно ввёл количество комнат, нажми ✏️ Редактровать\n'
			'Если хочешь отменить поиск, нажми Отмена',
			reply_markup=kb.edit_cancel)
		bot.register_next_step_handler(message, min_price_handler)


def min_price_handler(message):
	global min_price
	min_price = message.text
	if min_price == '❌ Отмена':
		bot.send_message(message.chat.id, 'Ты возвращён в Главное меню, для поиска объявлений по городу Екатеринбург, нажми соответствующую кнопку',
			reply_markup=kb.search)

	elif min_price == '✏️ Редактровать':
		bot.send_message(message.chat.id, 'Вижу, ты решил отредактировать максимальную цену!\n'
			'3) Отправь максимальную цену аренды квартиры в месяц снова, валюта рубли\n'
			'Если хочешь отменить поиск, нажми Отмена',
			reply_markup=kb.cancel)
		bot.register_next_step_handler(message, max_price_handler)

	else:
		bot.send_message(message.chat.id, f'Ты указал минимальную цену — {min_price} руб.\n'
			'Не правильно ввёл минимальную цену, нажми ✏️ Редактровать\n'
			'Если хочешь отменить поиск, нажми Отмена\n'
			'Хочешь завершить, нажми Приготовить файл с объявлениями аренды недвижимости',
			reply_markup=kb.done_edit_cancel)
		bot.register_next_step_handler(message, start_file_handler)

def start_file_handler(message):
	global start_file
	start_file = message.text
	if start_file == '❌ Отмена':
		bot.send_message(message.chat.id, 'Ты возвращён в Главное меню, для поиска объявлений по городу Екатеринбург, нажми соответствующую кнопку',
			reply_markup=kb.search)

	elif start_file == '✏️ Редактровать':
		bot.send_message(message.chat.id, 'Вижу, ты решил отредактировать минимальную цену!\n'
			'4) Отправь минимальную цену аренды квартиры в месяц, валюта рубли\n'
			'Если минимальные рамки тебе не нужны, напиши 0\n'
			'Если хочешь отменить поиск, нажми Отмена',
			reply_markup=kb.cancel)
		bot.register_next_step_handler(message, min_price_handler)

	elif start_file == '📝 Приготовить файлы':
		n1_get = f'{url_n1}&price_max={max_price}&price_min={min_price}'
		dragee_get = f'{url_dragee}{district_dragee}&price_to={max_price}&price_from={min_price}'
		avito_get = f'{url_avito}{district_avito}&pmax={max_price}&pmin={min_price}'
		cian_get = f'{url_cian}{district_cian}&maxprice={max_price}&minprice={min_price}'

		bot.send_message(message.chat.id, "Вот ссылки для парсинга:\n"
		f'N1: {n1_get}\n\n'
		f'DRAGEE: {dragee_get}\n\n'
		f'AVITO: {avito_get}\n\n')
		f'CIAN: {cian_get}'
		
		n1_data(n1_get)
		time.sleep(5)

		dragee_data(dragee_get)
		time.sleep(5)

		avito_data(avito_get)
		time.sleep(5)

		cian_data(cian_get)
		time.sleep(5)

		try:
			n1 = open('/Projects/Bot_parser/n1.csv', 'rb')
			bot.send_document(message.chat.id, n1)
			time.sleep(3)
		except Exception:
			bot.send_message(message.chat.id, 'Что то пошло не так с сайтом N1')

		try:
			dragee = open('/Projects/Bot_parser/dragee.csv', 'rb')
			bot.send_document(message.chat.id, dragee)
			time.sleep(5)
		except Exception:
			bot.send_message(message.chat.id, 'Что то пошло не так с сайтом DRAGEE')

		try:
			avito = open('/Projects/Bot_parser/avito.csv', 'rb')
			bot.send_document(message.chat.id, avito)
			time.sleep(3)
		except Exception:
			bot.send_message(message.chat.id, 'Что то пошло не так с сайтом AVITO')

		try:
			cian = open('/Projects/Bot_parser/cian.csv', 'rb')
			bot.send_document(message.chat.id, cian)
			time.sleep(3)
		except:
			bot.send_message(message.chat.id, 'Что то пошло не так с сайтом CIAN')


		bot.send_message(message.chat.id, "Извини, но следующее обращение по техническим причинам возможно, только через 5 минут",
			reply_markup=kb.main_fake)
		time.sleep(300)

		bot.send_message(message.chat.id, "Я снова доступен, переходи в Главное меню",
			reply_markup=kb.main)


if __name__ == '__main__':
	bot.polling(none_stop=True, interval=0)
