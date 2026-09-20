"""Player object."""
import pygame

from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, LINE_WIDTH


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
    
    def update(self, dt):
        """Move player object."""
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        