"""
Module that contains Spaceschip class
"""

from typing import List

from pygame import Surface, transform , K_w, K_a, K_d, K_s

from src.helper_functions import load_image, get_sin_or_cos
from src.game_objects.game_objects_helpers.game_object import GameObject, Vector2D
from src.game_objects.bullet import Bullet

class Spaceship(GameObject):
    """
    Spaceship class that inherites GameObject class
    """

    SPEED: float = 0.03
    ROTATION: int = 3
    BULLET_SPEED: float = 5

    def __init__(self, position):
        super().__init__(position, load_image("spaceship"), (0, 0))
        self.angle = 0
        self.head = self.__get_direction()

    def object_drawing(self, surface: Surface) -> None:
        """
        Method that draws the spaceship on the screen
        """

        rotated_image = transform.rotate(self.image, self.angle)
        rotated_rect = self.image.get_rect()
        rotated_rect.center = self.position.to_tuple()
        surface.blit(rotated_image, rotated_rect)

    def object_moving(self, surface: Surface) -> None:
        """
        Method that moves the spaceship on the screen and
        change where the spaceship points to
        """

        super().object_moving(surface)
        self.head = self.__get_direction()

    def __move_forward_and_back(self, forward: bool = True) -> None:
        if forward:
            self.velocity.x_coord += get_sin_or_cos(self.angle, False) * self.SPEED
            self.velocity.y_coord -= get_sin_or_cos(self.angle) * self.SPEED
        else:
            self.velocity.x_coord -= get_sin_or_cos(self.angle, False) * self.SPEED
            self.velocity.y_coord += get_sin_or_cos(self.angle) * self.SPEED

    def __rotate(self, right: bool = True) -> None:
        if right:
            self.angle -= self.ROTATION
        else:
            self.angle += self.ROTATION

        self.head = self.__get_direction()

    def spaceship_movement_handling(self, keys: List[bool]) -> None:
        """
        Method that calls the specific movement function
        from the pressed button
        """

        if keys[K_w]:
            self.__move_forward_and_back()
        elif keys[K_s]:
            self.__move_forward_and_back(False)

        if keys[K_a]:
            self.__rotate(False)
        elif keys[K_d]:
            self.__rotate()

    def __get_direction(self) -> Vector2D:
        new_x = (self.position.x_coord + get_sin_or_cos(self.angle) *
                self.image.get_width() // 2)
        new_y = (self.position.y_coord - get_sin_or_cos(self.angle, False) *
                self.image.get_height() // 2)

        return Vector2D(new_x, new_y)

    def shooting(self) -> Bullet:
        """
        Method that create a bullet and returns it
        """

        bullet_velocity = self.__get_bulet_velocity()
        bullet = Bullet(self.head.to_tuple(), bullet_velocity.to_tuple())
        bullet.angle = self.angle

        return bullet

    def __get_bulet_velocity(self) -> Vector2D:
        new_x = (self.head.x_coord * 0.8) * (self.SPEED * get_sin_or_cos(self.angle, False))
        new_y = (self.head.y_coord * 0.8) * (self.SPEED * get_sin_or_cos(self.angle))

        return Vector2D(new_x, new_y)
