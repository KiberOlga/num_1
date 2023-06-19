# -*- coding: cp1251 -*-
"""def strcounter(data):
    for sym in set(data):
        count = 0
        for el in data:
            if sym == el:
                count += 1
        print(sym, count)

strcounter("aaabbbccdd")"""




"""family = {}
print(family)
family["dad"] = 2
print(family)
family["mom"] = 10
print(family)
family["child"] = 1
print(family)
family["child"] = family.get("child") + 1
print(family)"""



def strcounter(data):
    counter = {}
    for sym in data:
        counter[sym] = counter.get(sym, 0) + 1
    for sym, count in counter.items():
        print(sym, count)

strcounter("aaabbbccdd")
