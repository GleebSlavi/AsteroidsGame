import pygame

from game_objects.spaceship import Spaceship
from game_objects.asteroid import Asteroid

from utilities.helper_functions import get_random_coordinates, load_image

class AsteroidsGame:
    MIN_ASTEROID_DISTANCE = 250

    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Asteroids")

        self.screen = pygame.display.set_mode((1000, 667))
        self.background = load_image("background")
        self.clock = pygame.time.Clock()

        self.spaceship = Spaceship((500, 333))
        self.bullets = []
        self.asteroids = self.__create_multiple_asteroids()

    def start_game(self):
        while True:
            self.__input_handling()
            self.__game_logic_processing()
            self.__drawing()

    def __input_handling(self):
        for event in pygame.event.get():
            if self.__quit_game(event):
                quit()

    def __game_logic_processing(self):
        #for game_object in self.__get_game_objects():
            #game_object.object_moving()
        pass

    def __drawing(self):
        self.screen.blit(self.background, (0, 0))
        
        for game_object in self.__get_game_objects():
            game_object.object_drawing(self.screen)

        pygame.display.flip()
    
        self.clock.tick(60)

    def __quit_game(self, event):
        return event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE)

    def __get_game_objects(self):
        objects =  [*self.asteroids, *self.bullets]

        if self.spaceship:
            objects.append(self.spaceship)

        return objects

    def __create_multiple_asteroids(self):
        asteroids = []
        for _ in range(6):
            position = get_random_coordinates(self.screen)
            while (position.euclidean_distance(self.spaceship.position)
                    <= self.MIN_ASTEROID_DISTANCE):
                position = get_random_coordinates(self.screen)

            asteroids.append(Asteroid(position.to_tuple()))

        return asteroids

