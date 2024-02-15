#!/usr/bin/python3
""" 15-main """
from models.square import Square

if __name__ == "__main__":

    Square.save_to_file([Square(1)])

    with open("Square.json", "r") as file:
        print(file.read())