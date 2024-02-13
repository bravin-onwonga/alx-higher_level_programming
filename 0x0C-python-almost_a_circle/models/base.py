#!/usr/bin/python3
"""Module models.base"""


class Base:
    """Base class inherited by other classes"""
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
            list_objs - a list of instances of class Rectangle
        """
        import json
        txt = "["

        len_list_objs = len([list_objs])

        i = 0
        while (i < len_list_objs):
            content = list_objs[i].to_dictionary()

            my_lst = ["y", "x", "id", "width", "height", "size"]
            new_dict = {}
            for n in range(0, len(my_lst)):
                key = my_lst[n]
                if key in content:
                    new_dict[key] = content[key]

            hold_content = json.dumps(new_dict)

            txt += hold_content
            if i != (len_list_objs - 1):
                txt += ", "
            else:
                txt += "]"
            i += 1

        if "size" in new_dict:
            with open("Square.json", 'w') as my_file:
                my_file.write(txt)
        else:
            with open("Rectangle.json", 'w') as my_file:
                my_file.write(txt)

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string

        Args:
            json_string - string rep of a list
        """
        import json
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

        if "size" in dictionary:
            square_obj = cls(size, x=x, y=y, id=id)
        else:
            rect = cls(width=width, height=height, x=x, y=y, id=id)

        if "size" in dictionary:
            square_obj.update(**dictionary)
            return square_obj

        else:
            rect.update(**dictionary)
            return rect

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
                return "[]"

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
                return "[]"
