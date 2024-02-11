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
        self.assertEqual(r1.id, 7)
        self.assertEqual(r2.id, 8)
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

    def test_display(self):
        """Test the display method"""
        r9 = Rectangle(4, 6)
        rect9 = "####\n####\n####\n####\n####\n####"
        self.assertEqual(r9.display(), rect9)

        r12 = Rectangle(2, 3, 2, 2)
        rect12 = "\n\n  ##\n  ##\n  ##"
        self.assertEqual(r12.display(), rect12)

    def test_str(self):
        r10 = Rectangle(4, 6, 2, 1, 12)
        test_str = "[Rectangle] (12) 2/1 - 4/6"
        self.assertEqual(r10.__str__(), test_str)

        r11 = Rectangle(5, 5)
        test_str = "[Rectangle] (9) 0/0 - 5/5"
        self.assertEqual(r11.__str__(), test_str)

    def test_update(self):
        r13 = Rectangle(10, 10, 10, 10)
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

        """Update with an unwanted value"""
        self.assertRaises(ValueError, lambda : r13.update(89, -2))
        self.assertRaises(ValueError, lambda : r13.update(89, 2, -3))
        self.assertRaises(ValueError, lambda : r13.update(89, 0))
        self.assertRaises(ValueError, lambda : r13.update(89, 2, 0))
        self.assertRaises(ValueError, lambda : r13.update(89, 2, 3, -4, 5))
        self.assertRaises(ValueError, lambda : r13.update(89, -2, 3, 4, -5))

        """Update with an unwanted type"""

        """With string values"""
        self.assertRaises(TypeError, lambda : r13.update(89, "Python"))
        self.assertRaises(TypeError, lambda : r13.update(89, 2, "*args"))
        self.assertRaises(TypeError, lambda : r13.update(89, 2, 3, "**kwargs", 5))
        self.assertRaises(TypeError, lambda : r13.update(89, -2, 3, 4, "*magic_variables"))

        """With type tuples values"""
        self.assertRaises(TypeError, lambda : r13.update(89, (9, 0)))
        self.assertRaises(TypeError, lambda : r13.update(89, 2, (9, 0)))
        self.assertRaises(TypeError, lambda : r13.update(89, 2, 3, (9, 0), 5))
        self.assertRaises(TypeError, lambda : r13.update(89, -2, 3, 4, (9, 0)))

        """With type bool values"""
        self.assertRaises(TypeError, lambda : r13.update(89, True))
        self.assertRaises(TypeError, lambda : r13.update(89, 2, False))
        self.assertRaises(TypeError, lambda : r13.update(89, 2, 3, True, 5))
        self.assertRaises(TypeError, lambda : r13.update(89, -2, 3, 4, False))

        """With type list values"""
        self.assertRaises(TypeError, lambda : r13.update(89, [9, 0]))
        self.assertRaises(TypeError, lambda : r13.update(89, 2, [9, 0]))
        self.assertRaises(TypeError, lambda : r13.update(89, 2, 3, [9, 0], 5))
        self.assertRaises(TypeError, lambda : r13.update(89, -2, 3, 4, [9, 0]))

        """With type dict values"""
        self.assertRaises(TypeError, lambda : r13.update(89, {"width": 8}))
        self.assertRaises(TypeError, lambda : r13.update(89, 2, {"height": 8}))
        self.assertRaises(TypeError, lambda : r13.update(89, 2, 3, {"x": 8}, 5))
        self.assertRaises(TypeError, lambda : r13.update(89, -2, 3, 4, {"y": 8}))



