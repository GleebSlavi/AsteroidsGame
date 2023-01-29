from math import sqrt

class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y - other.y)

    def euclidean_distance(self, other) -> float:
        return sqrt(((self.x - other.x) ** 2) + ((self.y - other.y) ** 2))

    def to_tuple(self):
        return (self.x, self.y)