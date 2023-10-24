#!/usr/bin/python3
"""Define Square class"""


class Square:
    """
    square class

    Attributes:
        size: size of square
    """
    __size = 0

    def __init__(self, size=0):
        """run when initialized

        Args:
            size: size of square
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """return area
        """

        return (self.__size)**2
