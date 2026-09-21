"""Shoting projectiles render package."""

import pygame

from circleshape import CircleShape
from constants import SHOT_REDIUS, LINE_WIDTH


class Shot(CircleShape):
    """Shoting projectile stripes."""
    
    def __init__(self, x: float, y: float, radius: float = SHOT_REDIUS):
        """Contructor for shots."""
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(
            screen,
    color="white",
            center=self.position,
            radius=self.radius,
            width=LINE_WIDTH               
        )
    
    def update(self, dt):
        self.position += self.velocity * dt