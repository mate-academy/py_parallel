"""Create a class for representing the box
 in accordance with the interface specified in the test file."""


class Box:
    """Class for representing the box"""

    def __init__(self, length: float, width: float, height: float):
        self.length = length
        self.width = width
        self.height = height

    def get_length(self) -> float:
        """Returns length attribute"""
        return self.length

    def get_width(self) -> float:
        """Returns width attribute"""
        return self.width

    def get_height(self) -> float:
        """Returns height attribute"""
        return self.height

    def get_volume(self) -> float:
        """Returns volume. The volume is the multiplication of the width, height and length."""
        volume = self.height * self.width * self.length
        return volume
