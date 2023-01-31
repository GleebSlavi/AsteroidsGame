import pygame
from pygame import event, mixer, font, Color
from typing import List

from game_objects.spaceship import Spaceship
from game_objects.asteroid import Asteroid
from game_objects.bullet import Bullet

from utilities.helper_functions import (get_random_coordinates, 
        load_image, load_sound, print_game_over_text)

class AsteroidsGame:
    MIN_ASTEROID_DISTANCE: int = 250

    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Asteroids")

        self.screen = pygame.display.set_mode((1000, 667))
        self.background = load_image("background")
        self.clock = pygame.time.Clock()
        self.font = font.Font(None, 80)

        self.spaceship = Spaceship((500, 333))
        self.bullets = []
        self.asteroids = self.__create_multiple_asteroids()

        self.is_destroyed = False

    def start_game(self) -> None:
        load_sound("game_song", mixer)
        mixer.music.play(loops=-1)

        while True:
            self.__input_handling()
            self.__game_logic_processing()
            self.__drawing()

    def __input_handling(self) -> None:
        for event in pygame.event.get():
            if self.__quit_game(event):
                quit()
        
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.spaceship.rotate(False)
        elif keys[pygame.K_RIGHT]:
            self.spaceship.rotate()
                

    def __game_logic_processing(self) -> None:
        self.__move_objects()

        if self.__asteroid_collision(self.spaceship):
            self.is_destroyed = True



    def __drawing(self) -> None:
        self.screen.blit(self.background, (0, 0))
        
        for game_object in self.__get_game_objects():
            game_object.object_drawing(self.screen)

        if self.is_destroyed:
            print_game_over_text(self.screen, self.font)

        pygame.display.flip()
    
        self.clock.tick(60)

    def __quit_game(self, event: event) -> bool:
        return event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE)

    def __move_spaceship(self, event: event) -> bool:
        return event.type == pygame.KEYDOWN and event.key in (pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT)

    def __get_game_objects(self) -> List[Asteroid | Bullet | Spaceship]:
        objects =  [*self.asteroids, *self.bullets, self.spaceship]

        return objects

    def __create_multiple_asteroids(self) -> List[Asteroid]:
        asteroids = []
        for _ in range(6):
            position = get_random_coordinates(self.screen)
            while (position.euclidean_distance(self.spaceship.position)
                    <= self.MIN_ASTEROID_DISTANCE):
                position = get_random_coordinates(self.screen)

            asteroids.append(Asteroid(position.to_tuple()))

        return asteroids

    def __move_objects(self):
        for game_object in self.__get_game_objects():
            game_object.object_moving(self.screen)


    def __asteroid_collision(self, other_object):
        for asteroid in self.asteroids:
            if asteroid.object_collision(other_object):
                return True

        return False

