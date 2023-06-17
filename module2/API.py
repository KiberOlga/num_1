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
my_file.write(Course("R01035") + " ������ �� 1 ���� ����������\n")
my_file.write(Course("R01035") + " ������ �� 1 ���� ����������\n")
my_file.write(Course("R01335") + " ������ �� 1 ��������� �����\n")
my_file.close()"""

"""print(Course("R01035"), "������ �� 1 ���� ����������")
print(Course("R01090B"), "������ �� 1 ����������� �����")
print(Course("R01335"), "������ �� 1 ��������� �����")"""






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
my_file.write(Course("R01035") + " ������ �� 1 ���� ����������\n")
my_file.write(Course("R01090B") + " ������ �� 1 ����������� �����\n")
my_file.write(Course("R01335") + " ������ �� 1 ��������� �����\n")
my_file.write(Course("R01115") + " ������ �� 1 ����������� ����\n")
my_file.write(Course("R01210") + " ������ �� 1 ���������� ����\n")
my_file.write(Course("R01230") + " ������ �� 1 ������ ���\n")
my_file.write(Course("R01355") + " ������ �� 1 ��������� ����\n")
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
amount = int(input("������� �����, ������� ������ ��������������: "))

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

print("����� ����������: ", course(valute_from, valute_to, amount))