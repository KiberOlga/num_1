# -*- coding: cp1251 -*-
"""from tkinter import *
window = Tk()
window.geometry('900x300')
window.title('No virus')
window.config(bg="black")
window.resizable(width=False, height=False)
text = Label(text="Ты попался на кликбейт, теперь ты под моей властью",
             fg="red", bg="black", font=("Courier New", 25))
text.place(x=100, y=100, width=700, height=100)
count_text = Label(text="6", fg="red", bg="black", font=("Courier New", 34))
def count_start():
    if int(count_text["text"]) > 0:
        count_text["text"] = int(count_text["text"]) - 1
        count_text.place(x=250, y=25, width=400, height=100)
        window.after(1000, on_close)
    else:
        width = window.winfo_screenwidth()
        heigth = window.winfo_screenwidth()
        window.geometry(str(width)+"x"+str(heigth))
        photo = PhotoImage(file="img_2.png")
        label = Label(image=photo, bg="black")
        label.place(width=900, height=300, x=0, y=0)

def on_close():
    count_start()

window.protocol("WM_DELETE_WINDOW", on_close)
window.mainloop()"""



"""from tkinter import *
window = Tk()
window.geometry('900x300')
window.title('No virus')
window.config(bg='black')
window.resizable(width=False, height=False)
text = Label(text='Ты под моей властью',
             fg='red', bg='black', font=('Courier New', 34))
text.place(x=100, y=100, width=700, height=100)
count_text = Label(text='6', fg='red', bg='black', font=('Courier New', 34))

def count_start():
    if int(count_text['text']) > 0:
        count_text['text'] = int(count_text['text']) - 1
        count_text.place(x=250, y=25, width=400, height=100)
        window.after(1000, on_close)
    else:
        width = window.winfo_screenwidth()
        height = window.winfo_screenheight()
        window.geometry(str(width)+'x'+str(height))
        photo = PhotoImage(file='img_3.png')
        label = Label(bg="black", image=photo)
        label.place(width=900, height=300, x=0, y=0)


def on_close():
    count_start()

window.protocol('WM_DELETE_WINDOW', on_close)

window.mainloop()"""



from tkinter import *
def a():
    text.config(text='Чтобы забрать выйгрыш необходимо внести 1000руб.', font=("Arial", 20))
    b.destroy()
window = Tk()
window.geometry('800x700')
window.title('ЛОТЕРЕЯ!')
window.config(bg='turquoise')
window.resizable(width=False, height=False)
text = Label(text='ВЫ ВЫЙГРАЛИ В ЛОТЕРЕЕ!',
             fg='white', bg='black', font=('Monotype Corsiva', 34))
text.place(x=65, y=100, width=700, height=100)

b = Button(text='ПОЛУЧИТЬ ВЫЙГРЫШ!', font=('Arial', 20), fg='black', bg="white", command=a)
b.place(x=265, y=300)
def on_close():
    a()
window.protocol('WM_DELETE_WINDOW', on_close)
window.mainloop()



"""N = int(input("Введите количество собак: "))
list_1 = list()
for i in range(N):
    list_1.append(int(input("Введите количество очков собаки: ")))
print(list_1)
min_1 = list_1.index(min(list_1))
max_1 = list_1.index(max(list_1))
list_1[max_1], list_1[min_1] = list_1[min_1], list_1[max_1]
print(list_1)"""


