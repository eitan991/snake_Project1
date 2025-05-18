import pygame
import sys

# init pygame
pygame.init()

# Screen Size
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Title
pygame.display.set_caption("Snake Game")

# Clock
clock = pygame.time.Clock()

# Main game loop
runing = True
while runing : 
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runing = False

    # Fill screen with background color (e.g., black)
    screen.fill((0, 0, 0))

    # Update display
    pygame.display.flip()

    # Limit FPS
    clock.tick(10)

# Quit Pygame
pygame.quit()
sys.exit()