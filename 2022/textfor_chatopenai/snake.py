# Import necessary modules
import pygame
import random

# Initialize the game
pygame.init()

# Set screen width and height
width = 600
height = 600

# Create the screen
screen = pygame.display.set_mode((width, height))

# Set title and icon
pygame.display.set_caption("Snake Game")
icon = pygame.image.load('snake.png')
pygame.display.set_icon(icon)

# Set colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)

# Set FPS
fps = 10

# Set snake initial position
snake_x = width / 2
snake_y = height / 2

# Set snake initial direction
snake_dir = "right"

# Set snake body list
snake_body = []

# Set snake initial length
snake_len = 1

# Set food initial position
food_x = random.randint(20, width - 20)
food_y = random.randint(20, height - 20)

# Set game over flag
game_over = False

# Define snake movement


def move_snake():
    global snake_x, snake_y, snake_dir, snake_body, snake_len, food_x, food_y

    # Move the snake in the current direction
    if snake_dir == "right":
        snake_x += 20
    elif snake_dir == "left":
        snake_x -= 20
    elif snake_dir == "up":
        snake_y -= 20
    elif snake_dir == "down":
        snake_y += 20

    # Check if the snake has collided with the food
    if snake_x == food_x and snake_y == food_y:
        # Increase the snake length
        snake_len += 1

        # Generate new food at a random position
        food_x = random.randint(20, width - 20)
        food_y = random.randint(20, height - 20)
    else:
        # Pop the last element from the snake body list
        snake_body.pop()

    # Insert the new position of the snake head at the beginning of the list
    snake_body.insert(0, (snake_x, snake_y))

# Define a function to draw the snake on the screen


def draw_snake():
    for x, y in snake_body:
        # Draw the snake body
        pygame.draw.rect(screen, green, (x, y, 20, 20))

        # Draw the snake eyes
        pygame.draw.circle(screen, black, (x + 8, y + 8), 4)
        pygame.draw.circle(screen, black, (x + 12, y + 8), 4)

# Define a function to draw the food on the screen


def draw_food():
    # Draw the food
    pygame.draw
