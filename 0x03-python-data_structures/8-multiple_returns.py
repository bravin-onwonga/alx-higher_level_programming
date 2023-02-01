#!/usr/bin/python3

def multiple_returns(sentence):
    if sentence == None:
        tuple_l = (None,)
    else:
        len_s = len(sentence)
        first_ch = sentence[0]
        tuple_l = (len_s, first_ch)
    return tuple_l
