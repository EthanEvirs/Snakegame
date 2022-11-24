from operator import truediv
from random import random
from turtle import down, up, width
import pygame
import random

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

SQUARE_WIDTH = 20
SQUARE_HEIGHT = 20

NUM_TILES_X = int(SCREEN_WIDTH / SQUARE_WIDTH)
NUM_TILES_Y = int(SCREEN_HEIGHT / SQUARE_HEIGHT)

FRAMERATE = 30

BACKGROUND_COLOR = (23, 25, 35)
FRUIT_COLOR = (255, 0, 0)
SNAKE_COLOR = (0, 255, 0)

UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def draw_square(point, color):
    new_x = point.x * SQUARE_WIDTH
    new_y = SCREEN_HEIGHT - SQUARE_HEIGHT - point.y * SQUARE_HEIGHT
    pygame.draw.rect(screen, color, (new_x, new_y, SQUARE_WIDTH, SQUARE_HEIGHT))


def draw_fruit(point):
    draw_square(point, FRUIT_COLOR)


def draw_snake(point):
    draw_square(point, SNAKE_COLOR)


pygame.init()
screen = pygame.display.set_mode([500, 500])
clock = pygame.time.Clock()
running = True

while running:
    # game starting
    pos = Point(random.randint(0, NUM_TILES_X - 1), random.randint(0, NUM_TILES_Y - 1))
    direction = -1
    paused = True
    dead = False

    while not dead and running:
        # handle events

        button_pressed = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # read keyboard
            elif event.type == pygame.KEYDOWN:
                if not button_pressed:
                    if event.key == pygame.K_UP:
                        if direction != DOWN:
                            direction = UP
                            button_pressed = True
                        paused = False
                    elif event.key == pygame.K_DOWN:
                        if direction != UP:
                            direction = DOWN
                            button_pressed = True
                        paused = False
                    elif event.key == pygame.K_LEFT:
                        if direction != RIGHT:
                            direction = LEFT
                            button_pressed = True
                        paused = False
                    elif event.key == pygame.K_RIGHT:
                        if direction != LEFT:
                            direction = RIGHT
                            button_pressed = True
                        paused = False
                if event.key == pygame.K_SPACE:
                    paused = True

        # update postion
        if not paused:
            if direction == UP:
                if pos.y < NUM_TILES_Y - 1:
                    pos.y += 1
                else:
                    dead = True
            elif direction == DOWN:
                if pos.y > 0:
                    pos.y -= 1
                else:
                    dead = True
            elif direction == LEFT:
                if pos.x > 0:
                    pos.x -= 1
                else:
                    dead = True
            elif direction == RIGHT:
                if pos.x < NUM_TILES_X - 1:
                    pos.x += 1
                else:
                    dead = True

        # set the screen color
        screen.fill(BACKGROUND_COLOR)
        square_color = FRUIT_COLOR

        draw_snake(pos)

        # update the display
        pygame.display.flip()
        clock.tick(FRAMERATE)


pygame.quit()
