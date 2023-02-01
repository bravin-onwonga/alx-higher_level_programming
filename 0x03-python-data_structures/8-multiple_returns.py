#!/usr/bin/python3

def multiple_returns(sentence):
    if sentence is None:
        tuple_l = (0, None)
    else:
        len_s = len(sentence)
        first_ch = sentence[0]
        tuple_l = (len_s, first_ch)
    return tuple_l
