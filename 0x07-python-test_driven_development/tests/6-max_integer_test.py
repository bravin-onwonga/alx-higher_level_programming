#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

"""
Test class to test my function
"""


class TestMaxInteger(unittest.TestCase):
    def test_max_integer(self):
        """Test when a proper list is given"""
        self.assertAlmostEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertAlmostEqual(max_integer([]), None)

    def test_values(self):
        """Value errors are raised when necessary"""
        self.assertRaises(TypeError, max_integer, type(str))
        self.assertRaises(TypeError, max_integer, type(None))
        self.assertRaises(TypeError, max_integer, True)
        self.assertRaises(TypeError, max_integer, float)
