import pygame
import sys

class AlienInvasion:
    """ Overall class to manage game assets and behavior """
    
    def __init__(self):
        """ Initialize the game, and create game resources (background) """
        pygame.init()
        
        self.screen = pygame.display.set_mode((1200, 800)) # Create a display window, where all game graphics are drawn
        pygame.display.set_caption("Alien Invasion") 
        
    def run_game(self):
        """ Start the main loop for the game """
        while True:
            # Watch for keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                    
            # Make the most recent drawn screen visible
            pygame.display.flip()
            
if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()
        