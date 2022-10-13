#!/usr/bin/python3
""" Define Square """


class Square:
    """ Square class """

    def __init__(self, size=0):
        """
        Intialize the size of the square
        Args:
            size (int): The integer size of square
        """
        self.size = size

    @property
    def size(self):
        """
        size property
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        if not (isinstance(value, int)):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        return area of the square
        """
        return (self.__size ** 2)

    def my_print(self):
        """
        print in stdout the square
        with the character
        """
        if self.__size == 0:
            print("")
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
