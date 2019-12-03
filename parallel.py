"""
module parallel
"""


class Box:
    """
    class Box representing the box in accordance with the interface specified in the test file.
    """

    def __init__(self, length: float, width: float, height: float):
        self._length = length
        self._width = width
        self._height = height

    def get_length(self) -> float:
        """
        Return length attribute of the box object.
        :return: float
        """
        return self._length

    def get_width(self) -> float:
        """
        Return width attribute of the box object.
        :return: float
        """
        return self._width

    def get_height(self) -> float:
        """
        Return height attribute of the box object.
        :return: float
        """
        return self._height

    def get_volume(self) -> float:
        """
        Calculate volume of the box object.
        :return: float
        """
        return self._length * self._width * self._height
