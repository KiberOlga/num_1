# -*- coding: cp1251 -*-
"""from pprint import pprint
from typing import Iterator

goods = [
        {
            "name": "Iphone 12",
            "brand": "Apple",
            "price": 60000
        },
        {
            "name": "Samsung Galaxy A53",
            "brand": "Samsung",
            "price": 40000
        },
        {
            "name": "Nokia 3310",
            "brand": "Nokia",
            "price": 80000
        }
    ]

if __name__ == "__main__":


    def item_price(item):
        return item.get("price")
    #print(sorted(goods, key=item_price)) #так делать не надо
    #pprint(sorted(goods,key=lambda item: item["price"]))

    apple_list = filter(lambda item: item["brand"] == "Apple", goods)
    print(list(apple_list))





    numbers = ["1", "2", "3", "4", "5"]
    numbers_list = list(map(int, numbers))
    #print(*numbers_list)




    name_list = ["Kate", "Ivan", "Alice"]
    surname_list = ["Selezneva", "Petrov", "Grey"]
    ages = [16, 17]
    full_name_list = list(map(lambda name, surname, age: f"{name} {surname} {age}", name_list, surname_list, ages))
    #print(full_name_list)




    indexad_goods = []

    for i, item in enumerate(goods):
        indexad_goods.append({i: item})

    #pprint(indexad_goods)




    patronymic_list = ["Daniilovna", "Vasilevich", "Alekseevna"]
    for name, surname, patronymic in zip(name_list, surname_list, patronymic_list):
        print(name, surname, patronymic)"""














#Домашняя работа


class Item:
    def __init__(self, price, brand):
        self.price = price
        self.brand = brand

    def __repr__(self):
        return self.brand

items_list = [
    Item(1000, "Apple"),
    Item(1200, "Apple"),
    Item(900, "Samsung"),
    Item(700, "Samsung"),
    Item(660, "Xiaomi")
]

for good in list(filter(lambda item: item.brand == "Apple", items_list)): print(good.brand, good.price)

#print(list(filter(lambda item: item.brand == "Apple", items_list)))






"""#1 способ
names_list = ['данил', 'артём', 'никита', 'влад']
print(list(names.capitalize() for names in names_list))

#2 способ
names_list = ['данил', 'артём', 'никита', 'влад']
print(list(names.title() for names in names_list))"""
