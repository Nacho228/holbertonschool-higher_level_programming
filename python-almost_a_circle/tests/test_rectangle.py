#!/usr/bin/python3
""" Testing rectangle class """
import unittest
import pep8
from models.rectangle import Rectangle


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

    def setUp(self):
        """
        Create an instance
        of Rectangle for testing
        """
        self.rectangle = Rectangle(5, 10, 2, 3, 1)

    def test_area(self):
        """
        Test the area method
        """
        self.assertEqual(self.rectangle.area(), 50)

    def test_display(self):
        """
         Test the display method
         Since the display method prints to stdout.
         You can manually check if the output is as expected.
        """
        self.rectangle.display()

    def test_to_string(self):
        """
        Test the __str__ method
        """
        expected_output = "[Rectangle] (1) 2/3 - 5/10"
        self.assertEqual(str(self.rectangle), expected_output)

    def test_update_args(self):
        """
        Test the update method with positional arguments
        """
        self.rectangle.update(2, 7, 8, 4, 5)
        self.assertEqual(self.rectangle.id, 2)
        self.assertEqual(self.rectangle.width, 7)
        self.assertEqual(self.rectangle.height, 8)
        self.assertEqual(self.rectangle.x, 4)
        self.assertEqual(self.rectangle.y, 5)

    def test_update_kwargs(self):
        """
        Test the update method with keyword arguments
        """
        self.rectangle.update(width=6, height=12, x=1, y=2)
        self.assertEqual(self.rectangle.width, 6)
        self.assertEqual(self.rectangle.height, 12)
        self.assertEqual(self.rectangle.x, 1)
        self.assertEqual(self.rectangle.y, 2)

    def test_properties(self):
        """
        Test the getter and setter properties
        """
        self.rectangle.width = 15
        self.assertEqual(self.rectangle.width, 15)

        self.rectangle.height = 20
        self.assertEqual(self.rectangle.height, 20)

        self.rectangle.x = 3
        self.assertEqual(self.rectangle.x, 3)

        self.rectangle.y = 4
        self.assertEqual(self.rectangle.y, 4)

    def test_to_dictionary(self):
        """
        Test the to_dictionary method
        """
        expected_dict = {'id': 1, 'width': 5, 'height': 10, 'x': 2, 'y': 3}
        self.assertEqual(self.rectangle.to_dictionary(), expected_dict)


if __name__ == '__main__':
    unittest.main()
