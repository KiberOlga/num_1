# -*- coding: cp1251 -*-
"""import telebot
import requests
from bs4 import BeautifulSoup
import random
token = "5939655875:AAE60eB1Zl_RyoacUAE2IOVY6ueFUAWi1VM"
bot = telebot.TeleBot(token)

@bot.message_handler(commands=["start"])
def send_welcome(message):
    welcome_text = """Привет! Я знаю много интересных фактов и стихотворений, а также мы можем посмотреть на котиков и сходить на фестиваль"""
    bot.send_message(message.chat.id, welcome_text)

@bot.message_handler(commands=["fact"])
def send_fact(massege):
    response = requests.get("https://i-fakt.ru").content
    html = BeautifulSoup(response, 'lxml')
    fact = random.choice(html.find_all(class_='p-2 clearfix'))
    fact_link = fact.a.attrs["href"]
    bot.send_message(massege.chat.id, fact.text)
    bot.send_message(massege.chat.id, fact_link)

@bot.message_handler(commands=["cat"])
def send_cat(message):
    cat_number = random.randint(1, 3)
    cat_pic = open("img/" + cat_number + ".jpg", "rb")
    bot.send_message(message.chat.id, cat_pic)
bot.polling()"""



import telebot
import requests
from bs4 import BeautifulSoup
import random

token = 'ваш токен'

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    welcome_text = """
    Привет! Я знаю много интересных фактов и стихотворений, а также мы можем посомтреть на котиков и сходить на фестиваль
    """
    bot.send_message(message.chat.id, welcome_text)


@bot.message_handler(commands=['fact'])
def send_fact(message):
    response = requests.get('https://i-fakt.ru/').content
    html = BeautifulSoup(response, 'lxml')
    fact = random.choice(html.find_all(class_='p-2 clearfix'))
    fact_link = fact.a.attrs['href']
    bot.send_message(message.chat.id, fact.text)
    bot.send_message(message.chat.id, fact_link)


@bot.message_handler(commands=['cat'])
def send_cat(message):
    cat_number = str(random.randint(1, 9))
    cat_pic = open('img/' + cat_number + '.jpg', 'rb')
    bot.send_photo(message.chat.id, cat_pic)


bot.polling()
