"""
Module that contains GameObject class
"""

from typing import Tuple
from pygame import Surface

from game_objects.game_objects_helpers.two_dimensional_vector import Vector2D

class GameObject:
    """
    GameObject class that serves as base class
    for the other game objects
    """

    def __init__(self, position: Tuple[float, float], image: Surface,
                velocity: Tuple[float, float]):
        self.image = image
        self.radius = image.get_width() / 2
        self.velocity = Vector2D(*velocity)
        self.position = Vector2D(*position)

    def object_drawing(self, surface: Surface) -> None:
        """
        Method that draws a game object on the screen
        """

        blit_position = self.position - Vector2D(self.radius, self.radius)
        surface.blit(self.image, blit_position.to_tuple())

    def object_moving(self, surface: Surface) -> None:
        """
        Method that moves a game object on the screen
        """

        self.position += self.velocity

        self.position.x_coord = self.__check_position(self.position.x_coord, surface.get_width())
        self.position.y_coord = self.__check_position(self.position.y_coord, surface.get_height())

    def object_collision(self, other: "GameObject") -> bool:
        """
        Method that checks if the game object collides
        with another game object
        """

        distance = self.position.euclidean_distance(other.position)
        return distance < self.radius + other.radius

    def __check_position(self, position: float, surface_dimension: float) -> float:
        if position > surface_dimension + self.radius:
            return -self.radius
        elif position < -self.radius:
            return surface_dimension + self.radius

        return position
