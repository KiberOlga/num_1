# -*- coding: cp1251 -*-
from fpdf import FPDF
from datetime import datetime
pdf = FPDF("P", "mm", "A4")
pdf.add_page()

pdf.output("birthdayGift1.pdf")
pdf.image('img_4.png', h=279, w=210, x=0, y=0)
pdf.add_font("Comic", "", "C:\WINDOWS\FONTS\COMIC.ttf", uni=True)
pdf.set_font("Comic", size=37)
pdf.set_text_color(0, 0, 0)

friend_name = input("Кого ты будешь поздравлять?\n")
pdf.cell(0, 100, ln=1)
pdf.cell(0, 20, txt="Дорогой, " + friend_name + " !", align="C", ln=1)

pdf.set_font("Comic", size=18)
pdf.set_text_color(0, 0, 0)
message = input("Введите текст поздравления\n")
pdf.set_left_margin(50)
pdf.set_right_margin(50)
pdf.multi_cell(0, 20, txt=message, align="C")

today = datetime.today().strftime("%d.%m.%Y")
pdf.set_text_color(0, 0, 0)
pdf.cell(0, 10, txt=today, align="R")
pdf.output("birthdayGift1.pdf")