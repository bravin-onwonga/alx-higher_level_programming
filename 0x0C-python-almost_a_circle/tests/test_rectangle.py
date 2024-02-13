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
        r9 = Rectangle(4, 6)
        rect9 = "####\n####\n####\n####\n####\n####"
        self.assertEqual(r9.display(), rect9)

        r12 = Rectangle(2, 3, 2, 2)
        rect12 = "\n\n  ##\n  ##\n  ##"
        self.assertEqual(r12.display(), rect12)

        """Test for display method without values
        self.assertRaises(TypeError, Rectangle.display())
        self.assertRaises(TypeError, Rectangle.display(6, ))
        self.assertRaises(TypeError, Rectangle.display())"""

    def test_str(self):
        r10 = Rectangle(4, 6, 2, 1, 12)
        test_str = "[Rectangle] (12) 2/1 - 4/6"
        self.assertEqual(r10.__str__(), test_str)

        r11 = Rectangle(5, 5)
        rect_id = r11.id
        test_str = "[Rectangle] ({}) 0/0 - 5/5".format(rect_id)
        self.assertEqual(r11.__str__(), test_str)

    def test_update(self):
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

    def test_create(self):
        """Tests the create method in the base class"""
        r20= Rectangle.create(**{ 'id': 89 })
        self.assertEqual(r20.__str__(), "[Rectangle] (89) 3/4 - 1/2")
        r21_dictionary = r1.to_dictionary()
        r22 = Rectangle.create(**r1_dictionary)

if __name__ == "__main__":
    unittest.main()
