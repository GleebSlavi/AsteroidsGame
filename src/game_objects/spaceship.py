import pygame
from pygame import Surface
from typing import List

from game_objects.game_objects_helpers.game_object import GameObject, Vector2D
from utilities.helper_functions import load_image

class Spaceship(GameObject):
    SPEED: float = 0.15

    def __init__(self, position):
        super().__init__(position, load_image("spaceship"), (0, 0))


    def __up_and_down(self, up: bool = True):
        if up:
            self.velocity.y -= self.SPEED
        else:
            self.velocity.y += self.SPEED

    # rotate doesnt work
    def __rotate(self, surface: Surface, right: bool = True):
        if right:
            self.image = pygame.transform.rotate(surface, 45)
        else:
            self.image = pygame.transform.rotate(surface, -45)
        

    def spaceship_movement_handling(self, keys: List[bool]) -> None:
        if keys[pygame.K_w]:
            self.__up_and_down()
        elif keys[pygame.K_s]:
            self.__up_and_down(False)
