# -*- coding: cp1251 -*-
"""user_choice = input("Напишите жанр игры: ")
action = "Team Fortress 2"
adventure = "Stray"
role = "Path of Exile"
simulator = "Potion Craft: Alchemist Simulator"
strategy = "RimWorld"
sports_and_racing = "BLACKTAIL"
if user_choice == "Action":
    print(action)
elif user_choice == "Adventure":
    print(adventure)
elif user_choice == "Role":
    print(role)
elif user_choice == "Simulator":
    print(simulator)
elif user_choice == "Strategy":
    print(strategy)
elif user_choice == "Sports and racing":
    print(sports_and_racing)"""


"""age = 18
is_allow = True if age >= 18 else False
print(is_allow)


import random
a = random.randint(1, 10)
print(a)"""








import random

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
hunter.fight(hardWolf)