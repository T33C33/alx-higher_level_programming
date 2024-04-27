#!/usr/bin/python3

"""Module to define a class Square."""


class Square:
    """Further definition of square"""

    def __init__(self, size=0):
        """
        Initializes an instance of Square.

        Args:
            size (int): The size of the square
        """
        self.size = size

    @property
    def size(self):
        """Get method to retrieve size of square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Set method to set size of square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Calculates the area of square"""
        return (self.__size ** 2)

    def my_print(self):
        """Prints the square using the character #"""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
