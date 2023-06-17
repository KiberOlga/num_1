# -*- coding: cp1251 -*-
import os
import sys

sys.setrecursionlimit(3000)

current_path = os.path.abspath(__file__)
parent_path = os.path.join(current_path, current_path)
#print(parent_path, current_path)

"""def recurs(count):
    print(count - 1)
    if count - 1 < 0:
        return
    recurs(count - 1)
recurs(5)"""



"""def f(n):
    if n == 0:
        return 1
    if n > 0:
        return 4 * f(n - 1)
print(f(2300)/f(2290))"""





def get_all_files(path):
    for i in os.listdir(path):
        new_path = os.path.join(path, i)
        if os.path.isdir(new_path):
            print(f"Папка: {i}")
            get_all_files(new_path)
        else:
            print(f"- {i}")
get_all_files(r"C:\Users\Asus\PycharmProjects\pythonProject1\module3")