import pygame

from image_loading import load_image

class AsteroidsGame:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Asteroids")

        self.screen = pygame.display.set_mode((800, 600))
        self.background = load_image("background")

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
        pass

    def __drawing(self):
        self.screen.blit(self.background, (0, 0))
        pygame.display.flip()

    def __quit_game(self, event):
        return event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE)

