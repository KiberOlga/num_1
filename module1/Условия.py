"""a = []
for i in range(7):
    a.append(int(input("Какая сегодня погода? ")))
print("Средняя температура - ", sum(a)/len(a))
for temp in a:
    if temp <= 7:
        print("Надень куртку и зонтик")
    elif temp <= -5:
        print("Возьми шапку и зонтик")
    else:
        print("Жара")"""

"""films_2 = [int(input()) for i in range(5)]
print(films_2)"""
"""favorite_actor = input("Какой ваш любимый актёр?")
actor = input("Кто играет главную роль в фильме?")
rang_films = float(input("Введите ранг фильма "))
films = ["Люди в чёрном", "Форсаж", "Титаник", "Дневник баскетболистов", "Брюс всемогущий", "Брат 2"]
print(films)
films = [i.upper() for i in films]
if actor == "уилл Смит" and (actor == favorite_actor or rang_films >= 7.5):
    print(films[0])
elif actor == "вин дизель" and (actor == favorite_actor or rang_films >= 7.5):
    print(films[1])
elif actor == "кейт уинслет" and (actor == favorite_actor or rang_films >= 7.5):
    print(films[2])
elif actor == "леонардо де каприо" and (actor == favorite_actor or rang_films >= 7.5):
    print(films[3])
elif actor == "джим керри" and (actor == favorite_actor or rang_films >= 7.5):
    print(films[4])
elif actor == "сергей бобров" and (actor == favorite_actor or rang_films >= 7.5):
    print(films[-1])
else:
    print("Ничего не найдено")"""


"""import random
k = 3
while True:
    c = random.randint(1, 10)
    u = int(input("Введите число "))
    d = abc(c - u)
    if c == u:
        print("Поздравляем")
        break
    elif d ==1:
        print("Почти")
        k -= 1
        print("У тебя осталось 2 попытки")
    else:
        print("нет")
    if k == 0:
        print("Попыток нет")
    break"""

"""weather = []
weather.append(int(input("Какая сегодня погода? ")))
for temp in weather:
    if temp <= -7:
        print("Очень холодно!")
    elif temp <= 0:
        print("Холодно!")
    elif temp <= 15:
        print("Прохладно!")
    elif temp <= 25:
        print("Тепло!")
    elif temp <= 35:
    
    print("Жарко!")
    else:
        print("Очень жарко!")"""

"""import random
while True:
    computer = random.randint(1, 2)
    user = int(input("Введите орёл(1) или решка(2): "))
    difference = abs(computer - user)
    if computer == user:
        print("Поздравляем! Вы выиграли миллион рублей!")
        break
    else:
        print("Вы проиграли...")
    break"""

"""list_number = [2, -9, 35, 21, 0, -6, 5]
print(sorted(list_number))"""

y = [2, 0, 35, 21, 4, -6, 5]
x = len(y)
for i in range(1, x):
    for a in range(x - 1, i - 1, -1):
        if y[a - 1] > y[a]:
            y[a - 1], y[a] = y[a], y[a - 1]
print(*y)





