# -*- coding: cp1251 -*-
"""def function(a, b, c, *args, **kwargs):
    print(a)
    print(b)
    print(c)
    print(kwargs.get("k"))
    print(args)
    print(kwargs)

function(15, 13, 17, 50, True, k = 47, f = "two")"""

"""list = [i for i in range(100)]
list1 = {x: len(x) for x in ["orange", "red", "blue", "grey"]}
print(list)
print(list1)"""

"""time = 17
go_to_sleep = True if time > 22 else False
print(go_to_sleep)"""

"""val = None
if val is None:
    res  = 0
else:
    res = val

res = 0 if val is None else val

res = val or res"""

"""dict = {"1": "10", "4": "40", "6": "60"}
for i in range(1, 7):
    value = dict.get(str(i))
    if value is None:
        res = 0
    else:
        res = value"""

"""list = [i**4 if i < 5 else i for i in range(100) if i % 2 == 0]
print(list)
list2 = [i**2 if i % 2 == 0 else i for i in range(20) if i > 6]
print(list2)"""

"""dict = {("1", "2"): "10", "4": "40", "6": "60"}
print(dict[("1", "2")])
new_yuple = (5, 6, 7)
print(type(new_yuple))
new_new_yuple = list(new_yuple)
print(type(new_new_yuple))"""

"""dict = {("1", "2"): "10", "4": "40", "6": "60"}
print(dict[("1", "2")])
new_yuple = ([5, 6, 7], 4, 6)
print(new_yuple)
new_yuple[0].append(4)
print(new_yuple)"""






"""list_1 = [i for i in range(1, 11) if i % 2 == 0]
list_2 = [i for i in range(1, 11) if i % 2 != 0]
print(list_1)
print(list_2)"""



a = (5, 3, 2, 1, 4)
print(tuple(sorted(a)))