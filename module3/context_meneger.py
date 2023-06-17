# -*- coding: cp1251 -*-
"""import time

class RunningCodeJudge:
    def __init__(self):
        self.start = None

    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        t = time.time() - self.start
        print(f"Программа работает {t} секунд")

        if exc_type is TypeError:
            return True

with RunningCodeJudge() as p1:
    my_list = [x for x in range(1, 1000000)]
    my_list -= "s"
    print(p1)"""


"""my_list = [1, 2, 3, 4, 5]
my_liter = iter(my_list)
print(next(my_liter))
print(next(my_liter))
print(next(my_liter))
print(next(my_liter))
print(next(my_liter))"""

"""for i in my_liter:
    print(i)"""


"""import random
class RandomIter:
    def __init__(self, limit):
        self.limit = limit
        self.limit_2 = limit

    def __iter__(self):
        self.limit = self.limit_2
        return self

    def __next__(self):
        if self.limit == 0:
            raise StopIteration
        self.limit -= 1
        return random.randint(0, 100)

rand_iter = RandomIter(10)
for i in rand_iter:
    print(i)

for i in rand_iter:
    print(i)"""



# Домашняя работа

"""class MyFile:
    def __init__(self, name, mode, encoding='utf-8'):
        self.name = name
        self.mode = mode
        self.encoding = encoding

    def __enter__(self):
        self.file = open(self.name, self.mode, encoding=self.encoding)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()

with MyFile('test.txt', 'r', encoding='utf-8') as file:
    print(file.read())"""



class InfiniteIterator:
    def __init__(self):
        self.number = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.number += 1
        return self.number

for i in InfiniteIterator():
    print(i)
