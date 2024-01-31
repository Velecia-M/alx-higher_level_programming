#!/usr/bin/python3
def multiple_returns(sentence):
    sen_to_tuple = ()
    x = len(sentence)
    if x == 0:
        sen_to_tuple = 0, "None"
    else:
        sen_to_tuple = (x, sentence[0])
        return sen_to_tuple
