#!/usr/bin/python3
""" Test file for base.py file"""


import unittest

class testBase(unittest.TestCase):
    def test_default_id(self):
        self.assertEqual(self, None)