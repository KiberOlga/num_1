
# -*- coding: cp1251 -*-
"""from tkinter import *

window = Tk()
window.geometry("700*500")
window.title("Тест по играм")

label_titel = Label(text="Супер мега крутой тест по играм", font=("Arial, 24"), fg="white", bg="red")
label_titel.place(width=700, height=50, x=0, y=0)
facts = [
    {"text": "CS 1.6 вышла в 2013", "right": 0},
    {"text": "Самая последняя часть Ассасина - Valhala", "right": 1},
    {"text": "Дона из частей дума enternal признана самой лёгкой", "right": 0},
    {"text": "Доту стоит скачивать", "right": 0},
    {"text": "Героиню игры The Walking Dead зовут Clementine", "right": 1}
]
number = 0
points = 0

def chek():
    global number, points
    answer = var.get()
    if bool(answer) == facts[number]["right"]:
        points += 1
    if number < len(facts) - 1:
        number += 1
        fact["text"] = facts[number]["text"]
    else:
        points_label = Label(text="Вы выбрали" + str(points) + "очка", font=("Arial",34))
        points_label.place(x=0, y=0, width=70, height=250)


fact = Message(text=facts[nuMesmber]["text"], font=("Arial", 14), width=680, borderwidth=0)
fact.configure(justify=CENTER)
fact.place(x=10, y=70)

var = IntVar()
true = Radiobutton(text="Правда", variable=var, value=0)
true.place(x=10, y=120)

false = Radiobutton(text="Ложь", variable=var, value=0)
false.place(x=10, y=170)

b = Button(text="Ответить", font=("Arial", 24), fg="black", command=check)

window.mainloop()"""











"""from tkinter import *

window = Tk()
window.geometry('700x500')
window.title('Тест по играм')

photo = PhotoImage(file="3.jpg")
label = Label(image=photo)
label.place(x=3, y=0)

label_title = Label(text='Супер мега крутой тест по играм', font=('Arial', 24), fg='white', bg='red')
label_title.place(width=700, height=50, x=0, y=0)

facts = [
    {'text': 'CS 1.6 вышла в 2013', 'right': 0},
    {'text': 'Самая последня часть Ассасина - Valhala?', 'right': 1},
    {'text': 'Одна из частей дума enternal признана саомй лёгкой', 'right': 0},
    {'text': 'Доту стоит скачивать', 'right': 0},
    {'text': 'героиню игры The Walking Dead зовут Clementine', 'right': 1},
]
number = 0
points = 0


def check():
    global number, points
    answer = var.get()
    if bool(answer) == facts[number]['right']:
        points += 1
    if number < len(facts) - 1:
        number += 1
        fact['text'] = facts[number]['text']
    else:
        points_label = Label(text='Вы набрали ' + str(points) + ' очка', font=('Arial', 34), fg='red', bd='white')
        points_label.place(x=0, y=9, width=70, height=250)


fact = Message(text=facts[number]['text'], font=('Arial', 14), width=680, borderwidth=0)
fact.configure(justify=CENTER)
fact.place(x=10, y=70)

var = IntVar()

true = Radiobutton(text='Правда', variable=var, value=1)
true.place(x=10, y=120)

false = Radiobutton(text='Ложь', variable=var, value=0)
false.place(x=10, y=170)

b = Button(text='Ответить', font=('Arial', 24), fg='black', command=check)
b.place(x=200, y=130)

pic_happy = PhotoImage(file="img_1.png")
label_happy = Label(image=pic_happy)
label_happy.place(x=0, y=200)

window.mainloop()"""


# -*- coding: cp1251 -*-
"""from tkinter import *
import random

window = Tk()
window.geometry('700x500')
window.title('Кликер')

points = 0


def check():
    global points
    b.place(x=random.randint(1, 550), y=random.randint(1, 350))
    points += 1
    label['text'] = points
    if points >= 20:
        b['bg'] = 'pink'


b = Button(text='нажми меня', font=('Arial', 20), fg='black', bg="blue", command=check)
b.place(x=200, y=130)
label = Label(text=points, font=('Arial', 15), fg='black')
label.place(x=10, y=10)

window.mainloop()"""



"""from tkinter import *
import random
import time

window = Tk()
window.geometry('700x500')
window.title('Кликер')

points = 0


def check():
    global points
    b.place(x=random.randint(1, 550), y=random.randint(1, 350))
    points += 1
    label['text'] = points
    if points == 20:
        time.sleep(2)

b = Button(text='нажми меня', font=('Arial', 20), fg='black', command=check)
b.place(x=200, y=130)
label = Label(text=points, font=('Arial', 15), fg='black')
label.place(x=10, y=10)

window.mainloop()"""



"""from tkinter import *
import random

window = Tk()
window.geometry('700x500')
window.title('Кликер')

points = 0
click_count1 = 0
click_count2 = 0
reset_count = 0

def check_1():
    global points
    global click_count1
    global click_count2
    global reset_count
    b_1.place(x=random.randint(1, 550), y=random.randint(1, 350))
    points += 1
    label['text'] = points
    click_count1 += 1
    reset_count += 1
    if reset_count == 20:
        click_count1 = 0
        click_count2 = 0
        reset_count = 0
    if click_count1 > 10 and click_count2 < 10:
        b_2['text'] = "Ну пожалуйста"

def check_2():
    global points
    global click_count1
    global click_count2
    global reset_count
    b_2.place(x=random.randint(1, 550), y=random.randint(1, 350))
    points += 1
    label['text'] = points
    click_count1 += 1
    reset_count += 1
    if reset_count == 20:
        click_count1 = 0
        click_count2 = 0
        reset_count = 0
    if click_count1 > 10 and click_count2 < 10:
        b_1['text'] = "Ну пожалуйста"

b_1 = Button(text='нажми меня', font=('Arial', 20), fg='black', bg="green", command=check_1)
b_2 = Button(text='нажми меня', font=('Arial', 20), fg='black', bg="pink", command=check_2)
b_1.place(x=200, y=130)
b_2.place(x=400, y=230)
label = Label(text=points, font=('Arial', 15), fg='black')
label.place(x=10, y=10)

window.mainloop()"""



from tkinter import *
import random

window = Tk()
window.geometry('700x500')
window.title('Кликер')

points_1 = 0
points_2 = 0
points_3 = 0
def check_1():
    global points_1
    b_1.place(x=random.randint(1, 550), y=random.randint(1, 350))
    points_1 += 1
    label_1['text'] = points_1
    if points_1 >= 10:
        b_1['bg'] = 'yellow'
def check_2():
    global points_2
    b_2.place(x=random.randint(1, 550), y=random.randint(1, 350))
    points_2 += 1
    label_2['text'] = points_2
    if points_2 >= 10:
        b_2['bg'] = 'green'
def check_3():
    global points_3
    b_3.place(x=random.randint(1, 550), y=random.randint(1, 350))
    points_3 += 1
    label_3['text'] = points_3
    if points_3 >= 10:
        b_3['bg'] = 'pink'

b_1 = Button(text='нажми меня', font=('Arial', 20), fg='black', bg="blue", command=check_1)
b_1.place(x=200, y=130)
b_2 = Button(text='нажми меня', font=('Arial', 20), fg='black', bg="red", command=check_2)
b_2.place(x=200, y=130)
b_3 = Button(text='нажми меня', font=('Arial', 20), fg='black', bg="orange", command=check_3)
b_3.place(x=200, y=130)
label_1 = Label(text=points_1, font=('Arial', 15), fg='blue')
label_1.place(x=10, y=10)
label_2 = Label(text=points_2, font=('Arial', 15), fg='red')
label_2.place(x=30, y=30)
label_3 = Label(text=points_3, font=('Arial', 15), fg='orange')
label_3.place(x=50, y=50)

window.mainloop()



"""from tkinter import *
import random

window = Tk()
window.geometry('700x500')
window.title('Кликер')

points = 0  # счётчик очков


def check():  # функция, которая отвечает за действия, происходящие после нажатия кнопки
    global points
    b.place(x=random.randint(1, 550), y=random.randint(1,
                                                       350))  # с помощью random каждый раз координаты кнопки будут менятся, так как значения меняются после каждого обращения к функции
    points += 1
    label['text'] = points  # обновление значения очков в надписи


b = Button(text='нажми меня', font=('Arial', 20), fg='black', command=check)  # создание кнопки
b.place(x=200, y=130)  # расположение кнопки в окне
label = Label(text=points, font=('Arial', 15), fg='black')  # вид счётчика в окне
label.place(x=10, y=10)  # расположение счётчика в окне

window.mainloop"""