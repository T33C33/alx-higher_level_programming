#!/usr/bin/python3
"""
   an empty class Rectangle that defines a rectangle
"""


class Rectangle:
    """This class defines a rectangle"""
    def __init__(self, width=0, height=0):
        """get width"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """get width"""
        return self.__width

    @width.setter
    def width(self, value):
        """set width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """get height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Docstring for Height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Docstring for Area"""
        return (self.width * self.height)

    def perimeter(self):
        """Docstring for Perimeter"""
        return (2 * (self.width + self.height))
