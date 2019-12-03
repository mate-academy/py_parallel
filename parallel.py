"""The class created has 3 dimensions and
provides opportunity to calculate its object's volume"""

class Box:
    """
    Class created has parameters of
    length, width, height being input by user
    """

    def __init__(self, length, width, height):
        """Define obligatory parameters of Box object"""
        self._length = length
        self._width = width
        self._height = height

    def get_length(self):
        """Define request for parameter input by user"""
        return self._length

    def get_width(self):
        """Define request for parameter input by user"""
        return self._width

    def get_height(self):
        """Define request for parameter input by user"""
        return self._height

    def get_volume(self):
        """Calculate the volume of Box object"""
        return self._length * self._width * self._height
