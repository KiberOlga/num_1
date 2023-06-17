# -*- coding: cp1251 -*-
"""from tkinter import *

window = Tk()
window.geometry("600x600")
canvas = Canvas(window, width=300, height=300, bg="white")

canvas.place(x=0, y=0)
canvas.create_rectangle(10, 10, 110, 110, fill="pink", outline="blue")

canvas.create_rectangle(40, 40, 80, 80, fill="white", outline="")
canvas.create_rectangle(90, 90, 150, 150, fill="white", outline="")
window.mainloop()"""


"""from tkinter import *

window = Tk()
window.geometry("600x600")
canvas = Canvas(window, width=300, height=300, bg="white")"""

"""canvas.pack()
canvas.create_polygon(10, 180, 60, 120, 110, 110, fill="pink", outline="blue")

window.mainloop()"""


"""from tkinter import *

window = Tk()
window.geometry("600x600")
canvas = Canvas(window, width=400, height=400, bg="white")

canvas.pack()
canvas.create_polygon(10, 260, 60, 200, 110, 260, fill="pink")
canvas.create_rectangle(20, 260, 100, 360, fill="pink")
window.mainloop()"""



"""from tkinter import *

window = Tk()
window.geometry("600x600")
canvas = Canvas(window, width=400, height=400, bg="white")

canvas.pack()"""



"""from tkinter import *

window = Tk()
window.geometry("600x600")
canvas = Canvas(window, width=300, height=300, bg="white")
canvas.pack()

class House:

    def __init__(self, color_roof, color_wall):
        self.color_roof = color_roof
        self.color_wall = color_wall
        self.h = 130
        self.w = 140
    def build(self, x, y):
        canvas.create_rectangle(x, self.h - x, y, self)"""

"""home = House("green", "blue")
home_1 = House("green", "black")
print(home.color_roof)
print(home.color_wall)
print(home_1.color_roof)
print(home_1.color_wall)"""






"""from tkinter import *

window = Tk()
window.geometry("600x600")


class Image(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.master.title("Абстракция")
        self.pack(fill=BOTH, expand=True)

        canvas = Canvas(self)

        canvas.create_polygon(10, 260, 60, 200, 110, 260, outline="blue", fill="violet")
        canvas.create_polygon(90, 390, 270, 220, 160, 340, outline="red", fill="orange")
        canvas.create_rectangle(500, 550, 190, 430, outline="yellow", fill="pink")
        canvas.create_rectangle(240, 90, 270, 60, outline="blue", fill="orange")
        canvas.create_rectangle(20, 139, 90, 180, outline="gray", fill="black")

        canvas.pack(fill=BOTH, expand=True)

f = Image()

window.mainloop()"""




import random

class Warrior_war:
    def __init__(self, name, health=100):
        self.name = name
        self.health = health

    def kick(self, aim):
        if type(self) == type(aim):
            aim.health -= 20
        else:
            raise TypeError

warriors = [Warrior_war('Воин 1'), Warrior_war('Воин 2')]
while True:
    a = input('1 - атака какого-то воина. 2 - выход из программы. Введите 1 или 2: ')
    if a == '1':
        b = random.randint(0, 1)
        attacker, pray = warriors[b], warriors[b - 1]
        attacker.kick(pray)
        print(attacker.name, 'атаковал', pray.name)
        print('У', pray.name, 'осталось здоровья', pray.health)
        if pray.health <= 0:
            print(attacker.name, 'победил! Ура!')
            break
    elif a == '2':
        break
    else:
        print('Ошибка при вводе')


