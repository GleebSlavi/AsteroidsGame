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

def get_highest_score() -> int:
    path = os.path.join("src", "utilities", "highest_score.txt")

    with open(path) as file:
        score = int(file.read().strip())

    return score

def safe_highest_score(new_highest_score: int) -> None:
    path = os.path.join("src", "utilities", "highest_score.txt")
    
    with open(path, 'w') as file:
        file.write(str(new_highest_score))

def show_score_and_highest_score(surface: Surface, font: font.Font, score: int, highest_score: int) -> None:
    texts = [f"Highest Score: {highest_score}", f"Score: {score}"]
    score_fonts = []

    for text in texts:
        score_fonts.append(font.render(text, True, Color("azure")))

    y = 3
    for score_font in score_fonts:
        surface.blit(score_font, (3, y))
        y += 20