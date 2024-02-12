#!/usr/bin/python3
"""Module models.base"""


class Base:
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
        """Returns the JSON string representation of list_dictionaries"""
        import json
        if not list_dictionaries or len(list_dictionaries) == 0:
            return "[]"
        my_lst = ["x", "width", "id", "height", "y"]
        my_dict = list_dictionaries[0]
        new_dict = {}
        for i in range(0, len(my_lst)):
            key = my_lst[i]
            new_dict[key] = my_dict[key]
        return json.dumps([new_dict])

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file"""
        import json
        txt = "["
        len_list_objs = len(list_objs)

        i = 0
        while(i < len_list_objs):
            content = list_objs[i].to_dictionary()

            my_lst = ["y", "x", "id", "width", "height"]
            new_dict = {}
            for n in range(0, len(my_lst)):
                key = my_lst[n]
                new_dict[key] = content[key]

            hold_content = json.dumps(new_dict)

            txt += hold_content
            if i != (len_list_objs - 1):
                txt += ", "
            else:
                txt += "]"
            i += 1
            print(i)

        with open("Rectangle.json", 'w') as my_file:
            my_file.write(txt)
