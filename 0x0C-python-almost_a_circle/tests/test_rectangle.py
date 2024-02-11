#!/usr/bin/python3
"""Unittest for models.rectangle module"""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def test_init(self):
        """Test for id attribute of parent class"""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 5)
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.id, 6)
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)

    def test_types(self):
        """Test for types of values given"""
        self.assertRaises(TypeError, lambda: Rectangle("Python", 2, 0, 0))
        self.assertRaises(TypeError, lambda: Rectangle(10, "Python", 0, 0))
        self.assertRaises(TypeError, lambda: Rectangle(10, 2, "Python", 0))
        self.assertRaises(TypeError, lambda: Rectangle(10, 2, 0, "Python"))

    def test_values(self):
        """Test for Values entered"""
        self.assertRaises(ValueError, lambda: Rectangle(0, 2, 0, 0))
        self.assertRaises(ValueError, lambda: Rectangle(10, 0, 0, 0))
        self.assertRaises(ValueError, lambda: Rectangle(-1, 2, 0, 0))
        self.assertRaises(ValueError, lambda: Rectangle(10, -1, 0, 0))
        self.assertRaises(ValueError, lambda: Rectangle(10, 2, -2, 0))
        self.assertRaises(ValueError, lambda: Rectangle(10, 2, 0, -2))

    def test_area(self):
        """Test for area method"""
        r6 = Rectangle(10, 2)
        self.assertEqual(r6.area(), 20)
        r7 = Rectangle(3, 2)
        self.assertEqual(r7.area(), 6)
        r8 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r8.area(), 56)
