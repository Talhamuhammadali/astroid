"""Player object."""
import pygame

from circleshape import CircleShape
from constants import (
    PLAYER_RADIUS,
    PLAYER_TURN_SPEED,
    PLAYER_SPEED,
    PLATER_SHOOT_SPEED,
    LINE_WIDTH
)
from shot import Shot


class Player(CircleShape):
    """Player repersentation on the screen. Hit-box is circular but looks like triangle."""
    
    def __init__(self, x: float, y: float, radius: float = PLAYER_RADIUS ):
        super().__init__(x, y, radius)
        self.rotation : int = 0
    
    def triangle(self) -> list[pygame.Vector2]:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)   
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        
        a = self.position + forward * self.radius   
        b = self.position - forward * self.radius - right 
        c = self.position - forward * self.radius + right
        
        return [a ,b, c]  
    
    def draw(self, screen):
        """Render Player on screen."""
        pygame.draw.polygon(surface=screen, color="white", points=self.triangle(), width=LINE_WIDTH)
    
    def rotate(self, dt):
        """Rotate the player object"""
        self.rotation +=  PLAYER_TURN_SPEED * dt
    
    def move(self, dt):
        """Move the playe object."""
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * dt
        self.position += rotated_with_speed_vector
    
    def update(self, dt):
        """Move player object."""
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()

    def shoot(self):
        """Shoot mechanism for player."""
        shot = Shot(x=self.position[0], y=self.position[1])
        shot_vec = pygame.Vector2(0, 1).rotate(self.rotation)
        shot.velocity = shot_vec * PLATER_SHOOT_SPEED