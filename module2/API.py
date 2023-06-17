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
    return xml.find("valute", {"id": id}).value.text

my_file = open("file.txt", "w", encoding="utf-8")
my_file.write(Course("R01035") + " рублей за 1 фунт стерлингов\n")
my_file.write(Course("R01035") + " рублей за 1 фунт стерлингов\n")
my_file.write(Course("R01335") + " рублей за 1 казахский тенге\n")
my_file.close()"""

"""print(Course("R01035"), "рублей за 1 фунт стерлингов")
print(Course("R01090B"), "рублей за 1 белорусский рубль")
print(Course("R01335"), "рублей за 1 казахский тенге")"""






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
    return xml.find("valute", {"id": id}).value.text

my_file = open("file.txt", "w", encoding="utf-8")
my_file.write(Course("R01035") + " рублей за 1 фунт стерлингов\n")
my_file.write(Course("R01090B") + " рублей за 1 белорусский рубль\n")
my_file.write(Course("R01335") + " рублей за 1 казахский тенге\n")
my_file.write(Course("R01115") + " рублей за 1 бразильский реал\n")
my_file.write(Course("R01210") + " рублей за 1 грузинский лари\n")
my_file.write(Course("R01230") + " рублей за 1 дирхам ОАЭ\n")
my_file.write(Course("R01355") + " рублей за 1 катарский риал\n")
my_file.close()"""






import requests
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
    return xml.find("valute", {"id": id}).value.text

valute_from = "EUR"
valute_to = "USD"
amount = int(input("Введите сумму, которую хотите конвертировать: "))

def course(valute_from, valute_to, amount):
    rates = {
        "RUR": 1.0,
        "USD": Course("R01235"),
        "EUR": Course("R01239")
    }

    if valute_from == "RUR":
        return amount / float(rates[valute_to].replace(',', '.'))
    else:
        return amount * float(rates[valute_from].replace(',', '.')) / float(rates[valute_to].replace(',', '.'))

print("Сумма составляет: ", course(valute_from, valute_to, amount))