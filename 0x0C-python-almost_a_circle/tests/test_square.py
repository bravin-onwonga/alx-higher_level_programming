#!/usr/bin/python3
"""Unittest for models.sqquaremodule"""
import unittest
from models.square import Square
from models.rectangle import Rectangle


class TestSquare(unittest.TestCase):
    def test_init(self):
        """test the instantiation method for square obj"""
        s1 = Square(5)
        self.assertEqual(s1.width, 5)
        s2 = Square(3, 1, 3, 20)
        self.assertEqual(s2.id, 20)

    def test_size_type(self):
        """Test with not-int values"""
        self.assertRaises(TypeError, lambda: Square("School"))
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
