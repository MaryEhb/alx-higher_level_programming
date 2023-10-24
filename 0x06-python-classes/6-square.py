#!/usr/bin/python3
"""Define Square class"""


class Square:
    """
    square class

    Attributes:
        __size: size of square
        __position: position
    """
    __size = 0

    def __init__(self, size=0, position=(0, 0)):
        """run when initialized

        Args:
            size: size of square
        """

        self.__size = size
        self.__position = position

    def area(self):
        """Return area
        """

        return (self.__size)**2

    @property
    def size(self):
        """Retrun size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        set size

        Args:
            size: size
            value: new value
        """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """
        print square
        """
        if self.__size == 0:
            print('')
        else:
            print(''.join('\n' * self.__position[1]), end='')
            for i in range(self.__size):
                print(''.join(' ' * self.__position[0]), end='')
                print(''.join('#' * self.__size))
