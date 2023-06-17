# -*- coding: cp1251 -*-
"""class Item:
    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight

    def __add__(self, other):
        if isinstance(other, Item):
            return self.price + other.price
        elif isinstance(other, int):
            return self.price + other

item_1 = Item("монитор", 30_000, 0.8)
item_2 = Item("процессор", 40_000, 0.3)

total_price = item_1 + item_2
print(total_price)"""







# Игра Алхимия

"""from tkinter import *
from random import randint

window = Tk()
window.geometry("600x600")

class Fire:
    image = PhotoImage(file="free-icon-fire-9509865.png").subsample(4, 4)

    def __add__(self, other):
        if isinstance(other, Earth):
            return Clay

class Water:
    image = PhotoImage(file="free-icon-water-drop-4246703.png").subsample(4, 4)

class Wind:
    image = PhotoImage(file="wind.png").subsample(4, 4)

class Earth:
    image = PhotoImage(file="ground.png").subsample(4, 4)
    def __add__(self, other):
        if isinstance(other, Fire):
            return Clay

class Clay:
    image = PhotoImage(file="free-icon-pottery-7942410.png").subsample(4, 4)

canvas = Canvas(window, width=600, height=600)
canvas.pack()

elements = [Earth(), Fire(), Water(), Wind()]

for elem in elements:
    canvas.create_image(randint(50, 500), randint(50, 500), image=elem.image)

def move(event):
    images_id = canvas.find_overlapping(event.x, event.y, event.x + 10, event.y + 10)

    if len(images_id) == 2:
        elem_id_1, elem_id_2 = images_id[0], images_id[1]
        element_1 = elements[elem_id_1 - 1]
        element_2 = elements[elem_id_2 - 1]
        new_element = element_1 + element_2
        if new_element:
            if new_element not in elements:
                canvas.create_image(event.x, event.y, image=new_element.image)
                elements.append(new_element)
    canvas.coords(images_id, event.x, event.y)

window.bind("<B1-Motion>", move)

window.mainloop()"""








# Домашняя работа




"""class Item:
    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight

    def __add__(self, other):
        if isinstance(other, Item):
            return self.price + other.price
        elif isinstance(other, int):
            return self.price + other

    def __sub__(self, other):
        if isinstance(other, Item):
            return self.price - other.price
        elif isinstance(other, int):
            return self.price - other

    def __mul__(self, other):
        if isinstance(other, Item):
            return self.weight * other.weight
        elif isinstance(other, int):
            return self.weight * other

    def __truediv__(self, other):
        if isinstance(other, Item):
            return self.weight / other.weight
        elif isinstance(other, int):
            return self.weight / other

item_1 = Item("монитор", 30_000, 0.8)
item_2 = Item("процессор", 40_000, 0.3)

add_price = item_1 + item_2
print(add_price)

sub_price = item_1 - item_2
print(sub_price)

mul_weight = item_1 * item_2
print(mul_weight)

div_weight = item_1 / item_2
print(div_weight)"""




from tkinter import *
from random import randint

window = Tk()
window.geometry("600x600")

class Fire:
    image = PhotoImage(file="free-icon-fire-9509865.png").subsample(4, 4)
    def __add__(self, other):
        if isinstance(other, Earth):
            return Clay

        elif isinstance(other, Water):
            return Steam

class Water:
    image = PhotoImage(file="free-icon-water-drop-4246703.png").subsample(4, 4)
    def __add__(self, other):
        if isinstance(other, Fire):
            return Steam

        elif isinstance(other, Earth):
            return Swamp

class Wind:
    image = PhotoImage(file="wind.png").subsample(4, 4)
    def __add__(self, other):
        if isinstance(other, Earth):
            return Dust

class Earth:
    image = PhotoImage(file="ground.png").subsample(4, 4)
    def __add__(self, other):
        if isinstance(other, Fire):
            return Clay

        elif isinstance(other, Wind):
            return Dust

        elif isinstance(other, Water):
            return Swamp

class Clay:
    image = PhotoImage(file="free-icon-pottery-7942410.png").subsample(4, 4)

class Dust:
    image = PhotoImage(file="free-icon-dust-2396941.png").subsample(4, 4)

class Steam:
    image = PhotoImage(file="aroma.png").subsample(4, 4)

class Swamp:
    image = PhotoImage(file="pngwing.com.png").subsample(4, 4)

canvas = Canvas(window, width=600, height=600)
canvas.pack()

elements = [Earth(), Fire(), Water(), Wind()]

for elem in elements:
    canvas.create_image(randint(50, 500), randint(50, 500), image=elem.image)

def move(event):
    images_id = canvas.find_overlapping(event.x, event.y, event.x + 10, event.y + 10)

    if len(images_id) == 2:
        elem_id_1, elem_id_2 = images_id[0], images_id[1]
        element_1 = elements[elem_id_1 - 1]
        element_2 = elements[elem_id_2 - 1]
        new_element = element_1 + element_2
        if new_element:
            if new_element not in elements:
                canvas.create_image(event.x, event.y, image=new_element.image)
                elements.append(new_element)
    canvas.coords(images_id, event.x, event.y)

window.bind("<B1-Motion>", move)

window.mainloop()

