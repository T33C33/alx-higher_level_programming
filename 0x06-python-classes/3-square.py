#!/usr/bin/python3

"""This class defines a Square."""


class Square:
    """footprint of square"""

    def __init__(self, size=0):
        """
        Initializes a square instance

        where:

        Args:
            size (int): The size of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Returns the area of the square."""
        return (self.__size ** 2)
