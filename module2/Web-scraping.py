# -*- coding: cp1251 -*-
"""hours = int(input())
if hours >= 12 and hours <= 16:
    print("день")
elif hours > 16 and hours <= 23:
    print("вечер")
elif hours >= 0 and hours <= 2:
    print("ночь")
elif hours >2 and hours< 12:
    print("утро")
else:
    print("ты дурак")"""



"""import requests
import json

url = "https://swapi.dev/api/"
response = requests.get(url).json()

people_api = response.get("people")
planets_api = response.get("planets")

def check_people(url):
    for i in range(1, 6):
        response = requests.get(f"{url}/{i}").json()
        print(response)

def check_planets(url):
    diameters = []
    for i in range(1, 6):
        response = requests.get(f"{url}/{i}").json()
        diameters.append({response.get("name"): response.get("diameter")})
    print(diameters)

check_people(people_api)
check_planets(planets_api)"""




"""import requests
import json

url = "https://swapi.dev/api/"
response = requests.get(url).json()

starships_api = response.get('starships')

def check_starships(url):
    max_atmosphering_speed = []
    for i in range(1, 6):
        response = requests.get(f"{url}/{i}").json()
        max_atmosphering_speed.append({response.get("name"): response.get("max_atmosphering_speed")})
        if max_atmosphering_speed == "unknown":
            continue
    print(max_atmosphering_speed)

check_starships(starships_api)"""




import requests
import json

url = 'https://swapi.dev/api/'
response = requests.get(url).json()

def check_func(url):
    max_atmosphering_speed = 0
    the_fastest_ship = ""
    num_sheeps = [2, 3, 5, 10, 13]
    for i in num_sheeps:
        a = requests.get(f'{url}/{i}').json().get('max_atmosphering_speed')
        print(a)
        a = int(a)
        if a > max_atmosphering_speed:
            max_atmosphering_speed = a
            the_fastest_ship = requests.get(f'{url}/{i}').json().get('name')

    print("The fastest ship is:", the_fastest_ship)


check_func(response.get('starships'))
