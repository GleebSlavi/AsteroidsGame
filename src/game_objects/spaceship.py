import pygame
from pygame import Surface
from typing import List
from pygame.mixer import Sound

from game_objects.game_objects_helpers.game_object import GameObject, Vector2D
from game_objects.bullet import Bullet
from utilities.helper_functions import load_image, get_sin_or_cos

class Spaceship(GameObject):
    SPEED: float = 0.03
    ROTATION: int = 3
    BULLET_SPEED: float = 5

    def __init__(self, position):
        super().__init__(position, load_image("spaceship"), (0, 0))
        self.angle = 0
        self.head = self.__get_direction()

    def object_drawing(self, surface: Surface) -> None:
        rotated_image = pygame.transform.rotate(self.image, self.angle)
        rotated_rect = self.image.get_rect()
        rotated_rect.center = self.position.to_tuple()
        surface.blit(rotated_image, rotated_rect)

    def object_moving(self, surface: Surface) -> None:
        super().object_moving(surface)
        self.head = self.__get_direction()

    def __move_forward_and_back(self, forward: bool = True) -> None:
        if forward:
            self.velocity.x += get_sin_or_cos(self.angle, False) * self.SPEED
            self.velocity.y -= get_sin_or_cos(self.angle) * self.SPEED
        else:
            self.velocity.x -= get_sin_or_cos(self.angle, False) * self.SPEED
            self.velocity.y += get_sin_or_cos(self.angle) * self.SPEED
            
    def __rotate(self, right: bool = True) -> None:
        if right:
            self.angle -= self.ROTATION
        else:
            self.angle += self.ROTATION

        self.head = self.__get_direction()

    def spaceship_movement_handling(self, keys: List[bool]) -> None:
        if keys[pygame.K_w]:
            self.__move_forward_and_back()
        elif keys[pygame.K_s]:
            self.__move_forward_and_back(False)

        if keys[pygame.K_a]:
            self.__rotate(False)
        elif keys[pygame.K_d]:
            self.__rotate()

    def __get_direction(self) -> Vector2D:
        x = self.position.x + get_sin_or_cos(self.angle) * self.image.get_width() // 2
        y = self.position.y - get_sin_or_cos(self.angle, False) * self.image.get_height() // 2

        return Vector2D(x, y)

    def shooting(self) -> Bullet:
        bullet_velocity = self.__get_bulet_velocity()
        bullet = Bullet(self.head.to_tuple(), bullet_velocity.to_tuple())
        bullet.angle = self.angle



        return bullet

    def __get_bulet_velocity(self) -> Vector2D:
        x = (self.head.x * 0.8) * (self.SPEED * get_sin_or_cos(self.angle, False))
        y = (self.head.y * 0.8) * (self.SPEED * get_sin_or_cos(self.angle))

        return Vector2D(x, y)