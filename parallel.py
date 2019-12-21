"""
box
"""


class Box:
    """
    box
    """
    def __init__(self, length, width, heigth):
        self._length = length
        self._width = width
        self._height = heigth

    def get_length(self):
        """
        length
        """
        return self._length

    def get_width(self):
        """
        width
        """
        return self._width

    def get_height(self):
        """
        height
        """
        return self._height

    def get_volume(self):
        """
        volume
        """
        return self._length * self._height * self._width
