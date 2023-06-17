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
        a = int(a)
        if a > max_atmosphering_speed:
            max_atmosphering_speed = a
            the_fastest_ship = requests.get(f'{url}/{i}').json().get('name')

    return ("The fastest ship is: ", the_fastest_ship)

check_func(response.get('starships'))
