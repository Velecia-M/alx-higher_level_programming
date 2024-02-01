#!/usr/bin/python3
def uniq_add(my_list=[]):
    add_ints = set(my_list)
    x = 0
    for i in add_ints:
        x += i
    return (x)
