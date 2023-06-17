# -*- coding: cp1251 -*-
"""from tkinter import *
import random

window = Tk()

w = 600
h = 600
window.geometry(str(w) + "x" + str(h))

canvas = Canvas(window, width=w, height=h)
canvas.place(in_=window, x=0, y=0)
bg_photo = PhotoImage(file="img_2.png")

class Knight:
    def __init__(self):
        self.x = 80
        self.y = h // 2
        self.v_y = 0
        self.photo = PhotoImage(file="knight.png")

    def stop(self, event):
        self.v_y = 0

    def up(self, event):
        self.v_y = -5

    def down(self, event):
        self.v_y = 5

class Dragon:
    def __init__(self):
        self.x = 580
        self.y = random.randint(50, 550)
        self.v_y = random.randint(1, 5)
        self.photo = PhotoImage(file="img.png")


knight = Knight()

dragons = []
for i in range(3):
    dragons.append(Dragon())

def game():
    canvas.delete("all")
    canvas.create_image(300, 300, image=bg_photo)
    canvas.create_image(knight.x, knight.y, image=knight.photo)
    knight.y += knight.v_y

    current_dragon = 0
    dragon_to_kill = -1
    for dragon in dragons:
        dragon.x -= dragon.v_y
        canvas.create_image(dragon.x, dragon.y, image=dragon.photo)
        if ((dragon.x - knight.x) ** 2) + ((dragon.y - knight.y) ** 2) <= 96 ** 2:
            dragon_to_kill = current_dragon

        current_dragon += 1
        if dragon.x <= 0:
            canvas.delete("all")
            canvas.create_text(w//2, h//2, text="You lose", font="Arial", fill="white")
            break

    if dragon_to_kill >= 0:
        del dragons[dragon_to_kill]

    if len(dragons) == 0:
        canvas.delete("all")
        canvas.create_text(w//2, h//2, text="You win", font="Arial", fill="white")
    else:
        window.after(5, game)

game()

window.bind("<Key-Up>", knight.up)
window.bind("<Key-Down>", knight.down)
window.bind("<KeyRelease>", knight.stop)

window.mainloop()"""




from tkinter import *
import random

window = Tk()

w = 600
h = 600
window.geometry(str(w) + "x" + str(h))

canvas = Canvas(window, width=w, height=h)
canvas.place(in_=window, x=0, y=0)
bg_photo = PhotoImage(file="img_2.png")

class Knight:
    def __init__(self):
        self.x = 80
        self.y = h // 2
        self.v_y = 0
        self.v_x = 0
        self.photo = PhotoImage(file="knight.png")

    def stop(self, event):
        self.v_y = 0
        self.v_x = 0

    def up(self, event):
        self.v_y = -2

    def right(self, event):
        self.v_x = +2

    def left(self, event):
        self.v_x = -2

    def down(self, event):
        self.v_y = 2

class Dragon:
    def __init__(self):
        self.x = 580
        self.y = random.randint(50, 550)
        self.v = random.randint(1, 2)
        self.photo = PhotoImage(file="img.png")


knight = Knight()

dragons = []
for i in range(3):
    dragons.append(Dragon())

def game():
    canvas.delete("all")
    canvas.create_image(300, 300, image=bg_photo)
    canvas.create_image(knight.x, knight.y, image=knight.photo)
    knight.y += knight.v_y
    knight.x += knight.v_x

    current_dragon = 0
    dragon_to_kill = -1
    for dragon in dragons:
        dragon.x -= dragon.v
        canvas.create_image(dragon.x, dragon.y, image=dragon.photo)
        if ((dragon.x - knight.x) ** 2) + ((dragon.y - knight.y) ** 2) <= 96 ** 2:
            dragon_to_kill = current_dragon

        current_dragon += 1
        if dragon.x <= 0:
            canvas.delete("all")
            canvas.create_text(w//2, h//2, text="You lose", font="Arial", fill="black")
            break

    if dragon_to_kill >= 0:
        del dragons[dragon_to_kill]

    if len(dragons) == 0:
        canvas.delete("all")
        canvas.create_text(w//2, h//2, text="You win", font="Arial", fill="black")
    else:
        window.after(5, game)

    if knight.y <= 52:
        knight.y = 53
    if knight.y >= 543:
        knight.y = 544
    if knight.x <= 50:
        knight.x = 51
    if knight.x >= 550:
        knight.x = 551

game()

window.bind("<Key-Up>", knight.up)
window.bind("<Key-Down>", knight.down)
window.bind('<Key-Right>', knight.right)
window.bind('<Key-Left>', knight.left)
window.bind("<KeyRelease>", knight.stop)

window.mainloop()




"""from tkinter import *
import random

window = Tk()

w = 600
h = 600
window.geometry(str(w) + "x" + str(h))

canvas = Canvas(window, width=w, height=h)
canvas.place(in_=window, x=0, y=0)
bg_photo = PhotoImage(file="img_2.png")

class Knight:
    def __init__(self):
        self.x = 80
        self.y = h // 2
        self.v_y = 0
        self.photo = PhotoImage(file="knight.png")

    def stop(self, event):
        self.v_y = 0

    def up(self, event):
        self.v_y = -5

    def down(self, event):
        self.v_y = 5

class Dragon:
    def __init__(self):
        self.x = 580
        self.y = random.randint(50, 550)
        self.v_y = random.randint(1, 5)
        self.photo = PhotoImage(file="img.png")

knight = Knight()

dragons = []
for i in range(3):
    dragons.append(Dragon())

def game():
    canvas.delete("all")
    canvas.create_image(300, 300, image=bg_photo)
    canvas.create_image(knight.x, knight.y, image=knight.photo)
    knight.y += knight.v_y

    current_dragon = 0
    dragon_to_kill = -1
    for dragon in dragons:
        dragon.x -= dragon.v_y
        canvas.create_image(dragon.x, dragon.y, image=dragon.photo)
        if ((dragon.x - knight.x) ** 2) + ((dragon.y - knight.y) ** 2) <= 96 ** 2:
            dragon_to_kill = current_dragon

        current_dragon += 1
        if dragon.x <= 0:
            canvas.delete("all")
            canvas.create_text(w//2, h//2, text="You lose", font="Arial", fill="black")
            break

    if dragon_to_kill >= 0:
        del dragons[dragon_to_kill]

    if len(dragons) == 0:
        canvas.delete("all")
        canvas.create_text(w//2, h//2, text="You win", font="Arial", fill="black")
    else:
        window.after(5, game)

    if knight.y <= 52:
        knight.y = 53
    if knight.y >= 543:
        knight.y = 544
    if knight.x <= 50:
        knight.x = 51
    if knight.x >= 550:
        knight.x = 551

game()

window.bind("<Key-Up>", knight.up)
window.bind("<Key-Down>", knight.down)
window.bind("<KeyRelease>", knight.stop)

window.mainloop()"""