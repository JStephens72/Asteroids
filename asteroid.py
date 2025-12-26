import pygame
import random
from logger import log_event
from constants import (
    LINE_WIDTH,
    ASTEROID_MIN_RADIUS,
    ASTEROID_MAX_RADIUS,
)
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            angle = random.uniform(20, 50)
            
            v = self.velocity.rotate(angle)
            child_asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)

            child_asteroid_1.velocity = v * 1.2


            v =self.velocity.rotate(-angle)
            child_asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
            child_asteroid_2.velocity = v * 1.2
