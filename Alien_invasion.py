import sys
import pygame


class AlienInvasion :
    """ Overall class to manage game asses and behavior"""

    def __init__(self):
        """Initialize the game, and greate gaame resources"""
        pygame.init()

        self.screen = pygame.display.set_mode((1200,800))
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            #Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            #Make the most recently drawn screen visible
            pygame.display.flip()