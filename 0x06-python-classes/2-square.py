#!/usr/bin/python3

"""Defining a class"""


class Square:
    """creating a class Square"""

    def __init__(self, size=0):
        """Initializing an instance

        Args:
            size (int): size of square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
