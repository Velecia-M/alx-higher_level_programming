#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(x) >= 97 and ord(x) <= 122:
            i = chr(ord(i) - 32)
        print("{}".format(i), end='')
    print()
