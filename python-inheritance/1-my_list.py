#!/usr/bin/python3
"""task 1 """


class MyList(list):
    """MY list class"""
    def print_sorted(self):
        """Print sortedlist"""
        print(sorted(self))
