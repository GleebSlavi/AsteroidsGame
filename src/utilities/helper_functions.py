import os
import random
from pygame.image import load

from game_objects.game_objects_helpers.two_dimensional_vector import Vector2D

def get_random_coordinates(surface):
    return Vector2D(random.randrange(surface.get_width()),
                    random.randrange(surface.get_height()))


def load_image(name: str):
    image_directory = os.path.join("external_recourses", "images")
    image = os.path.join(image_directory, f"{name}.png")

    return load(image).convert_alpha()