import random

import pygame

from circleshape import CircleShape
from constants import *


class Asteroid(CircleShape):
    containers = ()

    def __init__(self, x, y, radius):
        pygame.sprite.Sprite.__init__(self, self.containers)
        super().__init__(x, y, radius)
        self.radius = radius
        self.image = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
        self.rect = self.image.get_rect(center=(x, y))

    def draw(self, surface):
        pygame.draw.circle(surface, (200, 200, 200),
                           self.rect.center, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
        self.rect.center = (int(self.position.x), int(self.position.y))

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        # Calcular nuevo radio
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        # Ángulo aleatorio entre 20 y 50 grados
        angle = random.uniform(20, 50)

        # Calcular nuevas direcciones rotadas
        vel1 = self.velocity.rotate(angle) * 1.2
        vel2 = self.velocity.rotate(-angle) * 1.2

        # Crear nuevos asteroides en la misma posición
        Asteroid(self.position.x, self.position.y, new_radius).velocity = vel1
        Asteroid(self.position.x, self.position.y, new_radius).velocity = vel2
