#!/usr/bin/python3

class Square:
    """
    wrote a class Square that defines a square by:(based on 1-square.py
    """
    def __init__(self, size=0):
        self.__size = int(size)
        if not (isinstance(size, int)):
            raise TypeError("size must be an integer")
        if self.__size < 0:
            raise ValueError("size must be >= 0")
