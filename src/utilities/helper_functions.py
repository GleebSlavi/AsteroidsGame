import os
import random
from pygame.image import load
from pygame import mixer, Surface, font, Color

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
    return Vector2D(3, 0).rotate(angle)

def print_game_over_text(surface: Surface, font: font.Font) -> None:
    game_over_text = font.render("Game Over!", True, Color("azure"))
    
    text_rect = game_over_text.get_rect()
    text_rect.center = (500, 333)

    surface.blit(game_over_text, text_rect)