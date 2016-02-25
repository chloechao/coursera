#!/usr/bin/python
import random

def category(group, group_num):
    list_ = []
    if group_num > len(group):
        return

    entery = int(len(group) / int(group_num))
    enteries = [ entery for entery_num in range(group_num - 1) ]
    if len(group) % int(group_num) != 0:
        enteries.append(entery + 1)

    while len(group) > 0:
        for item in enteries:
            new_group = []
            for num in range(item):
                new_group.append(group.pop(random.randrange(len(group))))
            list_.append(tuple(new_group))
    return list_

group = ["A", "B", "C", "D", "E", "F", "G"]
group_num = 3
print category(group, group_num)
