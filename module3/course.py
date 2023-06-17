# -*- coding: cp1251 -*-
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

"""my_file = open("file.txt", "w", encoding="utf-8")
my_file.write(Course("R01035") + " ������ �� 1 ���� ����������\n")
my_file.write(Course("R01035") + " ������ �� 1 ���� ����������\n")
my_file.write(Course("R01335") + " ������ �� 1 ��������� �����\n")
my_file.close()"""