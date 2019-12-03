"""class box module"""


class Box:
    """Class with required interface"""
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height

    def get_length(self):
        """
        :return: box length
        """
        return self.length

    def get_width(self):
        """
        :return: box width
        """
        return self.width

    def get_height(self):
        """
        :return: box height
        """
        return self.height

    def get_volume(self):
        """
        :return: box volume
        """
        return self.length * self.width * self.height
