#!/usr/bin/python3
"""Module models.base"""


class Base:
    """Base class inherited by other classes

    Attr:
        nb_objects - private class attribute
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Instantiates attribute for objects

        Attribute:
            id - integer attribute for id of object
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries

        Params:
            list_dictionaries - a list of dictionaries containing attr
        """
        import json
        if not list_dictionaries or len([list_dictionaries]) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file

        Parameters:
            list_objs - a list of instances of class Rectangle or Square
        """
        if list_objs is None:
            list_objs = []
        len_list_objs = len(list_objs)
        new_list = []
        new_dict = {}

        i = 0
        while (i < len_list_objs):
            new_dict = list_objs[i].to_dictionary()
            new_list.append(new_dict)
            i += 1

        txt = cls.to_json_string(new_list)

        if cls.__name__ == "Square":
            with open("Square.json", 'w') as my_file:
                my_file.write(txt)
        if cls.__name__ == "Rectangle":
            with open("Rectangle.json", 'w') as my_file:
                my_file.write(txt)

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string

        Args:
            json_string - string rep of a list
        """
        import json
        if not json_string:
            json_string = "[]"
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set

        Args:
            dictionary - contains the attr to for the new instance
        """
        width = 1
        height = 2
        id = None
        x = 0
        y = 0
        size = 1

        if cls.__name__ == "Square":
            square_obj = cls(size, x=x, y=y, id=id)
        if cls.__name__ == "Rectangle":
            rect = cls(width=width, height=height, x=x, y=y, id=id)

        if cls.__name__ == "Square":
            square_obj.update(**dictionary)
            return square_obj

        if cls.__name__ == "Rectangle":
            rect.update(**dictionary)
            return rect

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Writes the csv string representation of list_objs to a file

        Parameters:
            list_objs - a list of instances of class Rectangle or Square
        """
        if list_objs is None:
            list_objs = []
        len_list_objs = len(list_objs)
        new_list = []
        new_dict = {}

        i = 0
        while (i < len_list_objs):
            new_dict = list_objs[i].to_dictionary()
            new_list.append(new_dict)
            i += 1

        k = 0
        text = ""
        while (k < i):
            curr_dict = new_list[k]
            temp_list = ['id', 'size', 'width', 'height', 'x', 'y']
            for key in temp_list:
                if key in curr_dict:
                    text += str(curr_dict[key])
                    if temp_list.index(key) != 5:
                        text += ", "
                    else:
                        text += '\n'
            k += 1

        if cls.__name__ == "Square":
            with open("Square.csv", 'w') as my_file:
                my_file.write(text)
        if cls.__name__ == "Rectangle":
            with open("Rectangle.csv", 'w') as my_file:
                my_file.write(text)

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""
        if cls.__name__ == "Rectangle":
            try:
                with open("Rectangle.json", 'r') as my_file:
                    txt = ""
                    for line in my_file:
                        txt += line
                    my_lst = cls.from_json_string(txt)
                    i = 0
                    new_lst = []
                    while (i < len(my_lst)):
                        new_lst.append(cls.create(**my_lst[i]))
                        i += 1
                    return (new_lst)
            except FileNotFoundError:
                return []

        if cls.__name__ == "Square":
            try:
                with open("Square.json", 'r') as my_file:
                    txt = ""
                    for line in my_file:
                        txt += line
                    my_lst = cls.from_json_string(txt)
                    i = 0
                    new_lst = []
                    while (i < len(my_lst)):
                        new_lst.append(cls.create(**my_lst[i]))
                        i += 1
                    return (new_lst)
            except FileNotFoundError:
                return []

    @classmethod
    def load_from_file_csv(cls):
        """Returns a list of instances creates from a csv file
        otherwise returns an empty list"""
        if cls.__name__ == "Rectangle":
            try:
                with open("Rectangle.csv", 'r') as my_file:
                    my_lst = []
                    for line in my_file:
                        my_lst.append(line.split(","))

                    new_lst = []
                    lst_keys = ['id', 'width', 'height', 'x', 'y']
                    i = 0
                    while (i < len(my_lst)):
                        new_dict = {}
                        for n in range(0, len(lst_keys)):
                            new_dict[lst_keys[n]] = int(my_lst[i][n])
                        new_lst.append(cls.create(**new_dict))
                        i += 1
                    return (new_lst)
            except FileNotFoundError:
                return []

        if cls.__name__ == "Square":
            try:
                with open("Square.csv", 'r') as my_file:
                    my_lst = []
                    for line in my_file:
                        my_lst.append(line.split(","))

                    new_lst = []
                    lst_keys = ['id', 'size', 'x', 'y']
                    i = 0
                    while (i < len(my_lst)):
                        new_dict = {}
                        for n in range(0, len(lst_keys)):
                            new_dict[lst_keys[n]] = int(my_lst[i][n])
                        new_lst.append(cls.create(**new_dict))
                        i += 1
                    return (new_lst)
            except FileNotFoundError:
                return []
