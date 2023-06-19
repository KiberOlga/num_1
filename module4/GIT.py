# -*- coding: cp1251 -*-
def palindrome(string):
    return string[::-1] == string

while True:
    string = input("Введите слово: ")
    if string == "stop":
        break
    if palindrome(string):
        print(f"{string} является палиндромом")
    else:
        print(f"{string} не является палиндромом")