#!/usr/bin/python3
"""
------------------
5. Geometry module
------------------
"""


class BaseGeometry:
    """ BaseGeometry (based on 6-base_geometry.py)"""

    def area(self):
        """Not yet implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate a parameter as an integer.

        Args:
            name (str): The name of the parameter.
            value (int): The parameter to validate.

        Raises:
            TypeError: if value not int
            ValueError: if value less than zero
        """

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
