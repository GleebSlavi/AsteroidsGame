"""
Module that contains AsteroidGame class
"""

from typing import List, Tuple

import pygame

from src.game_objects.spaceship import Spaceship
from src.game_objects.asteroid import Asteroid
from src.game_objects.bullet import Bullet

from src.game_objects.game_objects_helpers.two_dimensional_vector import Vector2D

from src.helper_functions import (get_random_coordinates,
        load_image, load_sound, get_highest_score,
        safe_highest_score, print_text_on_screen)

class AsteroidsGame:
    """
    The main class in the project that starts the game
    """

    HIGHEST_SCORE: int = get_highest_score()
    MIN_ASTEROID_DISTANCE: int = 300

    def __init__(self):
        pygame.init()

        pygame.display.set_caption("Asteroids")
        self.screen = pygame.display.set_mode((1000, 666))
        self.background = load_image("background")

        self.music_game_sound = load_sound("game_song")
        self.bullet_shot_sound = load_sound("bullet_shot")

        self.game_over_font = pygame.font.Font(None, 80)
        self.score_font = pygame.font.Font(None, 35)
        self.new_high_score_font = pygame.font.Font(None, 60)

        self.spaceship = Spaceship((500, 333))
        self.bullets = []
        self.asteroids = self.__create_multiple_asteroids()

        self.clock = pygame.time.Clock()
        self.score = 0
        self.new_high_score = False

    def start_game(self) -> None:
        """
        Method that play the game sound and then has
        an endless loop where implements the game
        three main things
        """

        channel = pygame.mixer.Channel(0)
        channel.play(self.music_game_sound, loops=-1)

        while True:
            self.__input_handling()
            self.__game_logic_processing()
            self.__drawing()

    def __input_handling(self) -> None:
        for event in pygame.event.get():
            if self.__quit_game(event):
                quit()
            elif self.spaceship and event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.bullets.append(self.spaceship.shooting())

                channel = pygame.mixer.Channel(1)
                channel.play(self.bullet_shot_sound)

        keys = pygame.key.get_pressed()
        if self.spaceship and self.__spaceship_moving(keys):
            self.spaceship.spaceship_movement_handling(keys)

    def __game_logic_processing(self) -> None:
        self.__move_objects()

        if self.spaceship and self.__asteroid_collision(self.spaceship):
            self.spaceship = None

            if self.score > self.HIGHEST_SCORE:
                safe_highest_score(self.score)
                self.new_high_score = True

        for bullet in self.bullets:
            asteroid = self.__asteroid_collision(bullet)
            if asteroid:
                del self.asteroids[asteroid[0]]
                self.bullets.remove(bullet)
                self.__create_new_asteroids(asteroid[1].size, asteroid[1].position)
                self.__add_score(asteroid[1].size)

                if len(self.asteroids) <= 4:
                    self.asteroids = self.asteroids + self.__create_multiple_asteroids(5)


    def __drawing(self) -> None:
        self.screen.blit(self.background, (0, 0))

        for game_object in self.__get_game_objects():
            game_object.object_drawing(self.screen)

        print_text_on_screen(self.screen, self.score_font, f"Highest Score: {self.HIGHEST_SCORE}",
                             (self.screen.get_width() // 2, 15))
        print_text_on_screen(self.screen, self.score_font, f"{self.score}",
                            (self.screen.get_width() // 2, 45))

        if not self.spaceship:
            print_text_on_screen(self.screen, self.game_over_font, "Game Over!",
                                 (500, 333))

        if self.new_high_score:
            print_text_on_screen(self.screen, self.new_high_score_font, "New High Score!",
                                 (500, 390))

        pygame.display.flip()
        self.clock.tick(60)

    def __quit_game(self, event: pygame.event) -> bool:
        return event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and
                event.key == pygame.K_ESCAPE)

    def __spaceship_moving(self, keys: List[bool]) -> bool:
        return any([keys[pygame.K_w], keys[pygame.K_s], keys[pygame.K_a], keys[pygame.K_d]])

    def __get_game_objects(self) -> List[Asteroid | Bullet | Spaceship]:
        objects =  [*self.asteroids, *self.bullets]

        if self.spaceship:
            objects.append(self.spaceship)

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

            if isinstance(game_object, Bullet) and game_object.is_out_of_screen:
                self.bullets.remove(game_object)

    def __asteroid_collision(self, other_object) -> Tuple[int, Asteroid] | None:
        for i, asteroid in enumerate(self.asteroids):
            if asteroid.object_collision(other_object):
                return (i, asteroid)

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
