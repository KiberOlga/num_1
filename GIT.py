# -*- coding: cp1251 -*-
def palindrome(word):
    return word[::-1] == word

while True:
    word = input("Введите слово: ")
    if word == "stop":
        break
    if palindrome(word):
        print(f"{word} является палиндромом")
    else:
        print(f"{word} не является палиндромом")