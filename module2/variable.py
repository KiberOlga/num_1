# -*- coding: cp1251 -*-
"""first_var = 3
second_var = 3.14
third = first_var + second_var"""
"""input_var = int(input("������� �����: "))
input_second_var = int(input("������� ������ �����: "))"""
"""if input_var > input_second_var:
    print(input_var, "������, ���", input_second_var)
elif input_var == input_second_var:
    print(input_var, "�����", input_second_var)
else:
    print(input_var, "������", input_second_var)"""

"""try:
    input_var = int(input("������� �����: "))
    #input_second_var = int(input("������� ������ �����: "))
except ValueError:
    print("����� �����! ")
else:
    if input_var % 10 ==0:
        print(input_var, "������ 10")
    if input_var == input_second_var:
        print(input_var, "������ 5")
    else:
        print(input_var, "�� ������")"""


"""n = int(input())
for i in range(n):
    print(i)"""

"""list = ["����", "����", "����"]
print(list[2])"""

"""def name():
    name = input()
    print("���� �����", name)
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
    x = int(input("������� ������ �����: "))
    a = input("������� �������������� ����: ")
    y = int(input("������� ������ �����: "))
except ValueError:
    print("��������� ����������� ������ � ������� ���������� ��������!")
else:
    e = calculate(x, y, a)
    print(e)
    file = open('calculations.txt', 'a')
    file.write(f'{e}' + '\n')


"""print("������� ������������ ��� ��������� ax^2 + bx + c = 0: ")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
def calculate_discriminant(a, b, c):
    return b*b - 4*a*c
e = calculate_discriminant(a, b, c)
print(e)"""