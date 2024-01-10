#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string == None or type(roman_string) != str:
        return (0)

    my_dict = {'I': 1, 'V': 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}

    str_len = len(roman_string)

    i = 0
    num = 0

    while (i < str_len - 1):
        num1 = my_dict[roman_string[i]]
        num2 = my_dict[roman_string[i + 1]]
        if num1 >= num2:
            num += num1
        else:
            num -= num1

        i += 1
    num += my_dict[roman_string[i]]


    return (num)
