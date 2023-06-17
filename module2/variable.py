# -*- coding: cp1251 -*-
"""first_var = 3
second_var = 3.14
third = first_var + second_var"""
"""input_var = int(input("Введите число: "))
input_second_var = int(input("Введите второе число: "))"""
"""if input_var > input_second_var:
    print(input_var, "больше, чем", input_second_var)
elif input_var == input_second_var:
    print(input_var, "равен", input_second_var)
else:
    print(input_var, "меньше", input_second_var)"""

"""try:
    input_var = int(input("Введите число: "))
    #input_second_var = int(input("Введите второе число: "))
except ValueError:
    print("Введи число! ")
else:
    if input_var % 10 ==0:
        print(input_var, "кратен 10")
    if input_var == input_second_var:
        print(input_var, "кратен 5")
    else:
        print(input_var, "не кратен")"""


"""n = int(input())
for i in range(n):
    print(i)"""

"""list = ["стоп", "стул", "шкаф"]
print(list[2])"""

"""def name():
    name = input()
    print("меня зовут", name)
name()
def add(x, y):
    return x * y
add(2, 3)"""



def calculate(x,y,a):
    if a == '+':
        return x + y
    elif a == '-':
        return x - y
    elif a == '*':
        return x * y
    elif a == '/':
        return x / y
try:
    x = int(input("Введите первое число: "))
    a = input("Введите арифметический знак: ")
    y = int(input("Введите второе число: "))
except ValueError:
    print("Запустите калькулятор заново и введите допустимое значение!")
else:
    e = calculate(x, y, a)
    print(e)
    file = open('calculations.txt', 'a')
    file.write(f'{e}' + '\n')


"""print("Введите коэффициенты для уравнения ax^2 + bx + c = 0: ")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
def calculate_discriminant(a, b, c):
    return b*b - 4*a*c
e = calculate_discriminant(a, b, c)
print(e)"""