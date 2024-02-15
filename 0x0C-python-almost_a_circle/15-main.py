#!/usr/bin/python3
""" 15-main """
from models.square import Square

if __name__ == "__main__":

    sq25 = Square(3, 2, 1, 41)
    sq26 = Square(4, 5, 2, 17)
    Square.save_to_file([sq25, sq26])

    with open("Square.json", "r") as file:
        print(file.read())
