import pygame

from circleshape import CircleShape
from constants import SHOT_RADIUS


class Shot(CircleShape):
    containers = ()

    def __init__(self, x, y, velocity):
        pygame.sprite.Sprite.__init__(self, self.containers)
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = velocity
        self.image = pygame.Surface((SHOT_RADIUS * 2, SHOT_RADIUS * 2), pygame.SRCALPHA)
        self.rect = self.image.get_rect(center=(x, y))

    def draw(self, surface):
        pygame.draw.circle(surface, (255, 255, 0), self.rect.center, self.radius)

    def update(self, dt):
        self.position += self.velocity * dt
        self.rect.center = (int(self.position.x), int(self.position.y))
