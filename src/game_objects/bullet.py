from game_objects.game_objects_helpers.game_object import GameObject, Vector2D
from utilities.helper_functions import load_image

class Bullet(GameObject):
    def __init__(self, position, velocity):
        super().__init__(position, load_image("bullet"), velocity)