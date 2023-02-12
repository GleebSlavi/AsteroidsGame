"""
Module that creates an AsteroidGame object
and starts the game
"""

from src.game import AsteroidsGame

if __name__ == "__main__":
    asteroids = AsteroidsGame()
    asteroids.start_game()
