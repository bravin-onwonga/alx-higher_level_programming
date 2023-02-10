#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    my_new_list = []

    for x, y in zip(my_list_1, my_list_2):
        try:
            my_new_list.append(x / y)
        except ZeroDivisionError:
            print("division by 0")
            my_new_list.append(0)
        except TypeError:
            print("wrong type")
            my_new_list.append(0)
        except IndexError:
            print("out of range")
            my_new_list.append(0)
        finally:
            return my_new_list
