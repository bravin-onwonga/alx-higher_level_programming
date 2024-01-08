#!/usr/bin/python3
def multiple_returns(sentence):
    len_str = len(sentence)

    if len_str > 0:
        first_char = sentence[0]
    else:
        first_char = None

    return len_str, first_char

