"""import random
import emoji
a = [1, 2, 3, 4, 5]
s = 0
for i in range(len(a)):
    s = s + a[i]
print("Сумма списка = ",s)
numbers = [1, 2, 3, 4, 5]
for number in range(len(numbers) - 1)"""
"""import random
animals = ["кот", "собака", "кролик"]
description = ["мохнатый", "игривый", "милый"]
print(animals)
print(description)
for i in range(4):
    print(random.choice(animals + description))
    print(random.choice(description + animals))

import random
print("Введите 3 названия животных")
pet_1 = input("1 животное: ")
pet_2 = input("2 животное: ")
pet_3 = input("3 животное: ")
print("Введите 3 описания животных")
description_1 = input("1 описание: ")
description_2 = input("2 описание: ")
description_3 = input("3 random.choice: ")
for i in range(3):
    print(random.choice([description_1, description_2, description_3]) + " " + random.choice([pet_1, pet_2, pet_3]))"""

import random
numbers = []
for i in range(30):
    numbers.append(random.randint(0, 5))
print(numbers)
print(numbers.count(5))

"""import random
numbers = []
for i in range(30):
    print(numbers.append(random.randint(0, 5)))
print(numbers.count(5))"""

"""import random
rand_list = []
n = 10
for i in range(n):
    rand_list.append(random.randint(3, 9))
print(rand_list)"""



"""import random
facts = ["варпол", "прдолосс"]
for fact in facts:
    print(fact)
print(random.choice(facts))
print(random.randint(1, 100))
print(emoji.emojize(":snake: is :green_heart:"))
income = []
print("Введите ваши доходы за последние 6 месяцев?")
for money in range(6) :
    incame = int(input())
    income.append(incame * 0.3)
print("Ваши накопления составлят: " + str(sum(income)) + "рублей")
i = 10
s = 0
a = 88
while i < 10:
    i +=1
    print(i)
x = 0
income = []
while x < 6:
    incame = int(input("Введите ваши доходы: "))
    income.append(incame * 0.3)
    x += 1
print("Ваши накопления составляют: ", sum(income), "рублей")"""


