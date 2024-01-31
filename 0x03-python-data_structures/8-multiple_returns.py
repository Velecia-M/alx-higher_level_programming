#!/usr/bin/python3
def multiple_returns(sentence):
    sen_to_tuple = ()
    x = len(sentence)
    y = sentence[0]
    if x == 0:
        sen_to_tuple = 0, "None"
    else:
        sen_to_tuple = (x, y)
        return sen_to_tuple
