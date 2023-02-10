"""
Module that contains Bullet class
"""

from pygame import Surface
import pygame

from game_objects.game_objects_helpers.game_object import GameObject
from utilities.helper_functions import load_image

class Bullet(GameObject):
    """
    Bullet class that inherites GameObject class
    """

    def __init__(self, position, velocity):
        super().__init__(position, load_image("bullet"), velocity)

        self.angle = 0
        self.is_out_of_screen = False

    def object_moving(self, surface: Surface) -> None:
        """
        Method that moves the bullet on the screen. If the 
        bullet goes out of the screen, it becomes None, the
        bullet dissapears
        """

        self.position.x_coord += self.velocity.x_coord
        self.position.y_coord -= self.velocity.y_coord

        if self.__out_of_screen(surface):
            self.is_out_of_screen = True

    def object_drawing(self, surface: Surface) -> None:
        """
        Method that draws the object on the screen.
        """

        rotated_image = pygame.transform.rotate(self.image, self.angle)
        rotated_rect = self.image.get_rect()
        rotated_rect.center = self.position.to_tuple()
        surface.blit(rotated_image, rotated_rect)

    def __out_of_screen(self, surface: Surface) -> bool:
        return (self.position.x_coord - self.radius <= 0 or
                self.position.x_coord + self.radius >= surface.get_width() or
                self.position.y_coord - self.radius <= 0 or
                self.position.y_coord + self.radius >= surface.get_height())
