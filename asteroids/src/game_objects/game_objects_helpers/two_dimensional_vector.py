"""
Module that contains Vector2D class
"""

from math import sqrt, cos, sin
from typing import Tuple

class Vector2D:
    """
    Vector2D that represent two dimensional vector
    """

    def __init__(self, x_coord: float, y_coord: float):
        self.x_coord = x_coord
        self.y_coord = y_coord

    def __sub__(self, other: "Vector2D") -> "Vector2D":
        return Vector2D(self.x_coord - other.x_coord,
                        self.y_coord - other.y_coord)

    def __add__(self, other: "Vector2D") -> "Vector2D":
        return Vector2D(self.x_coord + other.x_coord,
                        self.y_coord - other.y_coord)

    def __iadd__(self, other: "Vector2D") -> "Vector2D":
        self.x_coord += other.x_coord
        self.y_coord += other.y_coord

        return self

    def __isub__(self, other: "Vector2D") -> "Vector2D":
        self.x_coord -= other.x_coord
        self.y_coord -= other.y_coord

        return self

    def __div__(self, scalar: int | float) -> "Vector2D":
        return Vector2D(self.x_coord / scalar, self.y_coord / scalar)

    def __mul__(self, scalar: int | float) -> "Vector2D":
        return Vector2D(self.x_coord * scalar, self.y_coord * scalar)

    def euclidean_distance(self, other: "Vector2D") -> float:
        """
        Method that calculates the euclidean distance between
        two vectors
        """

        return sqrt(((self.x_coord - other.x_coord) ** 2) +
                    ((self.y_coord - other.y_coord) ** 2))

    def to_tuple(self) -> Tuple[float, float]:
        """
        Method that returns Vector2D coordinates
        as a tuple
        """

        return (self.x_coord, self.y_coord)

    def rotate(self, angle: int) -> "Vector2D":
        """
        Method that rotates a two dimensional
        vector by an angle
        """

        new_x = self.x_coord * cos(angle) - self.y_coord * sin(angle)
        new_y = self.x_coord * sin(angle) + self.y_coord * cos(angle)

        return Vector2D(new_x, new_y)
