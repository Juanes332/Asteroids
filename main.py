import pygame

from constants import *


def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    running = True

    while running:
        # poll for events
        # pygame.QUIT event means the user clicked x to close your window

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Fill the screen with a color wipe away anything form the last frame
        screen.fill("black")

        # flip() the display to put your work on the screen
        pygame.display.flip()

        clock.tick(60)  # Limits FPS to 60


if __name__ == "__main__":
    main()
