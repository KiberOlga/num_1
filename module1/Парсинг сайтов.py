"""import requests
from bs4 import BeautifulSoup
import random
def get_interesting_fact():
    response = requests.get("https://i-fakt.ru/")
    response = response.content
    html = BeautifulSoup(response, "lxml")
    fact = random.choice(html.find_all(class_="p-2 clearfix"))
    print(fact.text)
    print(fact.a.attrs["href"])

def get_festival():
    response = requests.get("https://kudago.com/msk/festival/")
    response = response.content
    html = BeautifulSoup(response, "lxml")
    festival = random.choice(html.find_all(class_="post-title"))
    print(festival.text)
    print(festival.a.atters["href"])"""
import html as html

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
print(festival.text)"""


"""import requests
from bs4 import BeautifulSoup

response = requests.get('http://www.columbia.edu/~fdc/sample.html')
response = response.content
html_1 = BeautifulSoup(response, 'lxml')
contents = html_1.find_all('h3')
for i in range(len(contents)-1):
    contents[i] = contents[i].text
print(contents)"""



"""import requests
from bs4 import BeautifulSoup
response = requests.get('https://webscraper.io/test-sites/e-commerce/ajax/computers/tablets')
response = response.content
html_1 = BeautifulSoup(response, 'lxml')
device = html_1.find("div", class_="row ecomerce-items ecomerce-items-ajax")
print(device["data-items"])"""


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
while user_wish != "не надо мне больше весель€" or user_wish != "стоп":
    user_wish = input("чем бы ты хотел зан€тьс€, мой дорогой? ").lower()
    if user_wish == "погл€деть факты":
        get_interesting_fact()
    elif user_wish == "€ бы сходил на фестиваль":
        get_festival()
    elif user_wish == "€ бы послушал какой-нибудь концерт":
        get_concert()
    else:
        print("“ы куда собралс€? такого нет:( давай-ка по сценарию")"""



user_choice = input("Ќапишите жанр игры: ")
action = "Team Fortress 2"
adventure = "Stray"
role = "Path of Exile"
simulator = "Potion Craft: Alchemist Simulator"
strategy = "RimWorld"
sports_and_racing = "BLACKTAIL"
if user_choice == "Action":
    print(action)
elif user_choice == "Adventure":
    print(adventure)
elif user_choice == "Role":
    print(role)
elif user_choice == "Simulator":
    print(simulator)
elif user_choice == "Strategy":
    print(strategy)
elif user_choice == "Sports and racing":
    print(sports_and_racing)
