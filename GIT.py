# -*- coding: cp1251 -*-
def palindrome(word):
    return word[::-1] == word

while True:
    word = input("������� �����: ")
    if word == "stop":
        break
    if palindrome(word):
        print(f"{word} �������� �����������")
    else:
        print(f"{word} �� �������� �����������")