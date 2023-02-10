"""
Module that contains helper functions
"""

from typing import Tuple
import os
import random
from math import sin, cos, radians

import pygame
from pygame.mixer import Sound
from pygame.image import load
from pygame import Surface, Color

from game_objects.game_objects_helpers.two_dimensional_vector import Vector2D

def get_random_coordinates(surface: Surface) -> Vector2D:
    """
    Method that returns Vector2D object with random
    coordinates
    """

    return Vector2D(random.randrange(surface.get_width()),
                    random.randrange(surface.get_height()))

def load_image(name: str) -> Surface:
    """
    Method that loads and returns an image from its name
    """

    image_directory = os.path.join("external_recourses", "images")
    image = os.path.join(image_directory, f"{name}.png")

    return load(image).convert_alpha()

def load_sound(name: str) -> Sound:
    """
    Method that loads and returns a sound from its name
    """

    sound_directory = os.path.join("external_recourses", "sounds")
    sound = os.path.join(sound_directory, f"{name}.wav")

    return Sound(sound)

def get_random_velocity():
    """
    Method that returns velocity Vector2D object with
    random coordinates
    """

    angle = random.randrange(0, 360)
    return Vector2D(1.5, 0).rotate(angle)

def get_highest_score() -> int:
    """
    Method that loads the highest score from a file
    and returns it
    """

    path = os.path.join("src", "utilities", "highest_score.txt")

    with open(path, encoding="utf-8") as file:
        score = int(file.read().strip())

    return score

def safe_highest_score(new_highest_score: int) -> None:
    """
    Method that safes the highest score in a file
    """

    path = os.path.join("src", "utilities", "highest_score.txt")

    with open(path, 'w', encoding="utf-8") as file:
        file.write(str(new_highest_score))

def get_sin_or_cos(angle: int, is_sin: bool = True):
    """
    Method that return sin or cosine of an angle
    """

    if is_sin:
        return sin(radians(angle + 90))

    return cos(radians(angle + 90))

def print_text_on_screen(surface: Surface, font: pygame.font.Font, text: str,
                        coordinates: Tuple[float, float]):
    """
    Method that prints text on the screen
    """

    screen_text = font.render(text, True, Color("azure"))

    text_rect = screen_text.get_rect()
    text_rect.center = coordinates

    surface.blit(screen_text, text_rect)
