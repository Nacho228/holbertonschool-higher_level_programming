#!/usr/bin/python3
"""Unittest for Square class"""


import unittest
import pep8
from models import square
Square = square.Square


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


class TestSquare(unittest.TestCase):
    """
    Test class for the Square class.
    """
    def test_attr_given(self):
        """
        Test for checking if attributes are assigned correctly when
        creating a Square object.
        """
        s = Square(6, 12, 43, 32)
        self.assertTrue(s.width == 6)
        self.assertTrue(s.height == 6)
        self.assertTrue(s.x == 12)
        self.assertTrue(s.y == 43)
        self.assertTrue(s.id == 32)

    def test_default_attr(self):
        """
        Test for checking if default attributes are assigned correctly
        when creating a Square object.
        """
        s = Square(1)
        self.assertTrue(s.width == 1)
        self.assertTrue(s.height == 1)
        self.assertTrue(s.x == 0)
        self.assertTrue(s.y == 0)
        self.assertTrue(s.id is not None)

    def test_invalid_args(self):
        """
        Test for invalid arguments when creating a Square object.
        """
        with self.assertRaises(TypeError):
            Square(1, 2, 3, 4, 5, 6, 7, 8, 9)
            Square()
            Square(None)

    def test_type_class(self):
        """
        Test the class type of the Square object.
        """
        self.assertTrue(Square(1), self.__class__ == Square)

    def test_private_attr(self):
        """
        Test accessing private attributes of the Square class.
        """
        with self.assertRaises(AttributeError):
            print(Square.__width)
            print(Square.__height)
            print(Square.__x)
            print(Square.__y)

    def test_attr_validated(self):
        """
        Test for checking if attribute values are properly validated when
        creating a Square object.
        """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("3", 3, 3, 3)
            Square([3, 3], 3, 3, 3)
            Square({3, }, 3, 3, 3)
            Square({"3": 3}, 3, 3, 3)
            Square((3, 3), 3, 3, 3)
            Square(None, 3, 3, 3)
            Square(3.3, 3, 3, 3)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(3, None, 3, 3)
            Square(3, 3.5, 3, 3)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 1, [3.0, "20"], 1)
            Square(1, 1, (30, 20), 1)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0, 7, 7, 7)
            Square(-5, 7, 7, 7)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(111, -111, 111, 111)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(10, 10, -999, 10)

    def test_area(self):
        """
        Test for calculating the area of a Square.
        """
        self.assertEqual(Square(5).area(), 25)
        self.assertEqual(Square(9, 0, 0).area(), 81)
        self.assertEqual(Square(10, 2, 1, 66).area(), 100)

    def test_print(self):
        """
        Test for the string representation of a Square object.
        """
        s0 = Square(3, 3, 3, 3)
        self.assertEqual(str(s0), '[Square] (3) 3/3 - 3')
        s1 = Square(13, 19, 6, -2)
        self.assertEqual(str(s1), '[Square] (-2) 19/6 - 13')

    def test_update(self):
        """
        Test for updating the attributes of a Square object.
        """
        s = Square(1, 2, 3, 4)
        s.update(10, 20, 30, 40)
        self.assertEqual(str(s), '[Square] (10) 30/40 - 20')
        s.update()
        self.assertEqual(str(s), '[Square] (10) 30/40 - 20')
        s.update(33)
        self.assertEqual(str(s), '[Square] (33) 30/40 - 20')
        s.update(33, 1)
        self.assertEqual(str(s), '[Square] (33) 30/40 - 1')
        s.update(33, 1, 2)
        self.assertEqual(str(s), '[Square] (33) 2/40 - 1')
        s.update(33, 1, 2, 3)
        self.assertEqual(str(s), '[Square] (33) 2/3 - 1')
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s.update(99, 1, 2, "hello")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s.update(99, 1, 2.5, 5)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            s.update(1, 2, -3, 4)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            s.update(1, 2, 3, -4)
        s.update(id=42)
        self.assertEqual(str(s), '[Square] (42) 3/3 - 2')
        s.update(id=555, x=666, y=777, width=888)
        self.assertEqual(str(s), '[Square] (555) 666/777 - 888')
        s.update(you=1000, cant=2000, do=3000, this=4000, id=5000)
        self.assertEqual(str(s), '[Square] (5000) 666/777 - 888')

    def test_to_dictionary(self):
        """
        Test for converting a Square object to a dictionary representation.
        """
        sdic = Square(1, 2, 3, 4).to_dictionary()
        self.assertEqual(type(sdic), dict)
        s = Square(10, 10)
        s.update(**sdic)
        self.assertEqual(str(s), '[Square] (4) 2/3 - 1')
