#!/usr/bin/python3
""" Rectangle Class """


class Rectangle:
    """
    Rectangle

    Args:
        __width: private int
        __height: private int
    """

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """
        Get __width

        Returns:
            __width
        """

        return self.__width

    @width.setter
    def width(self, value):
        """
        Set __width

        Args:
            value: new width

        Raises:
            TypeError: If `value` is not an int.
            ValueError: If `value` is less than 0.
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """
        Get __height

        Returns:
            __height
        """

        return self.__height

    @height.setter
    def height(self, value):
        """
        Set __height

        Args:
            value: new height

        Raises:
            TypeError: If `value` is not an int.
            ValueError: If `value` is less than 0.
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value
