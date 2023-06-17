# -*- coding: cp1251 -*-
""""class user:
    def __init__(self, name, color_eyes, height, weight):
        self.name = name
        self.color_eyes = color_eyes
        self.height = height
        self.weight = weight

person1 = user(name="Alice", color_eyes="green", height="158", weight="46")
person1.name = "Kate"
print(f"Её зовут {person1.name}, она весит {person1.weight} при росте {person1.height} и у неё {person1.color_eyes} глаза")

person2 = user(name="Ann", color_eyes="blue", height="170", weight="53")
print(f"Её зовут {person2.name}, она весит {person2.weight} при росте {person2.height} и у неё {person2.color_eyes} глаза")"""
import random

"""class First:
    def first1(self):
        print("first1")
    def first2(self):
        print("first2")

class Second(First):
    def three(self):
        print("three")
    def first1(self):
        print("first1")

firstFirst = Second()
firstFirst.three()
firstFirst.first1()
secondSecond = First
firstFirst.first2()"""







"""import random

class user:
    def __init__(self, name, health, damage_min, damage_max, armor):
        self.name = name
        self.health = health
        self.damage = random.randint(damage_min, damage_max)
        self.armor = armor

    def info(self):
        print(f"{self.name} имеет {self.health}, {self.armor}")

    def health_damage(self, enemy_damage):
        self.health -= enemy_damage
        print(f"У {self.name} осталось {self.health} жизни")

    def fight(self, enemy):
        if enemy.health <= 0 or self.damage >= enemy.health:
            print(f"{enemy.name} уничтожен")
        else:
            enemy.health_damage(self.damage)
            print(f"{enemy.name}, оказался силён, давай попробуем ещё")

hunter = user(name="Mag", health=100, damage_min=5, damage_max=7, armor=10)
hardWolf = user(name="HardWolf", health=100, damage_min=5, damage_max=7, armor=10)

hunter.info()
hardWolf.info()

hunter.fight(hardWolf)
hunter.fight(hardWolf)
hunter.fight(hardWolf)
hunter.fight(hardWolf)"""






"""import random

class user:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def push(self, damage_min, damage_max):
        self.damage = random.randint(damage_min, damage_max)
        #damage = 15
        self.health -= damage

    ""def damage(self, damage_min, damage_max):
        self.damage = random.randint(damage_min, damage_max)
        damage = 15
        self.health -= damage""


user1 = user(name="Mage", health=100, damage_min=7, damage_max=10)
user2 = user(100)
user1.push(user2)

""def info(self):
        print(f"{self.name} имеет {self.health} здоровья")

    def health_damage(self, enemy_damage):
        self.health -= enemy_damage
        print(f"У {self.name} осталось {self.health} жизни")

    def fight(self, enemy):
        if enemy.health <= 0 or self.damage >= enemy.health:
            print(f"{enemy.name} уничтожен")
        else:
            enemy.health_damage(self.damage)
            print(f"{enemy.name}, оказался силён, давай попробуем ещё")""

""class Mage(user):
    def mage(self):
        mage = user(name="Mage", health=100, damage_min=7, damage_max=10)
        mage.info()

class Warrior(user):
    def Warrior(self):
        warrior = user(name="Warrior", health=100, damage_min=10, damage_max=15)
        warrior.info()

class Archer(user):
    def archer(self):
        archer = user(name="Archer", health=100, damage_min=5, damage_max=7)
        archer.info()""
"""



import random
class user:
    def __init__(self, health):
        self.health = health

    def push(self, aim):
        damage_min = 7
        damage_max = 15
        damage = random.randint(damage_min, damage_max)
        aim.take_damage(damage)

    def damage(self, damage):
        self.health -= damage


class Mage(user):
    def mage_attack(self, aim):
        damage_min = 10
        damage_max = 17
        damage = random.randint(damage_min, damage_max)
        aim.take_damage(damage)


class Warrior(user):
    def warrior_attack(self, aim):
        damage_min = 8
        damage_max = 12
        damage = random.randint(damage_min, damage_max)
        aim.take_damage(damage)


class Archer(user):
    def archer_attack(self, aim):
        damage_min = 5
        damage_max = 10
        damage = random.randint(damage_min, damage_max)
        aim.take_damage(damage)

"""mage = Mage(100)
warrior = Warrior(100)
archer = Archer(100)

mage.mage_attack(warrior)"""