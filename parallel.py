"""Module desctibes class of the Box"""


class Box:
    """Class of the Box"""
    def __init__(self, length, width, height):
        self._length = length
        self._width = width
        self._height = height

    def get_width(self):
        """Get with of the box"""
        return self._width

    def get_height(self):
        """Get height of the box"""
        return self._height

    def get_length(self):
        """Get length of the box"""
        return self._length

    def get_volume(self):
        """Get volume of the box"""
        return self._width * self._height * self._length
