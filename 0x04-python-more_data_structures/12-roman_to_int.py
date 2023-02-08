#!/usr/bin/python3

def roman_to_int(roman_string):
    roman_dict = {"I": 1, "V": 5, "X": 10, "L": 50,
                  "C": 100, "D": 500, "M": 1000}

    len_roman = len(roman_string)
    result = 0
    i = 0

    if len_roman == 1:
        return roman_dict[roman_string]

    while (i <= len_roman):
        if roman_dict[roman_string[i]] >= roman_dict[roman_string[i + 1]]:
            result = result + roman_dict[roman_string[i]]
        else:
            result = result - roman_dict[roman_string[i]]
            i += 1

    result = result + roman_dict[roman_string[i]]
    return result
