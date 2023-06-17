# -*- coding: cp1251 -*-
"""start - �����
help - ������
poem - �������������
fact - ����
cat - �����
music - ������
sticker - ������
game - ����"""

"""import telebot
import requests
import random
from bs4 import BeautifulSoup

token = "5939655875:AAE60eB1Zl_RyoacUAE2IOVY6ueFUAWi1VM"
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    welcome_text = "������! � ���� ������������ �����, ���� ����� ���������� ������ � ���� �������� ����� �������!"
    bot.send_message(message.chat.id,  welcome_text)

@bot.message_handler(commands=['poem'])
def send_poem(message):
    poem_text = "���� ���� �� �������, ��� � ��� �������������..."
    bot.send_message(message.chat.id, poem_text)
    keyboard = telebot.types.InlineKeyboardMarkup(row_width=1)
    button_url = telebot.types.InlineKeyboardButton("������� ��������...", url="https://rustih.ru/")
    keyboard.add(button_url)
    bot.send_message(message.chat.id, "����� � ���������", reply_markup=keyboard)


@bot.message_handler(commands=["fact"])
def send_fact(message):
    response = requests.get("https://i-fakt.ru").content
    html = BeautifulSoup(response, 'lxml')
    fact = random.choice(html.find_all(class_='p-2 clearfix'))
    fact_link = fact.a.attrs["href"]
    bot.send_message(message.chat.id, fact.text)
    bot.send_message(message.chat.id, fact_link)

@bot.message_handler(commands=['cat'])
def send_cat(message):
    cat_number = str(random.randint(1, 2))
    cat_img = open('img/' + cat_number + '.jpg', 'rb')
    bot.send_photo(message.chat.id, cat_img)

@bot.message_handler(commands=["music"])
def send_music(message):
    song = open("Blestyashhie_-_Novogodnyaya_pesnya_52465315.mp3", "rb")
    bot.send_audio(message.chat.id, song)

@bot.message_handler(commands=["sticker"])
def send_sticker(message):
    bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAEHD9djrdO_3pYBnL2NKzxTWewJTaLF_gACbwADmL-ADeFz2TIaBadILAQ")

bot.polling()"""




"""import telebot
import requests
import random
from bs4 import BeautifulSoup

token = "5939655875:AAE60eB1Zl_RyoacUAE2IOVY6ueFUAWi1VM"
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    welcome_text = "������, {0.first_name}! � ���� ������������ �����, ���� ����� ���������� ������ � ���� �������� ����� �������!".format(message.from_user)
    bot.send_message(message.chat.id,  welcome_text)

@bot.message_handler(commands=['poem'])
def send_poem(message):
    poem_text = "���� ���� �� �������, ��� � ��� �������������..."
    bot.send_message(message.chat.id, poem_text)
    keyboard = telebot.types.InlineKeyboardMarkup(row_width=1)
    button_url = telebot.types.InlineKeyboardButton("������� ��������...", url="https://rustih.ru/")
    keyboard.add(button_url)
    bot.send_message(message.chat.id, "����� � ���������", reply_markup=keyboard)


@bot.message_handler(commands=["fact"])
def send_fact(message):
    response = requests.get("https://i-fakt.ru").content
    html = BeautifulSoup(response, 'lxml')
    fact = random.choice(html.find_all(class_='p-2 clearfix'))
    fact_link = fact.a.attrs["href"]
    bot.send_message(message.chat.id, fact.text)
    bot.send_message(message.chat.id, fact_link)

@bot.message_handler(commands=['cat'])
def send_cat(message):
    cat_number = str(random.randint(1, 4))
    cat_img = open('img/' + cat_number + '.jpg', 'rb')
    bot.send_photo(message.chat.id, cat_img)

@bot.message_handler(commands=["music"])
def send_music(message):
    song = open("Blestyashhie_-_Novogodnyaya_pesnya_52465315.mp3", "rb")
    bot.send_audio(message.chat.id, song)

@bot.message_handler(commands=["sticker"])
def send_sticker(message):
    bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAEHD9djrdO_3pYBnL2NKzxTWewJTaLF_gACbwADmL-ADeFz2TIaBadILAQ")

@bot.message_handler(commands=["game"])
def send_game(message):
    games = ["Goose Goose Duck", "Rust", "Raft", "DayZ", "Stray"]
    game = random.choice(games)
    game_1 = "C������ ���� �������� � ���� " + game
    bot.send_message(message.chat.id, game_1)

bot.polling()"""





import telebot
import requests
import random
from bs4 import BeautifulSoup

token = "5939655875:AAE60eB1Zl_RyoacUAE2IOVY6ueFUAWi1VM"
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    welcome_text = "������, {0.first_name}! � ���� ������������ �����, ���� ����� ���������� ������ � ���� �������� ����� �������!".format(message.from_user)
    bot.send_message(message.chat.id,  welcome_text)

@bot.message_handler(commands=['poem'])
def send_poem(message):
    poem_text = "���� ���� �� �������, ��� � ��� �������������..."
    bot.send_message(message.chat.id, poem_text)
    keyboard = telebot.types.InlineKeyboardMarkup(row_width=1)
    button_url = telebot.types.InlineKeyboardButton("������� ��������...", url="https://rustih.ru/")
    keyboard.add(button_url)
    bot.send_message(message.chat.id, "����� � ���������", reply_markup=keyboard)


@bot.message_handler(commands=["fact"])
def send_fact(message):
    response = requests.get("https://i-fakt.ru").content
    html = BeautifulSoup(response, 'lxml')
    fact = random.choice(html.find_all(class_='p-2 clearfix'))
    fact_link = fact.a.attrs["href"]
    bot.send_message(message.chat.id, fact.text)
    bot.send_message(message.chat.id, fact_link)

@bot.message_handler(commands=['cat'])
def send_cat(message):
    cat_number = str(random.randint(1, 2))
    cat_img = open('img/' + cat_number + '.jpg', 'rb')
    bot.send_photo(message.chat.id, cat_img)

@bot.message_handler(commands=["music"])
def send_music(message):
    song = open("������ ���������� ������ - jingle bells.mp3", "rb")
    bot.send_audio(message.chat.id, song)

@bot.message_handler(commands=["sticker"])
def send_sticker(message):
    bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAEHD9djrdO_3pYBnL2NKzxTWewJTaLF_gACbwADmL-ADeFz2TIaBadILAQ")

@bot.message_handler(commands=["game"])
def send_game(message):
    button = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_1 = telebot.types.KeyboardButton("action")
    button_2 = telebot.types.KeyboardButton("adventure")
    button_3 = telebot.types.KeyboardButton("role")
    button_4 = telebot.types.KeyboardButton("simulator")
    button_5 = telebot.types.KeyboardButton("strategy")
    button_6 = telebot.types.KeyboardButton("sports_and_racing")
    button.add(button_1, button_2, button_3, button_4, button_5, button_6)
    bot.send_message(message.chat.id, text="� ���� ������ ����� �� ������ �� ��������?", reply_markup=button)

@bot.message_handler(content_types=["text"])
def func(message):
    if(message.text == "action"):
        bot.send_message(message.chat.id, text="������� ���� �������� � ���� Team Fortress 2")
    if (message.text == "adventure"):
        bot.send_message(message.chat.id, text="������� ���� �������� � ���� Stray")
    if (message.text == "role"):
        bot.send_message(message.chat.id, text="������� ���� �������� � ���� Path of Exile")
    if (message.text == "simulator"):
        bot.send_message(message.chat.id, text="������� ���� �������� � ���� Potion Craft: Alchemist Simulator")
    if (message.text == "strategy"):
        bot.send_message(message.chat.id, text="������� ���� �������� � ���� RimWorld")
    if (message.text == "sports_and_racing"):
        bot.send_message(message.chat.id, text="������� ���� �������� � ���� BLACKTAIL")

bot.polling()