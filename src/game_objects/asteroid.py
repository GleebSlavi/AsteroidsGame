from pygame import Surface

from game_objects.game_objects_helpers.game_object import GameObject, Vector2D
from utilities.helper_functions import load_image, get_random_velocity

class Asteroid(GameObject):
    def __init__(self, position):
        super().__init__(position, load_image("asteroid"), get_random_velocity().to_tuple())

    def object_moving(self, surface: Surface) -> None:
        super().object_moving(surface)

        self.position.x = super()._check_position(self.position.x, surface.get_width())
        self.position.y = super()._check_position(self.position.y, surface.get_height())

