#!/usr/bin/python3
"""
   an empty class Rectangle that defines a rectangle
"""


class Rectangle:
    """This class defines a rectangle"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """get width"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        if self.width == 0 or self.height == 0:
            return 0
        return (2 * (self.width + self.height))

    def __str__(self):
        """Dunder to print the rectangle with #"""
        if self.width == 0 or self.height == 0:
            return ""
        hash = ""
        for display in range(self.height):
            hash += "#" * self.width + "\n"
        return hash.rstrip()

    def __repr__(self):
        """Dunder to print a representation of an instance"""
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """Dunder that prints message Bye rectangle...
        when an object instance is deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
