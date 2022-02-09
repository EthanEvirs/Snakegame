from operator import truediv
from turtle import width
import pygame

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

SQUARE_WIDTH = 20
SQUARE_HEIGHT = 20

NUM_TILES_X = SCREEN_WIDTH / SQUARE_WIDTH
NUM_TILES_Y = SCREEN_HEIGHT / SQUARE_HEIGHT

BACKGROUND_COLOR = (25, 25, 25)
FRUIT_COLOR = (255, 0, 0)
SNAKE_COLOR = (0, 255, 0)


def draw_square(x, y, color):
    new_x = x * SQUARE_WIDTH
    new_y = SCREEN_HEIGHT - SQUARE_HEIGHT - y * SQUARE_HEIGHT
    pygame.draw.rect(screen, color, (new_x, new_y, SQUARE_WIDTH, SQUARE_HEIGHT))


def draw_fruit(x, y):
    draw_square(x, y, FRUIT_COLOR)


def draw_snake(x, y):
    draw_square(x, y, SNAKE_COLOR)


pygame.init()
screen = pygame.display.set_mode([500, 500])

running = True

while running:
    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # set the screen color
    screen.fill(BACKGROUND_COLOR)

    draw_fruit(0, 0)
    draw_snake(24, 24)

    square_color = FRUIT_COLOR

    # update the display
    pygame.display.flip()

pygame.quit()
