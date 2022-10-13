#!/usr/bin/python3
"""Define a square class"""


class Square:
    """Our Square"""

    def __init__(self, size=0):
        """
        initialize a new square
        Args:
            size(int): The size of the new square
        """
        self.__size = int(size)
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if self.__size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """
        Area of the Square
        """
        return (self.__size ** 2)
