# -*- coding: cp1251 -*-
"""from tkinter import *

window = Tk()

window.title("окно")
window.geometry("1000x1000")
count = 0

def Klikeker():
    global count
    count += 1
    lab['text'] = count

lab = Label(window, text="Арбуз", font=("18"), fg="#FFFFFF", bg="#C72974")
lab.place(x=400, y=200)

button = Button(text="Button", font=("36"), fg="#FFFFFF", bg="#C72974", command=Klikeker)
button.place(x=400, y=400)
window.mainloop()"""





"""from tkinter import *
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import warnings
warnings.filterwarnings("ignore")

window = Tk()

window.title("сайт ЦБ 2.0")
window.geometry("1000x1000+150+50")

url = "http://www.cbr.ru/scripts/XML_daily.asp?"

today = datetime.today()
today = today.strftime("%d/%m/%y")

payload = {"date_req=": today}

responce = requests.get(url, params=payload)

xml = BeautifulSoup(responce.content, "lxml")

def getCourse(id):
    return xml.find("valute", {"id": id}).value.text

photo = PhotoImage(file="logo.png")
picture = Label(window, image=photo)
picture.place(x=10, y=10)

lab = Label(window, text="Курс валют на сегодня", fg="#FFFFFF", bg="#C72974", font="Arial, 40")
lab.place(x=200, y=30)

date_info = Label(window, text="Курс на " + today.replace("/", "."), font="Arial, 30")
date_info.place(x=200, y=100)

eur = Label(window, text="€" + getCourse("R01239"), font="Arial, 20")
eur.place(x=200, y=170)

usd = Label(window, text="$" + getCourse("R01235"), font="Arial, 20")
usd.place(x=200, y=210)
window.mainloop()"""






"""from tkinter import *
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import warnings
warnings.filterwarnings("ignore")

window = Tk()

window.title("сайт ЦБ 2.0")
window.geometry("1000x1000+150+50")

url = "http://www.cbr.ru/scripts/XML_daily.asp?"

today = datetime.today()
today = today.strftime("%d/%m/%y")

payload = {"date_req=": today}

responce = requests.get(url, params=payload)

xml = BeautifulSoup(responce.content, "lxml")

def getCourse(id):
    return xml.find("valute", {"id": id}).value.text

photo = PhotoImage(file="logo.png")
picture = Label(window, image=photo)
picture.place(x=10, y=10)

lab = Label(window, text="Курс валют на сегодня", fg="#FFFFFF", bg="#C72974", font="Arial, 40")
lab.place(x=200, y=30)

date_info = Label(window, text="Курс на " + today.replace("/", "."), font="Arial, 30")
date_info.place(x=200, y=100)

eur = Label(window, text="€" + getCourse("R01239"), font="Arial, 20")
eur.place(x=200, y=170)

usd = Label(window, text="$" + getCourse("R01235"), font="Arial, 20")
usd.place(x=200, y=210)

cny = Label(window, text="Юань:" + getCourse("R01375"), font="Arial, 20")
cny.place(x=200, y=250)
window.mainloop()"""








from tkinter import *
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import warnings
warnings.filterwarnings("ignore")

window = Tk()
window["bg"] = "#FFE4B5"

window.title("сайт ЦБ 2.0")
window.geometry("1000x1000+150+50")
window.resizable(width=False, height=False)

url = "http://www.cbr.ru/scripts/XML_daily.asp?"

today = datetime.today()
today = today.strftime("%d/%m/%y")

payload = {"date_req=": today}

responce = requests.get(url, params=payload)

xml = BeautifulSoup(responce.content, "lxml")

def getCourse(id):
    return xml.find("valute", {"id": id}).value.text

photo = PhotoImage(file="logo.png")
picture = Label(window, image=photo, bg="#FFE4B5")
picture.place(x=10, y=10)

lab = Label(window, text="Курс валют на сегодня", fg="#FFFFFF", bg="#C72974", font="Arial, 40")
lab.place(x=200, y=30)

date_info = Label(window, text="Курс на " + today.replace("/", "."), font="Arial, 30", bg="#FFE4B5")
date_info.place(x=200, y=100)

eur = Label(window, text="€" + getCourse("R01239"), font="Arial, 20", fg="#006400", bg="#FFFF00")
eur.place(x=200, y=170)

usd = Label(window, text="$" + getCourse("R01235"), font="Arial, 20", fg="#00FFFF", bg="#191970")
usd.place(x=200, y=210)

cny = Label(window, text="Юань:" + getCourse("R01375"), font="Arial, 20", fg="#FFC0CB", bg="#FF1493")
cny.place(x=200, y=250)
window.mainloop()