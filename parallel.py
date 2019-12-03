"""
Classes
-------
Box
    A class used to represent a box
"""


class Box:
    """
    A class used to represent a Box

    Attributes
    ----------
    length : int
        the length of the box
    width : int
        the width of the box
    height : int
        the height of the box

    Methods
    -------
    get_length()
        Return the length of the box
    get_width()
        Return the width of the box
    get_height()
        Return the height of the box
    get_volume()
        Return the volume of the box

    """
    def __init__(self, length, width, height):
        """
        :param length: int
            The length of the box
        :param width: int
            The width of the box
        :param height: int
            The height of the box
        """
        self.length = length
        self.width = width
        self.height = height

    def get_length(self):
        """Return length of the box"""
        return self.length

    def get_width(self):
        """Return width of the box"""
        return self.width

    def get_height(self):
        """Return height of the box"""
        return self.height

    def get_volume(self):
        """Return volume of the box"""
        return self.length * self.width * self.height
