import pygame

class SpaceShip:
    """A class to manage the space ship"""
    
    def __init__(self, ai_game): # ai_game is an instance of AlienInvasion class
        """Initialize the space ship and set its starting position"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        
        # Load the ship image and get its rect
        self.image = pygame.image.load('images/space_ship.bmp')
        self.rect = self.image.get_rect()
        
        # Start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom
        
        # Store a float for the ship's exact horizontal position
        self.x = float(self.rect.x)
        
        # Movement flag: start with a ship that's not moving
        self.moving_right = False
        self.moving_left = False
    
    def update(self):
        """Update the ship'S position based on the movement flag"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.space_ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.space_ship_speed
            
        # Update the rect object from self.x
        self.rect.x = self.x
        
    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)
        
    