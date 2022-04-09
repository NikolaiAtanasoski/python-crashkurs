import sys
import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet


class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self.ship.update_position()
            self._update_bullets()
            self._update_screen()

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_press(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_press(event)

    def _check_keydown_press(self, event):
        if event.key in (pygame.K_RIGHT, pygame.K_LEFT):
            self._change_ship_velocity(event)
        if event.key == pygame.K_SPACE:
            self._fire_bullet()
        else:
            self._check_other_keydown_keys(event)

    def _check_other_keydown_keys(self, event):
        if event.key == pygame.K_q:
            print("q pressed, exiting game")
            pygame.quit()
            sys.exit()

    def _check_keyup_press(self, event):
        if event.key in (pygame.K_RIGHT, pygame.K_LEFT):
            self._change_ship_velocity(event)

    def _change_ship_velocity(self, event):
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                self.ship.x_velocity += -1
            elif event.key == pygame.K_LEFT:
                self.ship.x_velocity += 1
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                self.ship.x_velocity += 1
            elif event.key == pygame.K_LEFT:
                self.ship.x_velocity += -1

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group"""
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Update positions of bullets and get rid of old bullets"""
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.background_color)
        self.ship.blitme()

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        pygame.display.flip()


if __name__ == "__main__":
    # Make a game instance, and run the game.
    alien_invasion = AlienInvasion()
    alien_invasion.run_game()
