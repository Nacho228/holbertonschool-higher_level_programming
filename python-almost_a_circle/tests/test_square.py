#!/usr/bin/python3
""" Test square class """
import unittest
import pep8
from models.square import Square


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
        files = ["models/square.py", "tests/test_square.py"]
        errors += style.check_files(files).total_errors
        self.assertEqual(errors, 0, 'Need to fix Pep8')


class TestSquare(unittest.TestCase):

    def setUp(self):
        """
        Create an instance of Square for testing
        """
        self.square = Square(5, 2, 3, 1)

    def test_area(self):
        """
        Test the area method
        """
        self.assertEqual(self.square.area(), 25)

    def test_display(self):
        """
        Test the display method
        Since the display method prints to stdout.
        You can manually check if the output is as expected.
        """
        self.square.display()

    def test_to_string(self):
        """
        Test the __str__ method
        """
        expected_output = "[Square] (1) 2/3 - 5"
        self.assertEqual(str(self.square), expected_output)

    def test_update_args(self):
        """
        Test the update method with positional arguments
        """
        self.square.update(2, 7, 4, 5)
        self.assertEqual(self.square.id, 2)
        self.assertEqual(self.square.size, 7)
        self.assertEqual(self.square.x, 4)
        self.assertEqual(self.square.y, 5)

    def test_update_kwargs(self):
        """
        Test the update method with keyword arguments
        """
        self.square.update(size=6, x=1, y=2)
        self.assertEqual(self.square.size, 6)
        self.assertEqual(self.square.x, 1)
        self.assertEqual(self.square.y, 2)

    def test_properties(self):
        """
        Test the getter and setter properties
        """
        self.square.size = 10
        self.assertEqual(self.square.size, 10)
        self.assertEqual(self.square.width, 10)
        self.assertEqual(self.square.height, 10)

        self.square.x = 3
        self.assertEqual(self.square.x, 3)

        self.square.y = 4
        self.assertEqual(self.square.y, 4)

    def test_to_dictionary(self):
        """
        Test the to_dictionary method
        """
        expected_dict = {'id': 1, 'size': 5, 'x': 2, 'y': 3}
        self.assertEqual(self.square.to_dictionary(), expected_dict)


if __name__ == '__main__':
    unittest.main()
