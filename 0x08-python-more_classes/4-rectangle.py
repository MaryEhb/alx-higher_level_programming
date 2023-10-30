#!/usr/bin/python3
""" Rectangle Class """


class Rectangle:
    """
    Rectangle

    Args:
        width: private int
        height: private int
    """

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def __str__(self):
        """
            rect String representation
        """

        return (('#' * self.width + '\n') * self.height).rstrip("\n")

    def __repr__(self):
        """
        Returns:
            a string representation of the rectangle to be
            able to recreate a new instance by using eval()
        """

        return f"Rectangle({self.width}, {self.height})"

    @property
    def width(self):
        """
        Get width

        Returns:
            width
        """

        return self.__width

    @width.setter
    def width(self, value):
        """
        Set width

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
        Get height

        Returns:
            height
        """

        return self.__height

    @height.setter
    def height(self, value):
        """
        Set height

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

    def area(self):
        """
        calc area

        Returns:
            area
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calc Perimeter

        Returns:
            perimeter
        """

        if self.width == 0 or self.height == 0:
            return 0

        return 2 * self.width + 2 * self.height
