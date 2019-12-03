"""
Create a class
"""


class Box:
    """
    Class Box
    """
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height

    def get_length(self):
        """Get length"""
        return self.length

    def get_width(self):
        """Get width"""
        return self.width

    def get_height(self):
        """Get height"""
        return self.height

    def get_volume(self):
        """Get volume"""
        return self.length * self.width * self.height
