#!/usr/bin/python3
"""Unittest for models.rectangle module"""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def test_init(self):
        """Test for id attribute of parent class"""
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r1.id, r2.id - 1)
        self.assertEqual(r3.id, 12)

    def test_types(self):
        """Test for types of values given"""
        self.assertRaises(TypeError, lambda: Rectangle("10", 2, 0, 0))
        self.assertRaises(TypeError, lambda: Rectangle(10, "2", 0, 0))
        self.assertRaises(TypeError, lambda: Rectangle(10, 2, "0", 0))
        self.assertRaises(TypeError, lambda: Rectangle(10, 2, 0, "4"))

        """Test for when attr value is None"""
        self.assertRaises(TypeError, lambda: Rectangle(None, 2, 0, 0))
        self.assertRaises(TypeError, lambda: Rectangle(10, None, 0, 0))
        self.assertRaises(TypeError, lambda: Rectangle(10, 2, None, 0))
        self.assertRaises(TypeError, lambda: Rectangle(10, 2, 0, None))

        """Test for when attr value is type bool"""
        self.assertRaises(TypeError, lambda: Rectangle(False, 2, 0, 0))
        self.assertRaises(TypeError, lambda: Rectangle(10, True, 0, 0))
        self.assertRaises(TypeError, lambda: Rectangle(10, 2, False, 0))
        self.assertRaises(TypeError, lambda: Rectangle(10, 2, 0, True))

        """Test for when attr value is type list"""
        self.assertRaises(TypeError, lambda: Rectangle([2, 3], 2, 0, 0))
        self.assertRaises(TypeError, lambda: Rectangle(10, [2, 3], 0, 0))
        self.assertRaises(TypeError, lambda: Rectangle(10, 2, [2, 3], 0))
        self.assertRaises(TypeError, lambda: Rectangle(10, 2, 0, [2, 3]))

        """Test for when attr value is type dict"""
        self.assertRaises(TypeError, lambda: Rectangle({2, 3}, 2, 0, 0))
        self.assertRaises(TypeError, lambda: Rectangle(10, {2, 3}, 0, 0))
        self.assertRaises(TypeError, lambda: Rectangle(10, 2, {2, 3}, 0))
        self.assertRaises(TypeError, lambda: Rectangle(10, 2, 0, {2, 3}))

    def test_values(self):
        """Test zero and -ve values entered for width and height"""
        self.assertRaises(ValueError, lambda: Rectangle(0, 2, 0, 0))
        self.assertRaises(ValueError, lambda: Rectangle(10, 0, 0, 0))
        self.assertRaises(ValueError, lambda: Rectangle(-1, 2, 0, 0))
        self.assertRaises(ValueError, lambda: Rectangle(10, -1, 0, 0))

        """Test -ve values entered for x and y"""
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

    def test_display(self):
        """Test the display method"""
        r20 = Rectangle(3, 2)

        import io
        from contextlib import redirect_stdout
        with io.StringIO() as captured_output:
            with redirect_stdout(captured_output):
                r20.display()

            printed_output = captured_output.getvalue()

        expected_display = (
            "###\n"
            "###\n"
        )

        self.assertEqual(printed_output, expected_display)

        """Test without y"""
        r21 = Rectangle(3, 2, 1)
        with io.StringIO() as captured_output:
            with redirect_stdout(captured_output):
                r21.display()

            r21_output = captured_output.getvalue()

        r21_expected_display = (
            " ###\n"
            " ###\n"
        )

        self.assertEqual(r21_output, r21_expected_display)

        """Test with x and y"""
        r22 = Rectangle(3, 2, 1, 2)
        with io.StringIO() as captured_output:
            with redirect_stdout(captured_output):
                r22.display()

            r22_output = captured_output.getvalue()

        r22_expected_display = (
            "\n"
            "\n"
            " ###\n"
            " ###\n"
        )

        self.assertEqual(r22_output, r22_expected_display)

    def test_str(self):
        """Test the __str__ method"""
        r10 = Rectangle(4, 6, 2, 1, 12)
        test_str = "[Rectangle] (12) 2/1 - 4/6"
        self.assertEqual(r10.__str__(), test_str)

        r11 = Rectangle(5, 5)
        rect_id = r11.id
        test_str = "[Rectangle] ({}) 0/0 - 5/5".format(rect_id)
        self.assertEqual(r11.__str__(), test_str)

    def test_update(self):
        """Test the update method"""
        r13 = Rectangle(10, 10, 10, 10)

        """Testing *args"""
        r13.update(89)
        self.assertEqual(r13.__str__(), "[Rectangle] (89) 10/10 - 10/10")

        r13.update(89, 2)
        self.assertEqual(r13.__str__(), "[Rectangle] (89) 10/10 - 2/10")

        r13.update(89, 2, 3)
        self.assertEqual(r13.__str__(), "[Rectangle] (89) 10/10 - 2/3")

        r13.update(89, 2, 3, 4)
        self.assertEqual(r13.__str__(), "[Rectangle] (89) 4/10 - 2/3")

        r13.update(89, 2, 3, 4, 5)
        self.assertEqual(r13.__str__(), "[Rectangle] (89) 4/5 - 2/3")

        """Testing *kwargs"""
        r13.update(**{ 'id': 99 })
        self.assertEqual(r13.__str__(), "[Rectangle] (99) 4/5 - 2/3")

        r13.update(**{ 'id': 89, 'width': 8 })
        self.assertEqual(r13.__str__(), "[Rectangle] (89) 4/5 - 8/3")

        r13.update(**{ 'id': 89, 'width': 1, 'height': 2 })
        self.assertEqual(r13.__str__(), "[Rectangle] (89) 4/5 - 1/2")

        r13.update(**{ 'id': 89, 'width': 1, 'height': 2, 'x': 3 })
        self.assertEqual(r13.__str__(), "[Rectangle] (89) 3/5 - 1/2")

        r13.update(**{ 'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4 })
        self.assertEqual(r13.__str__(), "[Rectangle] (89) 3/4 - 1/2")


        """Update with an unwanted value"""
        self.assertRaises(ValueError, lambda: r13.update(89, -2))
        self.assertRaises(ValueError, lambda: r13.update(89, 2, -3))
        self.assertRaises(ValueError, lambda: r13.update(89, 0))
        self.assertRaises(ValueError, lambda: r13.update(89, 2, 0))
        self.assertRaises(ValueError, lambda: r13.update(89, 2, 3, -4, 5))
        self.assertRaises(ValueError, lambda: r13.update(89, -2, 3, 4, -5))

        """Update with an unwanted type"""

        """With string values"""
        self.assertRaises(TypeError, lambda: r13.update(89, "Python"))
        self.assertRaises(TypeError, lambda: r13.update(89, 2, "*args"))
        self.assertRaises(TypeError, lambda: r13.update(89, 2, 3, "is", 5))
        self.assertRaises(TypeError, lambda: r13.update(89, 2, 3, 4, "magic"))

        """With type tuples values"""
        self.assertRaises(TypeError, lambda: r13.update(89, (9, 0)))
        self.assertRaises(TypeError, lambda: r13.update(89, 2, (9, 0)))
        self.assertRaises(TypeError, lambda: r13.update(89, 2, 3, (9, 0), 5))
        self.assertRaises(TypeError, lambda: r13.update(89, 2, 3, 4, (9, 0)))

        """With type bool values"""
        self.assertRaises(TypeError, lambda: r13.update(89, True))
        self.assertRaises(TypeError, lambda: r13.update(89, 2, False))
        self.assertRaises(TypeError, lambda: r13.update(89, 2, 3, True, 5))
        self.assertRaises(TypeError, lambda: r13.update(89, 2, 3, 4, False))

        """With type list values"""
        self.assertRaises(TypeError, lambda: r13.update(89, [9, 0]))
        self.assertRaises(TypeError, lambda: r13.update(89, 2, [9, 0]))
        self.assertRaises(TypeError, lambda: r13.update(89, 2, 3, [9, 0], 5))
        self.assertRaises(TypeError, lambda: r13.update(89, 2, 3, 4, [9, 0]))

        """With type dict values"""
        self.assertRaises(TypeError, lambda: r13.update(89, {"width": 8}))
        self.assertRaises(TypeError, lambda: r13.update(89, 2, {"height": 8}))
        self.assertRaises(TypeError, lambda: r13.update(9, 2, 3, {"x": 8}))
        self.assertRaises(TypeError, lambda: r13.update(9, 2, 3, 4, {'y': 8}))

    def test_to_dictionary(self):
        """Test for to_dictionary method that returns a dict rep of an obj
        """
        r14 = Rectangle(4, 6, 2, 1, 12)
        my_dict = r14.to_dictionary()
        res = {'x': 2, 'y': 1, 'id': 12, 'height': 6, "width": 4}
        self.assertEqual(my_dict, res)

    def test_create(self):
        """Tests the create method in the base class"""
        r15 = Rectangle.create(**{ 'id': 89 })
        self.assertEqual(r15.__str__(), "[Rectangle] (89) 0/0 - 1/2")

        r16 = Rectangle.create(**{ 'id': 89, 'width': 1 })
        self.assertEqual(r16.__str__(), "[Rectangle] (89) 0/0 - 1/2")

        r17 = Rectangle.create(**{ 'id': 89, 'width': 1, 'height': 2 })
        self.assertEqual(r17.__str__(), "[Rectangle] (89) 0/0 - 1/2")

        r18 = Rectangle.create(**{ 'id': 89, 'width': 1, 'height': 2, 'x': 3 })
        self.assertEqual(r18.__str__(), "[Rectangle] (89) 3/0 - 1/2")

        r19 = Rectangle.create(**{ 'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4 })
        self.assertEqual(r19.__str__(), "[Rectangle] (89) 3/4 - 1/2")

    def test_save_to_file(self):
        """Test for save_to_file method"""
        import os

        rect25 = Rectangle(3, 2, 1, 2, 41)
        rect26 = Rectangle(4, 5, 2, 6, 17)

        Rectangle.save_to_file([rect25, rect26])

        self.assertTrue(os.path.exists("Rectangle.json"))

        with open("Rectangle.json", 'r') as my_file:
            data = my_file.read()

        excepted_data = ('[{"x": 1, "y": 2, "id": 41, "height": 2, "width": 3}, '
                         '{"x": 2, "y": 6, "id": 17, "height": 5, "width": 4}]')

        self.assertEqual(data, excepted_data)

        """Test for None"""
        Rectangle.save_to_file(None)

        self.assertTrue(os.path.exists("Rectangle.json"))

        with open("Rectangle.json", 'r') as my_file:
            data = my_file.read()

        self.assertEqual(data, "[]")

        """Test with only width and height"""
        rect45 = Rectangle(1, 2)
        Rectangle.save_to_file([rect45])

        self.assertTrue(os.path.exists("Rectangle.json"))

        with open("Rectangle.json", 'r') as my_file:
            data = my_file.read()

        rect45_data = f'[{{"x": 0, "y": 0, "id": {rect45.id}, "height": 2, "width": 1}}]'

        self.assertEqual(data, rect45_data)

        """Test for empty dict"""
        Rectangle.save_to_file([])

        self.assertTrue(os.path.exists("Rectangle.json"))

        with open("Rectangle.json", 'r') as my_file:
            data = my_file.read()

        self.assertEqual(data, "[]")

    def test_load_from_file(self):
        """Test the load_from_file method"""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]

        Rectangle.save_to_file(list_rectangles_input)

        list_rectangles_output  = Rectangle.load_from_file()

        for prev_rect, file_rect in zip(list_rectangles_input, list_rectangles_output ):
            self.assertEqual(prev_rect.to_dictionary(), file_rect.to_dictionary())
            self.assertFalse(prev_rect.to_dictionary() is file_rect.to_dictionary())

if __name__ == "__main__":
    unittest.main()
