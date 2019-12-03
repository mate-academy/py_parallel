"""module docstring"""


class Box:
    """class representing box with height length and width"""
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height

    def get_length(self):
        """return length of box"""
        return self.length

    def get_width(self):
        """return width of box"""
        return self.width

    def get_height(self):
        """return height of box"""
        return self.height

    def get_volume(self):
        """return volume of box"""
        return self.width * self.height * self.length
