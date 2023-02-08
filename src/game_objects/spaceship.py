import pygame
from pygame import Surface
from typing import List
import math

from game_objects.game_objects_helpers.game_object import GameObject, Vector2D
from utilities.helper_functions import load_image

class Spaceship(GameObject):
    SPEED: float = 0.15
    ROTATION: int = 5

    def __init__(self, position):
        super().__init__(position, load_image("spaceship"), (0, 0))
        self.angle = 0

        self.__rotate_image()

    def object_drawing(self, surface: Surface) -> None:
        surface.blit(self.rotated_image, self.rotated_rect)

    def __up_and_down(self, up: bool = True) -> None:
        if up:
            self.velocity -= self.SPEED
        else:
            self.velocity += self.SPEED

    def __rotate(self, right: bool = True):
        if right:
            self.angle -= self.ROTATION
        else:
            self.angle += self.ROTATION

        self.__rotate_image()

    def spaceship_movement_handling(self, keys: List[bool], surface) -> None:
        if keys[pygame.K_w]:
            self.__up_and_down()
        elif keys[pygame.K_s]:
            self.__up_and_down(False)

        if keys[pygame.K_a]:
            self.__rotate(False)
        elif keys[pygame.K_d]:
            self.__rotate()

    def __rotate_image(self):
        self.rotated_image = pygame.transform.rotate(self.image, self.angle)
        self.rotated_rect = self.image.get_rect()
        self.rotated_rect.center = self.position.to_tuple()
