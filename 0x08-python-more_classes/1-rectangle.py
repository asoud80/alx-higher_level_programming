#!/usr/bin/python3
"""to defines the rectangle class."""


class Rectangle:
    """to display rectangle."""

    def __init__(self, width=0, height=0):
        """initialization of the new rectangle.

        arguments:
            width (int): a width Of a New Rectangle.
            height (int): a height Of a New Rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """set/get a width Of a Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("Width Must Be Integer")
        if value < 0:
            raise ValueError("Width Must Be >= 0")
        self.__width = value

    @property
    def height(self):
        """set/get a Height Of a Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("the Height Must Be integer")
        if value < 0:
            raise ValueError("the Height Must be >= 0")
        self.__height = value
