#!/usr/bin/python3
"""Unittest for Base class"""


import unittest
import json
import pep8
from models import base
from models import rectangle
Base = base.Base
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
        files = ["models/base.py", "tests/test_base.py"]
        errors += style.check_files(files).total_errors
        self.assertEqual(errors, 0, 'Need to fix Pep8')


class TestBase(unittest.TestCase):
    """
    Test class for the Base class.
    """
    def test_id_given(self):
        """
        Test the ID assignment when an ID is given.
        """
        self.assertTrue(Base(1), self.id == 1)
        self.assertTrue(Base(0), self.id == 0)
        self.assertTrue(Base(333), self.id == 333)
        self.assertTrue(Base(-77), self.id == -77)

    def test_id_not_given(self):
        """
        Test the ID assignment when an ID is not given.
        """
        self.assertTrue(Base(), self.id == 1)
        self.assertTrue(Base(), self.id == 2)
        self.assertTrue(Base(), self.id == 3)

    def test_invalid_args(self):
        """
        Test for invalid arguments when creating a Base object.
        """
        with self.assertRaises(TypeError):
            Base(1, 1)
            Base(1, 1, 1)

    def test_type_class(self):
        """
        Test the class type of the Base object.
        """
        self.assertTrue(Base(), self.__class__ == Base)

    def test_private_attr(self):
        """
        Test accessing private attributes of the Base class.
        """
        with self.assertRaises(AttributeError):
            print(Base.__nb_objects)
            print(Base.nb_objects)

    def test_to_json_string(self):
        """
        Test the conversion of a dictionary to a JSON string.
        """
        dic0 = {"id": 4, "width": 1, "height": 6, "x": 3, "y": 5}
        dic1 = {"id": 2, "width": 3, "height": 3, "x": 4, "y": 5}
        json_str = Base.to_json_string([dic0, dic1])
        self.assertTrue(type(dic0) == dict)
        self.assertTrue(type(json_str) == str)
        self.assertTrue(json_str,
                        [{"id": 4, "width": 1, "height": 6, "x": 3, "y": 5},
                         {"id": 2, "width": 3, "height": 3, "x": 4, "y": 5}])

    def test_none_to_json_string(self):
        """
        Test converting None to a JSON string.
        """
        dic = None
        json_str = Base.to_json_string([dic])
        self.assertTrue(type(json_str) == str)
        self.assertTrue(json_str, "[]")

    def test_empty_to_json_string(self):
        """
        Test converting an empty dictionary to a JSON string.
        """
        dic = dict()
        json_str = Base.to_json_string([dic])
        self.assertTrue(len(dic) == 0)
        self.assertTrue(type(json_str) == str)
        self.assertTrue(json_str, "[]")

    def test_save_to_file(self):
        """
        Test saving objects to a file.
        """
        r0 = Rectangle(1, 2, 3, 4, 5)
        r1 = Rectangle(9, 8, 7, 6, 5)
        Rectangle.save_to_file([r0, r1])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(
                json.dumps([r0.to_dictionary(), r1.to_dictionary()]),
                file.read())

    def test_save_none_to_file(self):
        """
        Test saving None to a file.
        """
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            self.assertEqual('[]', file.read())

    def test_save_empty_to_file(self):
        """
        Test saving an empty list to a file.
        """
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            self.assertEqual('[]', file.read())

    def test_from_json_string(self):
        """
        Test the conversion of a JSON string to a list of dictionaries.
        """
        json_str = '[{"id": 11, "width": 4, "height": 5, "x": 2, "y": 8},\
               {"id": 22, "width": 6, "height": 5, "x": 9, "y": 5}]'
        list_dict = Base.from_json_string(json_str)
        self.assertTrue(type(json_str) == str)
        self.assertTrue(type(list_dict) == list)
        self.assertTrue(type(list_dict[0]) == dict)
        self.assertTrue(list_dict,
                        [{"id": 11, "width": 4, "height": 5, "x": 2, "y": 8},
                         {"id": 22, "width": 6, "height": 5, "x": 9, "y": 5}])
        self.assertTrue(list_dict[0],
                        {"id": 11, "width": 4, "height": 5, "x": 2, "y": 8})

    def test_from_none_json_string(self):
        """
        Test converting None to a list of dictionaries.
        """
        json_str = None
        list_dict = Base.from_json_string(json_str)
        self.assertTrue(type(list_dict) == list)
        self.assertTrue(list_dict == [])

    def test_from_empty_json_string(self):
        """
        Test converting an empty JSON string to a list of dictionaries.
        """
        json_str = ""
        list_dict = Base.from_json_string(json_str)
        self.assertTrue(type(list_dict) == list)
        self.assertTrue(list_dict == [])

    def test_create(self):
        """
        Test creating an object using the create() method.
        """
        r0 = Rectangle(4, 6, 2, 3, 34)
        rdic = r0.to_dictionary()
        r1 = Rectangle.create(**rdic)
        self.assertEqual(str(r0), '[Rectangle] (34) 2/3 - 4/6')
        self.assertEqual(str(r1), '[Rectangle] (34) 2/3 - 4/6')
        self.assertIsNot(r0, r1)

    def test_load_from_file(self):
        """
        Test loading objects from a file.
        """
        r0 = Rectangle(5, 7, 22, 18, 10)
        r1 = Rectangle(6, 8, 21, 17, 20)
        Rectangle.save_to_file([r0, r1])
        recs = Rectangle.load_from_file()
        self.assertEqual(len(recs), 2)
        for key, value in enumerate(recs):
            if key == 0:
                self.assertEqual(str(value), '[Rectangle] (10) 22/18 - 5/7')
            if key == 1:
                self.assertEqual(str(value), '[Rectangle] (20) 21/17 - 6/8')

    def test_load_from_none_file(self):
        """
        Test loading objects from a None file.
        """
        Rectangle.save_to_file(None)
        recs = Rectangle.load_from_file()
        self.assertEqual(type(recs), list)
        self.assertEqual(len(recs), 0)

    def test_load_from_empty_file(self):
        """
        Test loading objects from an empty file.
        """
        Rectangle.save_to_file([])
        recs = Rectangle.load_from_file()
        self.assertEqual(type(recs), list)
        self.assertEqual(len(recs), 0)
