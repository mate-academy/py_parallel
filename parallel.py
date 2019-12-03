"""docstring"""


class Box:
    """Create a class for representing the box"""
    def __init__(self, length=None, width=None, height=None):
        self.length = length
        self.width = width
        self.height = height

    def get_length(self):
        """return length box"""
        return self.length

    def get_width(self):
        """return width box"""
        return self.width

    def get_height(self):
        """return height box"""
        return self.height

    def get_volume(self):
        """calculate and return volume box"""
        return self.height * self.width * self.length
