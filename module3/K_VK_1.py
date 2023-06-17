# -*- coding: cp1251 -*-
import requests
import json

url = 'https://swapi.dev/api/'
response = requests.get(url).json()

def diameter(api):
    response = requests.get(f"{url}/{api}/").json()
    planets = response.get("results")
    m_res = []
    for planet in planets:
        diameter = int(planet.get("diameter"))
        m_res.append(diameter)
        m_diameter = max(m_res)
    #print(m_res)
    return ("Планета Bespin имеет диаметр", m_diameter)

diameter("planets")



