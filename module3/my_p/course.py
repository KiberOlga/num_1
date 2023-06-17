# -*- coding: cp1251 -*-
"""import requests
from bs4 import BeautifulSoup
from datetime import datetime
import warnings
warnings.filterwarnings("ignore")

url = "http://www.cbr.ru/scripts/XML_daily.asp?"

today = datetime.today()
today = today.strftime("%d/%m/%y")

date = {"date_req=": today}

responce = requests.get(url, params=date)

xml = BeautifulSoup(responce.content, "lxml")

def Course(id):
    return xml.find("valute", {"id": id}).value.text"""


"""my_file = open("file.txt", "w", encoding="utf-8")
my_file.write(Course("R01035") + " рублей за 1 фунт стерлингов\n")
my_file.write(Course("R01035") + " рублей за 1 фунт стерлингов\n")
my_file.write(Course("R01335") + " рублей за 1 казахский тенге\n")
my_file.close()"""




"""import requests
from bs4 import BeautifulSoup

def get_currency_rate(currency):
    url = 'https://www.banki.ru/products/currency/'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    currency_table = soup.find('table', {'class': 'currency-table__table'})
    rows = currency_table.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        cols = [col.text.strip() for col in cols]
        if cols and cols[1] == currency:
            return cols[3]

currency_command = input('Введите команду для получения курса валюты: ')
if currency_command.startswith('-к '):
    currency = currency_command[3:]
    currency = get_currency_rate(currency)
    if currency:
        print(f'Курс {currency} на сегодня: {currency}')
    else:
        print(f'Курс {currency} не найден')
else:
    print('Неверный формат команды')"""






import requests
from bs4 import BeautifulSoup
from datetime import datetime
import warnings

warnings.filterwarnings("ignore")

url = "http://www.cbr.ru/scripts/XML_daily.asp?"

today = datetime.today()
today = today.strftime("%d/%m/%Y")

date = {"date_req=": today}

responce = requests.get(url, params=date)

xml = BeautifulSoup(responce.content, "lxml")

def Course(chr):
    return xml.find('charcode', text=chr).parent.value.text
#print(Course("AUD"))