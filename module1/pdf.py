# -*- coding: cp1251 -*-
"""import requests
from bs4 import BeautifulSoup
import random

def get_interesting_fact():
    response = requests.get('https://i-fakt.ru/')
    response = response.content
    html = BeautifulSoup(response, 'lxml')
    fact = random.choice(html.find_all(class_='p-2 clearfix'))
    print(fact.text)
    print(fact.a.attrs['href'])

def get_festival():
    response = requests.get('https://kudago.com/msk/festival/')
    response = response.content
    html = BeautifulSoup(response, 'lxml')
    festival = random.choice(html.find_all(class_='post-title'))
    print(festival.text)
    print(festival.a.attrs['href'])

def get_concert():
    response = requests.get('https://kudago.com/msk/concerts/')
    response = response.content
    html = BeautifulSoup(response, 'lxml')
    concert = random.choice(html.find_all(class_='post-title'))
    print(concert.text)
    print(concert.a.attrs['href'])

user_wish = ""
while user_wish != "�� ���� ��� ������ �������" or user_wish != "����":
    user_wish = input("��� �� �� ����� ��������, ��� �������? ").lower()
    if user_wish == "��������� �����":
        get_interesting_fact()
    elif user_wish == "� �� ������ �� ���������":
        get_festival()
    elif user_wish == "� �� �������� �����-������ �������":
        get_concert()
    else:
        print("�� ���� ��������? ������ ���:( �����-�� �� ��������")"""



"""from fpdf import FPDF
pdf = FPDF("P", "cm", (10, 15))
pdf.add_page()
pdf.add_font("Montserrat-Thin", "", "C:\WINDOWS\FONT\COUR.ttf")
pdf.set_text_color(0, 255, 0)
pdf.set_fill_color(155, 50, 168)
pdf.set_draw_color(0, 0, 255)

pdf.set_font("Montserrat-Thin", size=16)
pdf.cell(7, 5, txt="Python is nice", align="C", border=1, fill=True)

pdf.output("first_pdf.pdf")"""




"""from fpdf import FPDF

pdf = FPDF('P', 'cm', (10, 15))
pdf.add_page()

pdf.add_font('courier', '', 'C:\WINDOWS\FONTS\COUR.ttf', uni=True)

pdf.set_text_color(0, 255, 0)
pdf.set_fill_color(155, 50, 168)
pdf.set_draw_color(0, 0, 255)

pdf.set_font('courier', size=16)
pdf.cell(7, 5, txt='����� ������!', align='C', border=1, fill=True)
pdf.image('img_1.png', h=0, w=10, x=0, y=5)

pdf.output('first_pdf.pdf')"""



"""password = int(input("������� ������: "))
while password != 235:
    password = int(input("������ ��������. ������� ��� ��� ���: "))
print("�� �����. ����� ����������!")"""


"""password = int(input('������� ������: '))
while password != 235:
    print('������ �� �����! ')
    password = int(input('������� ������ ��� ���: '))
print('������ ������! ����� ����������.')"""

"""import requests
from bs4 import BeautifulSoup
response = requests.get('https://webscraper.io/test-sites/e-commerce/ajax/computers/tablets')
response = response.content
html_1 = BeautifulSoup(response, 'lxml')
device = html_1.find("div", class_="row ecomerce-items ecomerce-items-ajax")
print(device["data-items"])"""


"""import xlrd, xlwt
rb = xlrd.open_workbook('../ArticleScripts/ExcelPython/xl.xls',formatting_info=True)
sheet = rb.sheet_by_index(0)
val = sheet.row_values(0)[0]
vals = [sheet.row_values(rownum) for rownum in range(sheet.nrows)]
wb = xlwt.Workbook()
ws = wb.add_sheet('Test')
ws.write(0, 0, val[0])
i = 0
for rec in vals:
    ws.write(i,1,rec[0])
    i =+ i
wb.save('../ArticleScripts/ExcelPython/xl_rec.xls')"""


import requests
from bs4 import BeautifulSoup
import random

def get_interesting_fact():
    response = requests.get('https://store.steampowered.com/search/?supportedlang=russian&tags=699&ndl=1')
    response = response.content
    html = BeautifulSoup(response, 'lxml')
    fact = random.choice(html.find_all(class_='tab_item_name'))
    print(fact.text)
    print(fact.a.attrs['href'])

def get_festival():
    response = requests.get('https://store.steampowered.com/search/?supportedlang=russian&tags=699&ndl=1')
    response = response.content
    html = BeautifulSoup(response, 'lxml')
    festival = random.choice(html.find_all(class_='post-title'))
    print(festival.text)
    print(festival.a.attrs['href'])

def get_concert():
    response = requests.get('https://store.steampowered.com/search/?supportedlang=russian&tags=699&ndl=1')
    response = response.content
    html = BeautifulSoup(response, 'lxml')
    concert = random.choice(html.find_all(class_='post-title'))
    print(concert.text)
    print(concert.a.attrs['href'])

user_wish = ""
while user_wish != "�� ���� ��� ������ �������" or user_wish != "����":
    user_wish = input("��� �� �� ����� ��������, ��� �������? ").lower()
    if user_wish == "��������� �����":
        get_interesting_fact()
    elif user_wish == "� �� ������ �� ���������":
        get_festival()
    elif user_wish == "� �� �������� �����-������ �������":
        get_concert()
    else:
        print("�� ���� ��������? ������ ���:( �����-�� �� ��������")
