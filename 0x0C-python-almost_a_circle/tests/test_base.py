#!/usr/bin/python3
"""Unittest for models.base module"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):

    def test_id(self):
        """Test when no value is passed"""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)
        b3 = Base(89)
        self.assertEqual(b3.id, 89)

    def test_id_as_None(self):
        """Test when None is passed as id"""
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id, b2.id - 1)

    def test_id_as_list(self):
        """Test when id is a list"""
        self.assertEqual(Base([1, 2]).id, [1, 2])

    def test_to_json_string(self):
        """Tests to_json_string method"""
        rect1 = Rectangle(10, 7, 2, 8)
        rect1_dict = rect1.to_dictionary()
        my_str = Rectangle.to_json_string([rect1_dict])
        res_str = '[{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}]'
        self.assertEqual(len(my_str), len(res_str) + 1)

        new_str = Base.to_json_string([ { 'id': 12 }])
        self.assertEqual(new_str, '[{"id": 12}]')

        self.assertEqual(Base.to_json_string([]), '[]')
        self.assertEqual(Base.to_json_string(None), '[]')

    def test_save_to_file(self):
        """Test for save_to_file"""
        rect1 = Rectangle(10, 7, 2, 8)
        self.assertEqual(Rectangle.save_to_file([rect1]), None)

    def test_from_json_string(self):
        """Test from json to string method"""
        lst_inp = [
            {"height": 4, "width": 10, "id": 89},
            {"height": 7, "width": 1, "id": 7}
        ]
        json_lst_inp = Rectangle.to_json_string(lst_inp)
        my_list = Rectangle.from_json_string(json_lst_inp)
        res = [
            {'height': 4, 'width': 10, 'id': 89},
            {'height': 7, 'width': 1, 'id': 7}
        ]
        self.assertEqual(my_list, res)

        """Test if None is passed"""
        self.assertEqual(Base.from_json_string(None), [])

        """Test if an empty list str is passed"""
        self.assertEqual(Base.from_json_string("[]"), [])
        self.assertEqual(Base.from_json_string('[{ "id": 89 }]'), [{'id': 89}])

    def test_create(self):
        """Tests the create method"""
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertFalse(r1 is r2)
        self.assertFalse(r1 == r2)

    def test_load_from_file(self):
        """Test the load_from_file method"""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]

        Rectangle.save_to_file(list_rectangles_input)

        list_rectangles_output  = Rectangle.load_from_file()

        for prev_rect, file_rect in zip(list_rectangles_input, list_rectangles_output ):
            self.assertEqual(prev_rect.to_dictionary(), file_rect .to_dictionary())
            self.assertFalse(prev_rect.to_dictionary() is file_rect .to_dictionary())

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
