import os
import random
from pygame.image import load

from game_objects.game_objects_helpers.two_dimensional_vector import Vector2D

def get_random_coordinates(surface):
    return Vector2D(random.randrange(surface.get_width()),
                    random.randrange(surface.get_height()))


def load_image(name: str, with_alpha: bool=True):
    path = os.path.join("external_recourses", "images", f"{name}.png")

    if with_alpha:
        return load(path).convert_alpha()
    else:
        return load(path).convert()