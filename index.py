import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 800, 600
CELL_SIZE = 20
CELL_WIDTH, CELL_HEIGHT = WIDTH // CELL_SIZE, HEIGHT // CELL_SIZE
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Snake properties
snake = [(CELL_WIDTH // 2, CELL_HEIGHT // 2)]
snake_dir = (0, 1)  # Initial direction: down
snake_speed = 6
snake_timer = pygame.time.Clock()

# Food properties
food = (random.randint(0, CELL_WIDTH - 1), random.randint(0, CELL_HEIGHT - 1))

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Handle keys for snake movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and snake_dir != (0, 1):
        snake_dir = (0, -1)
    elif keys[pygame.K_DOWN] and snake_dir != (0, -1):
        snake_dir = (0, 1)
    elif keys[pygame.K_LEFT] and snake_dir != (1, 0):
        snake_dir = (-1, 0)
    elif keys[pygame.K_RIGHT] and snake_dir != (-1, 0):
        snake_dir = (1, 0)

    # Move the snake
    new_head = (snake[0][0] + snake_dir[0], snake[0][1] + snake_dir[1])

    # Check for collision with the walls or itself
    if (
        new_head[0] < 0
        or new_head[0] >= CELL_WIDTH
        or new_head[1] < 0
        or new_head[1] >= CELL_HEIGHT
        or new_head in snake
    ):
        break

    # Check for collision with food
    if new_head == food:
        food = (random.randint(0, CELL_WIDTH - 1), random.randint(0, CELL_HEIGHT - 1))
    else:
        snake.pop()

    snake.insert(0, new_head)

    # Draw everything
    screen.fill(BLACK)
    for segment in snake:
        pygame.draw.rect(
            screen, GREEN, (segment[0] * CELL_SIZE, segment[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        )
    pygame.draw.rect(
        screen, RED, (food[0] * CELL_SIZE, food[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE)
    )

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    snake_timer.tick(snake_speed)

# Game over
font = pygame.font.SysFont(None, 72)
game_over_text = font.render("Game Over", True, WHITE)
game_over_rect = game_over_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
screen.fill(BLACK)
screen.blit(game_over_text, game_over_rect)
pygame.display.flip()

# Wait for a moment before exiting
pygame.time.wait(2000)
pygame.quit()
sys.exit()
