from pygame.image import load
import os

def load_image(name: str, with_alpha: bool=True):
    path = os.path.join("recourses", "images", f"{name}.png")

    if with_alpha:
        return load(path).convert_alpha()
    else:
        return load(path).convert()