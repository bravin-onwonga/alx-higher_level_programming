#!/usr/bin/python3
"""Unittest for models.sqquaremodule"""
import unittest
from models.square import Square
import os, json


class TestSquare(unittest.TestCase):
    def test_init(self):
        """test the instantiation method for square obj"""
        s1 = Square(5)
        self.assertEqual(s1.width, 5)
        s2 = Square(1, 2)
        self.assertEqual(s1.id, s2.id -1)
        s3 = Square(1, 2, 3)
        self.assertEqual(s3.height, 1)
        s4 = Square(3, 1, 3, 20)
        self.assertEqual(s4.id, 20)

    def test_size_type(self):
        """Test with not-int values"""
        self.assertRaises(TypeError, lambda: Square("1"))
        self.assertRaises(TypeError, lambda: Square({1, 2}))
        self.assertRaises(TypeError, lambda: Square(True))
        self.assertRaises(TypeError, lambda: Square([1, 2]))
        self.assertRaises(TypeError, lambda: Square((1,)))

        """Test x and y for square instance"""
        self.assertRaises(TypeError, lambda: Square(1, "Python"))
        self.assertRaises(TypeError, lambda: Square(1, 2, "is"))
        self.assertRaises(TypeError, lambda: Square(1, {1, 2}))
        self.assertRaises(TypeError, lambda: Square(1, 2, ["cool"]))
        self.assertRaises(TypeError, lambda: Square(1, 2, (3,)))

    def test_values(self):
        """Test for wrong values of type int"""
        self.assertRaises(ValueError, lambda: Square(0))
        self.assertRaises(ValueError, lambda: Square(-1))
        self.assertRaises(ValueError, lambda: Square(1, -2))
        self.assertRaises(ValueError, lambda: Square(1, 2, -7))

    def test_str(self):
        """Test __str__ method"""
        s4 = Square(3, 1, 3, 20)
        self.assertEqual(s4.__str__(), "[Square] (20) 1/3 - 3")

    def test_size_setter(self):
        s7 = Square(5)
        s7.size = 10
        self.assertEqual(s7.width, 10)
        self.assertEqual(s7.height, 10)

    def test_update(self):
        """Test for update attrs method"""
        s5 = Square(5)
        s5.update(10)
        self.assertEqual(s5.id, 10)

        s5.update(1, 2, 3, 4)
        self.assertEqual(s5.__str__(), "[Square] (1) 3/4 - 2")

        s5.update(size=7, y=1)
        self.assertEqual(s5.width, 7)
        self.assertEqual(s5.y, 1)
        self.assertEqual(s5.__str__(), "[Square] (1) 3/1 - 7")

    def test_to_dictionary(self):
        """Test the dict rep of a square instance"""
        s6 = Square(9, 2, 3, 17)
        my_dict = s6.to_dictionary()
        res_dict = {'id': 17, 'x': 2, 'size': 9, 'y': 3}
        self.assertEqual(my_dict, res_dict)

    def test_create(self):
        """Tests the create method in the base class"""
        sq41 = Square.create(**{ 'id': 89 })
        self.assertEqual(sq41.__str__(), "[Square] (89) 0/0 - 1")

        sq42 = Square.create(**{ 'id': 89, 'size': 1 })
        self.assertEqual(sq42.__str__(), "[Square] (89) 0/0 - 1")

        sq43 = Square.create(**{ 'id': 89, 'size': 1, 'x': 2 })
        self.assertEqual(sq43.__str__(), "[Square] (89) 2/0 - 1")

        sq44 = Square.create(**{ 'id': 89, 'size': 1, 'x': 2, 'y': 3 })
        self.assertEqual(sq44.__str__(), "[Square] (89) 2/3 - 1")

    def test_save_to_file(self):
        """Test for save_to_file method"""
        sq25 = Square(3, 2, 1, 41)
        sq26 = Square(4, 5, 2, 17)

        Square.save_to_file([sq25, sq26])

        self.assertTrue(os.path.exists("Square.json"))

        with open("Square.json", 'r') as my_file:
            data = my_file.read()

        excepted_data = ('[{"id": 41, "x": 2, "size": 3, "y": 1}, '
                         '{"id": 17, "x": 5, "size": 4, "y": 2}]')

        self.assertEqual(data, excepted_data)

        Square.save_to_file([Square(1)])

        self.assertTrue(os.path.exists("Square.json"))

        with open("Square.json", 'r') as my_file:
            data = my_file.read()

        sq_dict = json.loads(data)

        self.assertEqual(sq_dict[0]['size'], 1)

        Square.save_to_file([Square(1, 2)])

        self.assertTrue(os.path.exists("Square.json"))

        with open("Square.json", 'r') as my_file:
            data = my_file.read()

        sq_dict = json.loads(data)
        self.assertEqual(sq_dict[0]['x'], 2)

        Square.save_to_file([Square(1, 2, 4)])

        self.assertTrue(os.path.exists("Square.json"))

        with open("Square.json", 'r') as my_file:
            data = my_file.read()

        sq_dict = json.loads(data)
        self.assertEqual(sq_dict[0]['y'], 4)

    def test_save_to_file_None(self):
        """Test for None"""
        Square.save_to_file(None)

        self.assertTrue(os.path.exists("Square.json"))

        with open("Square.json", 'r') as my_file:
            data = my_file.read()

        self.assertEqual(data, "[]")

    def test_save_to_file_empty(self):
        """Test for empty dict"""
        Square.save_to_file([])

        self.assertTrue(os.path.exists("Square.json"))

        with open("Square.json", 'r') as my_file:
            data = my_file.read()

        self.assertEqual(data, "[]")

        os.remove("Square.json")

        """Test for no parames"""
        with self.assertRaises(TypeError):
            Square.save_to_file()

    def test_load_from_file(self):
        """Test the load_from_file method"""

        if (os.path.exists("Square.json")):
            os.remove("Square.json")

        res = Square.load_from_file()

        self.assertEqual(res, [])

        s1 = Square(5)
        s2 = Square(7, 9, 1)
        list_squares_input = [s1, s2]

        Square.save_to_file(list_squares_input)

        list_squares_output = Square.load_from_file()

        for prev_square, file_square in zip(list_squares_input, list_squares_output):
            self.assertEqual(prev_square.to_dictionary(), file_square.to_dictionary())
            self.assertFalse(prev_square.to_dictionary() is file_square.to_dictionary())

if __name__ == "__main__":
    unittest.main()
