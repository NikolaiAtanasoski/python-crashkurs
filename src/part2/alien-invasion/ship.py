import pygame


class Ship:
    """A class to manage the ship"""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        # Load the ship image and get its rect.
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        self.x = float(self.rect.x)
        self.x_velocity = 0

    def update_position(self):
        """Update the ship's position based on the movement flag."""
        if self.x_velocity != 0 and self.is_move_legal():
            print(f"x before: {self.x} adding velocity: {self.x_velocity * self.settings.ship_speed}")
            self.x += self.x_velocity * self.settings.ship_speed
            self.rect.x = self.x
            print(f"x after: {self.x} rect.x after: {self.rect.x}")

    def is_move_legal(self):
        # right moving and not already at right end
        if self.x_velocity > 0 and self.rect.right < self.screen_rect.right:
            return True
        # left moving and not already at left end
        elif self.x_velocity < 0 and self.rect.left > 0:
            return True
        return False

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
