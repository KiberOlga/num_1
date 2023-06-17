# -*- coding: cp1251 -*-
"""class Year:
    def __init__(self, days,season):
        self.__days = days
        self.__season = season

    def get_days(self):
        return self.__days

    def get_season(self):
        return self.__season

    def set_days(self, days):
        self.__days = days

    def set_season(self, season):
        self.__season = season

year = Year(365, "winter")"""

"""year.set_days(366)
year.set_season("summer")
print(year.get_days())
print(year.get_season())"""






"""class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age <= 0:
            raise ValueError("Тебя ещё не существует, малыш")
        self.__age = age

person = Person("Kate", 24)
person.name = "Maria"
person.age = 0
print(person.name)
print(person.age)"""








# Домашняя работа

"""class Year:
    def __init__(self, days, season):
        self.__days = days
        self.__season = season

    @property
    def days(self):
        return self.__days

    @days.setter
    def days(self, days):
        if days <= 364 or days >= 367:
            raise ValueError("Ты живёшь на другой планете")
        self.__days = days

    @property
    def season(self):
        return self.__season

    @season.setter
    def season(self, season):
        self.__season = season

year = Year(365, "summer")

year.days = 366
year.season = "spring"
print(year.days)
print(year.season)"""




class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @name.deleter
    def name(self):
        del self.__name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age <= 0:
            raise ValueError("Тебя ещё не существует, малыш")
        self.__age = age

    @age.deleter
    def age(self):
        del self.__age

person = Person("Kate", 24)
person.name = "Maria"
person.age = 14
del person.name
del person.age
#print(person.name)
#print(person.age)