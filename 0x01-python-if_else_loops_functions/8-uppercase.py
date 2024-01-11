#!/usr/bin/python3
def uppercase(str):
    for i in str:
        x = i
        if ord(x) >= 65 and ord(x) <= 90:
            x = chr(ord(i) - 32)
        print("{}".format(i), end='')
    print()
