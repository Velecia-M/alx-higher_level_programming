#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    x = my_list.copy()
    y = len(x)
    if idx < 0:
        return x
    elif idx >= y:
        return x
    else:
        x[idx] = element
        return x
