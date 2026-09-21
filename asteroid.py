"""Asteroid objects"""
import pygame
import random

from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS, ASTEROID_MAX_RADIUS
from logger import log_event

class Asteroid(CircleShape):
    
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)
    
    def draw(self, screen) -> None:
        pygame.draw.circle(
            screen,
            color="white",
            center=self.position,
            radius=self.radius,
            width=LINE_WIDTH
        )
    
    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")    
        angle = random.uniform(20, 50)
        ast_one_vec = self.velocity.rotate(angle)
        ast_two_vec = self.velocity.rotate(-angle)
        
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        ast_one = Asteroid(self.position.x, self.position.y, new_radius)
        ast_two = Asteroid(self.position.x, self.position.y, new_radius)
        ast_one.velocity = ast_one_vec * 1.2
        ast_two.velocity = ast_two_vec * 1.2