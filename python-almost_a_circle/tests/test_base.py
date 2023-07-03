#!/usr/bin/python3
"""test each method"""
import unittest
import pep8
from models.base import Base


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
        files = ["models/base.py", "tests/test_base.py"]
        errors += style.check_files(files).total_errors
        self.assertEqual(errors, 0, 'Need to fix Pep8')


class TestBase(unittest.TestCase):

    def test_integer_validator(self):
        """ Test integer validator """
        instance = Base()

        instance.integer_validator("test", 5)

        with self.assertRaises(TypeError):
            instance.integer_validator("test", "not an integer")

        with self.assertRaises(ValueError):
            instance.integer_validator("test", -5)

    def test_x_or_y(self):
        """test x or y"""
        instance = Base()

        instance.x_or_y("test", 10)

        with self.assertRaises(TypeError):
            instance.x_or_y("test", "not an integer")

        with self.assertRaises(ValueError):
            instance.x_or_y("test", -5)

    def test_to_json_string(self):
        """test to_json_string"""
        instance = Base()

        self.assertEqual(instance.to_json_string([]), "[]")

        data = [{'name': 'o', 'age': 30}, {'name': 'Pe', 'age': 25}]
        expected_json = '[{"name": "o", "age": 30}, {"name": "Pe", "age": 25}]'
        self.assertEqual(instance.to_json_string(data), expected_json)

    def test_save_to_file(self):
        """test save_to_file"""
        instance = Base()

        instance.save_to_file([])
        instance1 = Base()
        instance2 = Base()
        instances = [instance1, instance2]

        instance.save_to_file(instances)

    def test_from_json_string(self):
        """test from_json_string"""
        instance = Base()

        self.assertEqual(instance.from_json_string("[]"), [])

        json_string = '[{"name": "J", "age": 30}, {"name": "Ja", "age": 25}]'
        expected_data = [{'name': 'J', 'age': 30}, {'name': 'Ja', 'age': 25}]
        self.assertEqual(instance.from_json_string(json_string), expected_data)

    def test_create(self):
        """test create"""
        from models.rectangle import Rectangle

        rectangle = Rectangle.create(**{"type": "Rectangle", "width": 5, "height": 10})
        self.assertIsInstance(rectangle, Rectangle)
        self.assertEqual(rectangle.width, 5)
        self.assertEqual(rectangle.height, 10)

    def test_load_from_file(self):
        """test load_from_file"""
        instance = Base()

        filename = "nonexistent.json"
        result = instance.load_from_file(filename)
        self.assertEqual(result, [])

        # Test loading from an empty file
        # Create an empty JSON file named "empty.json" before running the test case
        filename = "empty.json"
        result = instance.load_from_file(filename)
        self.assertEqual(result, [])

        # Test loading from a file with valid data
        # Create a JSON file named "valid.json"
        filename = "valid.json"
        result = instance.load_from_file(filename)


if __name__ == '__main__':
    unittest.main()
