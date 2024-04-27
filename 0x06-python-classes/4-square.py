#!/usr/bin/python3

"""Class defines a class Square"""


class Square:
    """Definitions of the class square"""

    def __init__(self, size=0):
        """
        Initializes an instance of Square.

        Args:
            size (int): The size of Square.
        """
        self.size = size

    @property
    def size(self):
        """get method to retrieve the size of the square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Set method for setting the size of the square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Calculate area of the square"""
        return (self.__size ** 2)
