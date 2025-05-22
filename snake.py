import pygame
import sys
import random

# init pygame
pygame.init()

# Screen Size
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Sanke block size
block_size = 20 
# Starting pos for snake
snake_pos = [(WIDTH // 2, HEIGHT // 2)]

# Velocity
velocity =[0,0] # so the snake would keep moving without constant input

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
        # Key preses handeling
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and velocity[1] == 0:
                velocity = [0, -block_size]
            elif event.key == pygame.K_DOWN and velocity[1] == 0:
                velocity = [0, block_size]
            elif event.key == pygame.K_LEFT and velocity[0] == 0:
                velocity = [-block_size, 0]
            elif event.key == pygame.K_RIGHT and velocity[0] == 0:
                velocity = [block_size, 0]


    head_x, head_y = snake_pos[0]
    head_x += velocity[0]
    head_y += velocity[1]
    snake_pos[0] = (head_x, head_y)



    # Fill screen with background color (e.g., black)
    screen.fill((0, 0, 0))

    for pos in snake_pos :
        pygame.draw.rect(screen, (0, 255, 0), (pos[0], pos[1], block_size, block_size))
    # Update display
    pygame.display.flip()

    # Limit FPS
    clock.tick(5)

# Quit Pygame
pygame.quit()
sys.exit()