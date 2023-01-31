import pygame

from game_objects.game_objects_helpers.game_object import GameObject, Vector2D
from utilities.helper_functions import load_image

class Spaceship(GameObject):
    def __init__(self, position):
        super().__init__(position, load_image("spaceship"), (0, 0))


    def rotate(self, right=True):
        if right:
            old_center = Vector2D(self.image.get_rect().center, self.image.get_rect().center)
            rotated_image = pygame.transform.rotate(self.image, 5)
            self.image = rotated_image
            old_center.rotate(5)
            self.image.get_rect().center = old_center.rotate(5).to_tuple()
        else:
            old_center = Vector2D(self.image.get_rect().center, self.image.get_rect().center)
            rotated_image = pygame.transform.rotate(self.image, -5)
            self.image = rotated_image
            old_center.rotate(5)
            self.image.get_rect().center = old_center.rotate(-5).to_tuple()
