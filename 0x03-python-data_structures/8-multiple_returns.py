#!/usr/bin/python3
def multiple_returns(sentence):
    x = len(sentence)
    sen_to_tuple = ()
    y = sentence[0]
    if x == 0:
        return None
    else:
        sen_to_tuple = (x, y)
        return sen_to_tuple
