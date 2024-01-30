#!/usr/bin/python3
"""
prints a text with 2 new lines after each of these characters: ., ? and :
"""


def text_indentation(text):
    """
    Raises:
        TypeError: text is not a string
    """
    if not isinstance(text, str):
        raise TypeError('text must be a string')

    chars = ['.', '?', ':']
    len_txt = len(text)
    i = 0

    while (i < len_txt):
        c = text[i]
        if c not in chars:
            if c == ' ' and text[i - 1] not in chars:
                print(c, end="")
            if c != ' ':
                print(c, end="")
        else:
            print(c)
            print()
        i += 1
