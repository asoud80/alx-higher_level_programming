#!/usr/bin/python3
""" for Creating Mylist class """


class MyList(list):
    """
    MyList class that inherits from list
    """
    def print_sorted(self):
        """
        to prints the list in sorted order
        """
        print(sorted(self))
