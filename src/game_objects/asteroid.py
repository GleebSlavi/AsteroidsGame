from game_objects.game_objects_helpers.game_object import GameObject, Vector2D
from utilities.utils import load_image

class Asteroid(GameObject):
    def __init__(self, position):
        super().__init__(position, load_image("asteroid"), (0, 0))