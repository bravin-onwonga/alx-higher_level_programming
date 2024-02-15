#!/usr/bin/python3
""" 15-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

    rect45 = Rectangle(1, 2)
    Rectangle.save_to_file([rect45])

    with open("Rectangle.json", "r") as file:
        print(file.read())