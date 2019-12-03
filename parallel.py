"""
docstring
"""


class Box:
    """
    class docstring
    """
    def __init__(self, length, width, height):
        """

        :param length:
        :param width:
        :param height:
        """
        self.length = length
        self.width = width
        self.height = height

    def get_length(self):
        """

        :return:
        """
        return self.length

    def get_width(self):
        """

        :return:
        """
        return self.width

    def get_height(self):
        """

        :return:
        """
        return self.height

    def get_volume(self):
        """

        :return:
        """
        return self.length * self.width * self.height
