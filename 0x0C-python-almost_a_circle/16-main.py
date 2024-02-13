#!/usr/bin/python3
""" 16-main """
from models.rectangle import Rectangle
from models.base import Base

if __name__ == "__main__":

    list_input = [ { 'id': 12 }]
    json_list_input = Rectangle.to_json_string(list_input)
    list_output = Rectangle.from_json_string(json_list_input)
    print(Base.from_json_string('[{ "id": 89 }]'))
    print("[{}] {}".format(type(list_input), list_input))
    print("[{}] {}".format(type(json_list_input), json_list_input))
    print("[{}] {}".format(type(list_output), list_output))
