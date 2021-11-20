import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    # A class that manages bullets fired from ship

    def __init__(self, ai_settings, screen, ship):
        # Create a bullet object from ship's current position
        super(Bullet, self).__init__()
        self.screen = screen

        # Create a bullet object at (0,0) and then set correct position
        self.rect = pygame.Rect(
            0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # store bullet's position as a decimal value
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        # Move bullet up the screen.
        self.y -= self.speed_factor
        # Update rect position.
        self.rect.y = self.y

    def draw_bullet(self):
        # Draw bullets on the screen.
        pygame.draw.rect(self.screen, self.color, self.rect)
