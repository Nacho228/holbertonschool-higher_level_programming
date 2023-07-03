#!/usr/bin/python3
"""Unittest for Rectangle class"""


import unittest
import pep8
from models import rectangle
Rectangle = rectangle.Rectangle


class TestPep8(unittest.TestCase):
    """
    Test class to check PEP 8 compliance in specific files.
    """
    def test_pep8(self):
        """
        Check PEP 8 compliance in the specified files.
        """
        style = pep8.StyleGuide(quiet=False)
        errors = 0
        files = ["models/rectangle.py", "tests/test_rectangle.py"]
        errors += style.check_files(files).total_errors
        self.assertEqual(errors, 0, 'Need to fix Pep8')


class TestRectangle(unittest.TestCase):
    """
    Test class for the Rectangle class.
    """
    def test_attr_given(self):
        """
        Test for checking if attributes are assigned correctly when
        creating a Rectangle object.
        """
        r = Rectangle(6, 12, 43, 32, 655)
        self.assertTrue(r.width == 6)
        self.assertTrue(r.height == 12)
        self.assertTrue(r.x == 43)
        self.assertTrue(r.y == 32)
        self.assertTrue(r.id == 655)

    def test_default_attr(self):
        """
        Test for checking if default attributes are assigned correctly
        when creating a Rectangle object.
        """
        r = Rectangle(1, 2)
        self.assertTrue(r.width == 1)
        self.assertTrue(r.height == 2)
        self.assertTrue(r.x == 0)
        self.assertTrue(r.y == 0)
        self.assertTrue(r.id is not None)

    def test_invalid_args(self):
        """
        Test for invalid arguments when creating a Rectangle object.
        """
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4, 5, 6, 7, 8, 9)
            Rectangle(0)
            Rectangle()
            Rectangle(None)

    def test_type_class(self):
        """
        Test the class type of the Rectangle object.
        """
        self.assertTrue(Rectangle(1, 1), self.__class__ == Rectangle)

    def test_private_attr(self):
        """
        Test accessing private attributes of the Rectangle class.
        """
        with self.assertRaises(AttributeError):
            print(Rectangle.__width)
            print(Rectangle.__height)
            print(Rectangle.__x)
            print(Rectangle.__y)

    def test_attr_validated(self):
        """
        Test for checking if attribute values are properly validated when
        creating a Rectangle object.
        """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("3", 3, 3, 3, 3)
            Rectangle([3, 3], 3, 3, 3, 3)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, {}, 2, 2, 2)
            Rectangle(2, {"hello": 222}, 2, 2, 2)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(3, 3, None, 3, 3)
            Rectangle(3, 3, 5.5, 3, 3)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 1, 1, [3.0, "20"], 1)
            Rectangle(1, 1, 1, (30, 20), 1)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 7, 7, 7, 7)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(8, -222, 8, 8, 8)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(111, 111, -111, 111, 111)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(10, 10, 10, -999, 10)

    def test_area(self):
        """
        Test for calculating the area of a Rectangle.
        """
        self.assertEqual(Rectangle(5, 3).area(), 15)
        self.assertEqual(Rectangle(9, 6, 0, 0).area(), 54)
        self.assertEqual(Rectangle(10, 5, 2, 1, 66).area(), 50)

    def test_print(self):
        """
        Test for the string representation of a Rectangle object.
        """
        r0 = Rectangle(3, 3, 3, 3, 3)
        self.assertEqual(str(r0), '[Rectangle] (3) 3/3 - 3/3')
        r1 = Rectangle(7, 13, 19, 6, -2)
        self.assertEqual(str(r1), '[Rectangle] (-2) 19/6 - 7/13')

    def test_update(self):
        """
        Test for updating the attributes of a Rectangle object.
        """
        r = Rectangle(1, 2, 3, 4, 5)
        r.update(10, 20, 30, 40, 50)
        self.assertEqual(str(r), '[Rectangle] (10) 40/50 - 20/30')
        r.update()
        self.assertEqual(str(r), '[Rectangle] (10) 40/50 - 20/30')
        r.update(33)
        self.assertEqual(str(r), '[Rectangle] (33) 40/50 - 20/30')
        r.update(33, 1)
        self.assertEqual(str(r), '[Rectangle] (33) 40/50 - 1/30')
        r.update(33, 1, 2)
        self.assertEqual(str(r), '[Rectangle] (33) 40/50 - 1/2')
        r.update(33, 1, 2, 3, 4)
        self.assertEqual(str(r), '[Rectangle] (33) 3/4 - 1/2')
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r.update(99, 1, 2, 3, "hello")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.update(99, 1, 2, 5.2, 4)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r.update(99, 1, 2, -3, 4)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r.update(99, 1, 2, 3, -4)
        r.update(id=42)
        self.assertEqual(str(r), '[Rectangle] (42) 3/4 - 1/2')
        r.update(id=555, x=666, y=777, width=888, height=999)
        self.assertEqual(str(r), '[Rectangle] (555) 666/777 - 888/999')
        r.update(you=1000, cant=2000, do=3000, this=4000, id=5000)
        self.assertEqual(str(r), '[Rectangle] (5000) 666/777 - 888/999')

    def test_to_dictionary(self):
        """
        Test for converting a Rectangle object to a dictionary representation.
        """
        rdic = Rectangle(7, 56, 15, 7, 19).to_dictionary()
        self.assertEqual(type(rdic), dict)
        r = Rectangle(10, 10)
        r.update(**rdic)
        self.assertEqual(str(r), '[Rectangle] (19) 15/7 - 7/56')
