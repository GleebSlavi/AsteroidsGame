"""
Module that contains Asteroid class
"""

from typing import Dict

from pygame import transform, Surface

from utilities.helper_functions import load_image, get_random_velocity
from game_objects.game_objects_helpers.game_object import GameObject, Vector2D

class Asteroid(GameObject):
    """
    Asteroid class that inherites GameObject class
    """

    SIZES: Dict[int, float] = {
        1: 1,
        2: 0.5,
        3: 0.25
    }

    def __init__(self, position: Vector2D, size: int = 1):
        self.size = size
        image = load_image("asteroid")
        image = transform.scale(image, self.__get_new_size(image))

        super().__init__(position, image, get_random_velocity().to_tuple())

    def __get_new_size(self, image: Surface):
        return (image.get_rect().width * self.SIZES[self.size],
                image.get_rect().height * self.SIZES[self.size])
