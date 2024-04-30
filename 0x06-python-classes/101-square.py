#!/usr/bin/python3
"""
    Module description
"""

class Square:
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self._size = value

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
            len(value) != 2 or
            not all(isinstance(num, int) and num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self._position = value

    def area(self):
        """Returns the area of the square."""
        return self._size ** 2

    def my_print(self):
        """Prints the square with the character # and uses the position for spacing."""
        if self.size == 0:
            print()
            return

        for _ in range(self.position[1]):
            print()

        for _ in range(self.size):
            print(" " * self.position[0] + "#" * self.size)

    def __str__(self):
        """Defines the string representation of the square."""
        output = []
        if self.size == 0:
            return ""

        for _ in range(self.position[1]):
            output.append("")

        for _ in range(self.size):
            line = " " * self.position[0] + "#" * self.size
            output.append(line)

        return "\n".join(output)
