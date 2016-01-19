#!/usr/bin/python

def merge(line):
    """
        Function that merges a single row or column in 2048.
    """
    new_line = []
    #removed all zero item
    new_line += [ item for item in line if item != 0 ]

    #replaced with a tile of twice the value
    index = 0
    while index < len(new_line)-1:
        if new_line[index] == new_line[index+1]:
            new_line[index] = int(new_line[index]) * 2
            new_line.pop(index+1)
        index += 1

    #appended zero to the new list
    new_line += [ 0 for i in range(len(new_line),len(line)) ]
    return new_line

list0=[2, 0, 2, 4]
list1=[0, 0, 2, 2]
list2=[2, 2, 0, 0]
list3=[2, 2, 2, 2, 2]
list4=[8, 16, 16, 8]

print merge(list0)
print merge(list1)
print merge(list2)
print merge(list3)
print merge(list4)
