# -*- coding: cp1251 -*-
"""print(id(1), type(1))"""


"""class A:
    def public(self):
        return 456
    def _privat(self):
        return "test"
    def __protected(self):
        return True
    def wrapper(self):
        return self.__protected()

a = A()
print(a.public())
print(a._privat())
print(a.wrapper())
print(a._A__protected()) #_НазваниеКласса__НазваниеМетода()"""




"""class Singleton(object):
    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance

s = Singleton()
print("Объект создан", s, id(s))
s1 = Singleton()
print("Объект создан", s1, id(s1))

print(s == s1)"""





"""def good_f(func):
    def wrapper(a, b):
        return func(a, b) - 1
    return wrapper

@good_f

def wrong_f(a, b):
    return a + b + 1

def ok_f(a, b):
    return a * b

print(ok_f(5, 6))
print(wrong_f(5, 5))"""





from datetime import datetime

def timeis(func):
    def wrapper(val):
        start = datetime.now()
        res = func(val)
        end = datetime.now()
        print("time", end - start)
        return res
    return wrapper

@timeis

def get_list_1(val):
    return [x for x in range(val) if x % 2 == 1]

@timeis

def get_list_2(val):
    new_list = []
    for x in range(val):
        if x % 2 == 1:
            new_list.append(x)
    return new_list

a = get_list_1(10000000)
b = get_list_1(10000000)