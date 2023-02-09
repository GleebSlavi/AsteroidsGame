from math import sqrt, cos, sin
from typing import Tuple
from pygame import Surface

class Vector2D:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __sub__(self, other: "Vector2D") -> "Vector2D":
        return Vector2D(self.x - other.x, self.y - other.y)

    def __add__(self, other: "Vector2D") -> "Vector2D":
        return Vector2D(self.x + other.x, self.y - other.y)

    def __iadd__(self, other: "Vector2D") -> "Vector2D":
        self.x += other.x
        self.y += other.y

        return self

    def __isub__(self, other: "Vector2D") -> "Vector2D":
        self.x -= other.x
        self.y -= other.y

        return self

    def __div__(self, scalar: int | float) -> "Vector2D":
        return Vector2D(self.x / scalar, self.y / scalar)

    def __mul__(self, scalar: int | float) -> "Vector2D":
        return Vector2D(self.x * scalar, self.y * scalar)

    def euclidean_distance(self, other: "Vector2D") -> float:
        return sqrt(((self.x - other.x) ** 2) + ((self.y - other.y) ** 2))

    def to_tuple(self) -> Tuple[float, float]:
        return (self.x, self.y)

    def rotate(self, angle: int) -> "Vector2D":
        new_x = self.x * cos(angle) - self.y * sin(angle)
        new_y = self.x * sin(angle) + self.y * cos(angle)

        return Vector2D(new_x, new_y)
