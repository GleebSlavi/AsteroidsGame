import pygame
from pygame import event, mixer, font
from typing import List, Tuple

from game_objects.spaceship import Spaceship
from game_objects.asteroid import Asteroid
from game_objects.bullet import Bullet

from game_objects.game_objects_helpers.two_dimensional_vector import Vector2D

from utilities.helper_functions import (get_random_coordinates, 
        load_image, load_sound, get_highest_score,
        safe_highest_score, print_text_on_screen)

class AsteroidsGame:
    HIGHEST_SCORE: int = get_highest_score()
    MIN_ASTEROID_DISTANCE: int = 300

    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Asteroids")
        self.screen = pygame.display.set_mode((1000, 666))
        self.background = load_image("background")

        self.game_over_font = font.Font(None, 80)
        self.score_font = font.Font(None, 30)
        self.new_high_score_font = font.Font(None, 60)

        self.spaceship = Spaceship((500, 333))
        self.bullets = []
        self.asteroids = self.__create_multiple_asteroids(6)

        self.clock = pygame.time.Clock()
        self.score = 0
        self.new_high_score = False

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
        if self.spaceship and self.__spaceship_moving(keys):
            self.spaceship.spaceship_movement_handling(keys, self.screen)
                

    def __game_logic_processing(self) -> None:
        self.__move_objects()

        if self.spaceship and self.__asteroid_collision(self.spaceship):
            self.spaceship = None

            if self.score > self.HIGHEST_SCORE:
                self.HIGHEST_SCORE = self.score
                safe_highest_score(self.HIGHEST_SCORE)
                self.new_high_score = True

        for bullet in self.bullets:
            asteroid = self.__asteroid_collision(bullet)
            if asteroid:
                self.asteroids.remove(asteroid)
                self.bullets.remove(bullet)
                self.__create_new_asteroids(asteroid.size, asteroid.position)
                self.__add_score(asteroid.size)

                if self.asteroids.count() <= 4:
                    self.__create_multiple_asteroids(3)

    def __drawing(self) -> None:
        self.screen.blit(self.background, (0, 0))

        for game_object in self.__get_game_objects():
            if game_object:
                game_object.object_drawing(self.screen)

        print_text_on_screen(self.screen, self.score_font, f"Highest Score: {self.HIGHEST_SCORE}",
                             (85, 15))
        print_text_on_screen(self.screen, self.score_font, f"Score: {self.score}", (45, 35))

        if not self.spaceship:
            print_text_on_screen(self.screen, self.game_over_font, "Game Over!",
                                 (500, 333))

        if self.new_high_score:
            print_text_on_screen(self.screen, self.new_high_score_font, "New High Score!",
                                 (500, 390))

        pygame.display.flip()
        self.clock.tick(60)

    def __quit_game(self, event: event) -> bool:
        return event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE)

    def __spaceship_moving(self, keys: List[bool]) -> bool:
        return any([keys[pygame.K_w], keys[pygame.K_s], keys[pygame.K_a], keys[pygame.K_d]])

    def __get_game_objects(self) -> List[Asteroid | Bullet | Spaceship]:
        objects =  [*self.asteroids, *self.bullets, self.spaceship]

        return objects

    def __create_multiple_asteroids(self, count: int = 6) -> List[Asteroid]:
        asteroids = []
        for _ in range(count):
            position = get_random_coordinates(self.screen)
            while (position.euclidean_distance(self.spaceship.position)
                    <= self.MIN_ASTEROID_DISTANCE):
                position = get_random_coordinates(self.screen)

            asteroids.append(Asteroid(position.to_tuple()))

        return asteroids

    def __move_objects(self) -> None:
        for game_object in self.__get_game_objects():
            if game_object:
                game_object.object_moving(self.screen)

    def __asteroid_collision(self, other_object) -> Asteroid | None:
        for asteroid in self.asteroids:
            if asteroid.object_collision(other_object):
                return asteroid

        return None

    def __create_new_asteroids(self, asteroid_size: int, position: Vector2D) -> None:
        if asteroid_size < 3:
            for _ in range(2):
                self.asteroids.append(Asteroid(position.to_tuple(), asteroid_size + 1))

    def __add_score(self, asteroid_size: int) -> None:
        points = {
            1: 50,
            2: 25,
            3: 10
        }

        self.score += points[asteroid_size]

