#!/usr/bin/python3
"""Square defines a square """


class Square:
    """class that defines a square."""

    def __init__(self, size=0):
        """
        an instance from the Square class
        Args:
            size (int, optional): defines size of the square
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
