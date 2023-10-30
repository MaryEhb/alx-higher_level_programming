#!/usr/bin/python3
""" Rectangle Class """


class Rectangle:
    """
    Rectangle

    Args:
        width: private int
        height: private int
        number_of_instances: int incremented each time
        class instnce is created and decremented when del
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        """
            rect String representation
        """

        return ((str(self.print_symbol) * self.width + '\n')
                * self.height).rstrip("\n")

    def __repr__(self):
        """
        Returns:
            a string representation of the rectangle to be
            able to recreate a new instance by using eval()
        """

        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """
        Called when obj lifetime ends
        """

        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Args:
            rect1: rect1
            rect2: rect2

        Returns:
            the biggest rectangle based on the area
        """

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_2.area() > rect_1.area():
            return rect_2
        return rect_1

    def square(cls, size=0):
        """
        Returns:
            returns a new Rectangle instance with width == height == size
        """

        return Rectangle(cls, cls)
