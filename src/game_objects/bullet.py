from pygame import Surface
import pygame

from game_objects.game_objects_helpers.game_object import GameObject
from utilities.helper_functions import load_image

class Bullet(GameObject):
    def __init__(self, position, velocity):
        super().__init__(position, load_image("bullet"), velocity)

        self.angle = 0

    def object_moving(self, surface: Surface) -> None:
        self.position.x += self.velocity.x
        self.position.y -= self.velocity.y

        if self.__out_of_screen(surface):
            self = None

    def object_drawing(self, surface: Surface) -> None:
        rotated_image = pygame.transform.rotate(self.image, self.angle)
        rotated_rect = self.image.get_rect()
        rotated_rect.center = self.position.to_tuple()
        surface.blit(rotated_image, rotated_rect)

    def __out_of_screen(self, surface: Surface):
        return (self.position.x - self.radius <= 0 or
                self.position.x + self.radius >= surface.get_width() or
                self.position.y - self.radius <= 0 or
                self.position.y + self.radius >= surface.get_height())