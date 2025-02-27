import pygame
import sys
from settings import Settings
from space_ship import SpaceShip
from bullet import Bullet

class AlienInvasion:
    """ Overall class to manage game assets and behavior """
    
    def __init__(self):
        """ Initialize the game, and create game resources (background) """
        pygame.init() # Initialize the background settings that Pygame needs to work properly
        self.clock = pygame.time.Clock() # Create a clock object to control the speed of the game (frame rate)
        self.settings = Settings() # Create an instance of Settings class
        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN) # Create a display window, where all game graphics are drawn. Its a surface.
        self.settings.screen_width = self.screen.get_rect().width # Set the screen width to the width of the display window
        self.settings.screen_height = self.screen.get_rect().height # Set the screen height to the height of the display window
        pygame.display.set_caption("Alien Invasion") # A surface is a part of the screen where a game element can be displayed, for ex, here the window.
        self.bg_colour  = self.settings.bg_colour # Set the background colour
        self.space_ship = SpaceShip(self) # Create an instance of SpaceShip class. self refers to the current instance of AlienInvasion class.
        self.bullets = pygame.sprite.Group() # Create a group to store bullets
        
    def run_game(self):
        """ Start the main loop for the game """
        while True:
            # Watch for keyboard and mouse events
            self._check_events()
            self.space_ship.update()
            self._update_bullets()
            self._update_screen()
            self.clock.tick(60) # pygame will make the loop run exactly 60 times per second
            
    def _check_events(self):
        """Helper func: Respond to key presses and mouse events"""
        for event in pygame.event.get(): # event loop, listens for events and performs appropriate tasks. Returns a list of events.
            if event.type == pygame.QUIT:
                sys.exit()
                
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
                    
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
                
    def _check_keydown_events(self, event):
        """Helper func: Respond to key down events"""
        if event.key == pygame.K_RIGHT:
            # Move ship to the right
            self.space_ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            # Move ship to right
            self.space_ship.moving_left = True
        elif event.key ==pygame.K_q:
            # Quit the game when user presses 'Q'
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
    
    def _check_keyup_events(self, event):
        """Helper func: Respond to key up events"""
        if event.key == pygame.K_RIGHT:
            # Stop moving the ship
            self.space_ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            # Stop moving the ship
            self.space_ship.moving_left = False
            
    def _fire_bullet(self):
        """Helper func: Create a new bullet and add it to the bullets group"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
            
    def _update_bullets(self):
        """Helper func: Update position of bullets and get rid of old bullets"""
        # Update bullet position
        self.bullets.update()
        
        # Get rid of bullets that have disappeared
        for bullet in self.bullets.copy(): # copy() method is used to modify a list while looping through it
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        #print(len(self.bullets))
                
    def _update_screen(self):
        """Helper func: Update images on screen, & flip to new screen"""
        # Redraw the screen during each pass through the loop
        self.screen.fill(self.bg_colour)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.space_ship.blitme()
        
        # Make the most recent drawn screen visible
        pygame.display.flip()
            
if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()
        