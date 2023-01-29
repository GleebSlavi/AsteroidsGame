import pygame

from game_objects.game_object import GameObject
from image_loading import load_image

class AsteroidsGame:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Asteroids")

        self.screen = pygame.display.set_mode((1000, 667))
        self.background = load_image("background", False)
        self.clock = pygame.time.Clock()

        #self.spaceship = GameObject((400, 300), load_image("spaceship"), (0, 0))
        self.asteroid = GameObject((500, 333), load_image("asteroid"), (1, 0))

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
        #self.spaceship.object_moving()
        self.asteroid.object_moving()

    def __drawing(self):
        self.screen.blit(self.background, (0, 0))
        #self.spaceship.object_drawing(self.screen)
        self.asteroid.object_drawing(self.screen)
        pygame.display.flip()
    
        self.clock.tick(60)

    def __quit_game(self, event):
        return event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE)

