from pygame import Surface

from game_objects.game_objects_helpers.game_object import GameObject, Vector2D
from utilities.helper_functions import load_image, get_random_velocity

class Asteroid(GameObject):
    def __init__(self, position):
        super().__init__(position, load_image("asteroid"), get_random_velocity().to_tuple())
