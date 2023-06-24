#!/usr/bin/python3
"""task 1 """


class My_list(list):
    """MY list class"""
    def print_sorted(self):
        """Print sortedlist"""
        print(sorted(self))
