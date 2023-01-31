from typing import Tuple
from pygame import Surface

from game_objects.game_objects_helpers.two_dimensional_vector import Vector2D

class GameObject:
    def __init__(self, position: Tuple[float, float], image: Surface, velocity: Tuple[float, float]):
        self.image = image
        self.radius = image.get_width() / 2
        self.velocity = Vector2D(*velocity)
        self.position = Vector2D(*position)

    def object_drawing(self, surface: Surface) -> None:
        blit_position = self.position - Vector2D(self.radius, self.radius)
        surface.blit(self.image, blit_position.to_tuple())

    def object_moving(self, surface: Surface) -> None:
        self.position += self.velocity

    def object_collision(self, other: "GameObject") -> bool:
        distance = self.position.euclidean_distance(other.position)
        return distance < self.radius + other.radius

    def _check_position(self, position: float, surface_dimension: float) -> float:
        if position > surface_dimension + self.radius:
            return -self.radius
        elif position < -self.radius:
            return surface_dimension + self.radius

        return position
