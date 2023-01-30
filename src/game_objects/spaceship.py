from game_objects.game_objects_helpers.game_object import GameObject, Vector2D
from utilities.helper_functions import load_image

class Spaceship(GameObject):
    def __init__(self, position):
        super().__init__(position, load_image("spaceship"), (0, 0))