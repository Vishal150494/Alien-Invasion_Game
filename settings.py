class Settings:
    """A class to store all settings for the game"""
    
    def __init__(self):
        """Initialize game's settings"""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_colour = (63, 72, 204)
        
        # Space ship settings
        self.space_ship_speed = 1.5 # Moves 1.5 pixels while moving left or right
        
        # Bullet settings
        self.bullet_speed = 2.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_colour = (60, 60, 60)
        self.bullets_allowed = 6