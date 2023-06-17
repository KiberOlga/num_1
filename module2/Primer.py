# -*- coding: cp1251 -*-
from datetime import datetime
import pyaudio
import speech_recognition as sr
import pyttsx3
import os
import webbrowser
import random
from threading import Thread
from tkinter import *
from PIL import Image, ImageTk

r = sr.Recognizer()
voice = pyttsx3.init()
voice.say('Привет, меня зовут Квант, я твой голосовой ассистент.')
print('Привет, меня зовут Квант, я твой голосовой ассистент.')
voice.runAndWait()

def window_application():
    window = Tk()
    window["bg"] = "#FFE4B5"

    window.title("Квант")

    window.geometry("800x600+100+50")

    """photo = PhotoImage(file="Kvant.gif")
    picture = Label(window, image=photo)
    picture.place(x=10, y=10)"""

    window.mainloop()



def programming():
    while True:
        with sr.Microphone() as source:
            print('Слушаю...')
            audio = r.listen(source)
        try:
            speech = r.recognize_google(audio, language='ru_RU').lower()
            print('Вы сказали -  ', speech)

        except:
            voice.say('ничего не слышу')
            voice.runAndWait()
            break

        if speech.find('привет') >= 0 or speech.find('добрый день') >= 0:
            greeting = ["Привет!", "Добрый день!", "Hello!", "Hi!", "Good afternoon!"]
            gr = random.choice(greeting)
            voice.say(gr + "рад тебя слышать")
            voice.runAndWait()
            a = Label(window, text=gr, font="Arial, 20", fg="black", bg="#FFFF00")
            a.place(x=200, y=170)

        elif speech.find('youtube') >= 0 or speech.find('ютуб') >= 0:
            webbrowser.open_new('https://www.youtube.com/')
            voice.say('Я открыл ютуб')
            voice.runAndWait()

        elif speech.find('пока') >= 0 or speech.find('бай') >= 0:
            voice.say('Пока! До скорой встречи!')
            voice.runAndWait()
            break



thread1 = Thread(target=window_application, args=())
thread2 = Thread(target=programming, args=())

thread1.start()
thread2.start()
thread1.join()
thread2.join()