# -*- coding: cp1251 -*-
import time
#my_list = [time.sleep(x) for x in range(1, 3)]
"""my_list = (time.sleep(x) for x in range(1, 3))

for element in my_list:
    print(element)
print(my_list)"""

"""my_range = list(range(1, 6))
#print(my_range)

def my_laze_func(my_list):
    yield from my_list
my_list = ["кот", "утка", "слон"]

for i in my_laze_func(my_list):
    print(i)"""


"""file = open("test.txt", "w")
file.write("Hello")
file.close()
"""
"""with open("test.txt", "w") as file:
    file.write("Bye")
    print(file.closed)
print(file.closed)"""





"""import contextlib

@contextlib.contextmanager

def exc_handler(exc):
    try:
        yield True
    except exc:
        print("Что-то не работает")

with exc_handler(IndexError):
    my_l = [5, 7]
    print(my_l[4])"""

"""def str_reverse(my_str):
    print("Мы вошли в контекстный менеджер")
    yield my_str[::-1]
    print("Мы вышли из контекстного менеджера")

with str_reverse("Hello, mom") as reversed_str:
    print(f"Развёрнутая строка {reversed_str}")"""





"""def func_with_args_and_kwargs(*args, **kwargs):
    print(f"Арги:{args}\nКварги:{kwargs}")
func_with_args_and_kwargs(3, 4, 5, a=7, b=3, c=7, d=8)"""








#Домашняя работа

# 1 способ
numbers = list(range(1, 1000000))
def my_laze_func(numbers):
    yield from numbers

for i in my_laze_func(numbers):
    square = i * i
    print(square)

# 2 способ
def squares(length):
    for i in range(length):
        yield i ** 2

for square in squares(1000000):
    print(square)




"""import requests
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

currency = input('Введите код валюты: ')
def get_course(currency):
    return xml.find("valute", {'id': currency}).value.text

with get_course(currency) as currency:
    print(currency)"""





"""import requests
#import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
from contextlib import contextmanager
from datetime import datetime
import warnings

warnings.filterwarnings("ignore")

url = "http://www.cbr.ru/scripts/XML_daily.asp"

list = ['USD', 'EUR', 'GBP', 'JPY', 'CHF', 'CNY']

@contextmanager

def get_course_info(c_id):
    today = datetime.today()
    today = today.strftime("%d/%m/%Y")

    date = {"date_req=": today}

    responce = requests.get(url, params=date)

    xml = BeautifulSoup(responce.content, "lxml")
    valute = xml.find(f"./Valute[CharCode='{c_id}']")
    if valute:
        currency = float(valute.find('Value').text.replace(",", "."))
        yield f"(1 шт.) {valute.find('Name').text} стоит(ят) {currency:.4f} руб."
    else:
        yield f"Ошибка: валюта {c_id} не найдена"

c_id = input("Введите код валюты: ")

if c_id not in list:
    print("Неверный код валюты")
else:
    with get_course_info(c_id) as currency:
        print(currency)"""




"""import requests
from datetime import datetime
from contextlib import contextmanager
import xml.etree.ElementTree as ET

url = "http://www.cbr.ru/scripts/XML_daily.asp?"

list = ["AUD", "AZN", "GBP", "AMD", "BYN", "BGN", "BRL", "HUF", "VND", "HKD", "GEL", "DKK", "AED", 'USD', 'EUR', "EGP",
        "INR", "KZT", "CAD", "QAR", "KGS", "CNY", "TRY", "TMT", "ZAR", "KRW", "JPY"]

@contextmanager

def get_course_info(c_id):
    today = datetime.today()
    today = today.strftime("%d/%m/%Y")

    date = {"date_req=": today}
    responce = requests.get(url, params=date)

    xml = ET.fromstring(responce.content)
    val = xml.find(f"./Valute[CharCode='{c_id}']")

    if val:
        currency = float(val.find('Value').text.replace(",", "."))
        yield f"(1 шт.) {val.find('Name').text} стоит(ят) {currency:.2f} руб."
    else:
        yield f"Ошибка. Валюта {c_id} не найдена"

c_id = input("Введите код валюты: ")

if c_id not in list:
    print("Неверный код валюты")
else:
    with get_course_info(c_id) as currency:
        print(currency)"""





