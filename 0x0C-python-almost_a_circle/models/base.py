#!/usr/bin/python3
"""Module for a Base Class."""

class Base:
    """Represents a Base class"""

    __nb_objects = 0
    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            seld.id = __nb_objects
