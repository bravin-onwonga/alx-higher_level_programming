#!/usr/bin/python3
"""Unittest for models.base module"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):

    def test_id(self):
        """Test when no value is passed"""
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b1 = Base(9)
        self.assertEqual(b1.id, 9)

    def test_nb_objects(self):
        """Test for when value is passed"""
        b2 = Base()
        self.assertEqual(b2.id, 2)
