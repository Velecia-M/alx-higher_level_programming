#!/usr/bin/python3

"""Defining a class"""


class Square:
    """creating a class Square"""

    def __init__(self, size=0):
        """Initializing a new square

        Args:
            size (int): size of square
        """
        self.__size = size

    @property
    def size(self):
        """sets the current size of square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the current area of square"""
        return (self.__size * self.__size)
