from pygame.image import load
import os

def load_image(name):
    path = os.path.join("recourses", "images", f"{name}.png")
    return load(path).convert()