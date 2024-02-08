#!/usr/bin/python3
"""A class that inherits from list
"""


class MyList(list):
    def print_sorted(self):
        """Prints a sorted list
        """
        print(sorted(self))
