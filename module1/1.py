"""with open("file.txt") as f:
    for line in f.readlines():
        print(line)

file = open("file.txt")
massive = [int(i) for i in file]
print(massive)"""
"""import math

file = open("numbers.txt", "w")
numbers = [int(input()) for i in range(7)]
result = 0
for number in numbers:
    result += math.factorial(number) - math.sqrt(number)
    file.write(str(number))
file.close()"""

"""def Calculate(x, y):
    sign = input("Введите арифметический знак ")
    if sign == "+":
        return x + y
    return x - y
print(Calculate(19, 7))

def Calculate2(x, y):
    return x + y, x - y
print(Calculate(30, 17))"""

def leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
        return year // 10
    else:
        return year // 10
for year in range(1800, 2023):
    if leap_year(year) >= 195:
    print(year, leap_year(year))