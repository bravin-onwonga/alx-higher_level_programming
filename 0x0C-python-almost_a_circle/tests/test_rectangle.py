#!/usr/bin/python3
"""Unittest for models.rectangle module"""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def test_init(self):
        """Test for id attribute of parent class"""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 3)
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.id, 4)
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)

    def test_types(self):
        self.assertRaises(TypeError, lambda: Rectangle("Python", 2, 0, 0))
        self.assertRaises(TypeError, lambda: Rectangle(10, "Python", 0, 0))
        self.assertRaises(TypeError, lambda: Rectangle(10, 2, "Python", 0))
        self.assertRaises(TypeError, lambda: Rectangle(10, 2, 0, "Python"))

    def test_values(self):
        self.assertRaises(ValueError, lambda: Rectangle(0, 2, 0, 0))
        self.assertRaises(ValueError, lambda: Rectangle(10, 0, 0, 0))
        self.assertRaises(ValueError, lambda: Rectangle(10, 2, -2, 0))
        self.assertRaises(ValueError, lambda: Rectangle(10, 2, 0, -2))

if __name__ == '__main__':
    unittest.main()
