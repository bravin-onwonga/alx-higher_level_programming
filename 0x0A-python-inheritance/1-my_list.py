#!/usr/bin/python3
"""A class that inherits from list
"""


class MyList(list):
    """A class that inherits from class list and sorts the list
    """
    def __init__(self):
        super().__init__(self)
        self.my_lst = self

    def print_sorted(self):
        """Prints a sorted list
        """
        print(sorted(self.my_lst))
