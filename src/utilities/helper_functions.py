import os
import random
from math import sin, cos, radians
from pygame.image import load
from pygame import mixer, Surface, font, Color
from typing import Tuple

from game_objects.game_objects_helpers.two_dimensional_vector import Vector2D

def get_random_coordinates(surface: Surface) -> Vector2D:
    return Vector2D(random.randrange(surface.get_width()),
                    random.randrange(surface.get_height()))

def load_image(name: str) -> Surface:
    image_directory = os.path.join("external_recourses", "images")
    image = os.path.join(image_directory, f"{name}.png")

    return load(image).convert_alpha()

def load_sound(name: str, mixer: mixer) -> None:
    sound_directory = os.path.join("external_recourses", "sounds")
    sound = os.path.join(sound_directory, f"{name}.wav")

    mixer.music.load(sound)

def get_random_velocity():
    angle = random.randrange(0, 360)
    return Vector2D(2, 0).rotate(angle)

def get_highest_score() -> int:
    path = os.path.join("src", "utilities", "highest_score.txt")

    with open(path) as file:
        score = int(file.read().strip())

    return score

def safe_highest_score(new_highest_score: int) -> None:
    path = os.path.join("src", "utilities", "highest_score.txt")
    
    with open(path, 'w') as file:
        file.write(str(new_highest_score))

def get_sin_or_cos(angle: int, is_sin: bool = True):
    if is_sin:
        return sin(radians(angle + 90))

    return cos(radians(angle + 90))

def print_text_on_screen(surface: Surface, font: font.Font, text: str, coordinates: Tuple[float, float]):
    screen_text = font.render(text, True, Color("azure"))

    text_rect = screen_text.get_rect()
    text_rect.center = coordinates

    surface.blit(screen_text, text_rect)
