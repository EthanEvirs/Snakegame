from direction import Direction
import pygame
import random
from snake import Snake


class Game:
    SCREEN_WIDTH = 500
    SCREEN_HEIGHT = 500

    FRAMERATE = 10

    SQUARE_WIDTH = 20
    SQUARE_HEIGHT = 20

    BACKGROUND_COLOR = (23, 25, 35)
    FRUIT_COLOR = (255, 0, 0)
    SNAKE_COLOR = (0, 255, 0)

    NUM_TILES_X = int(SCREEN_WIDTH / SQUARE_WIDTH)
    NUM_TILES_Y = int(SCREEN_HEIGHT / SQUARE_HEIGHT)

    key_to_direction_map: dict = {
        pygame.K_UP: Direction.UP,
        pygame.K_DOWN: Direction.DOWN,
        pygame.K_RIGHT: Direction.RIGHT,
        pygame.K_LEFT: Direction.LEFT,
    }

    def __init__(self) -> None:
        pygame.init()

        self.screen = pygame.display.set_mode([self.SCREEN_WIDTH, self.SCREEN_HEIGHT])
        self.clock = pygame.time.Clock()
        self.snake_x: int
        self.snake_y: int

    def check_collisions(self, x: int, y: int) -> bool:
        return x < 0 or x >= self.NUM_TILES_X or y < 0 or y >= self.NUM_TILES_Y

    def render_square(self, x: int, y: int, color: tuple) -> tuple:
        square_x = x * self.SQUARE_WIDTH
        square_y = self.SCREEN_HEIGHT - self.SQUARE_HEIGHT - y * self.SQUARE_HEIGHT
        pygame.draw.rect(
            self.screen,
            color,
            (square_x, square_y, self.SQUARE_WIDTH, self.SQUARE_HEIGHT),
        )

    def render(self) -> None:
        self.screen.fill(self.BACKGROUND_COLOR)
        # draw the snake
        self.render_square(self.snake_x, self.snake_y, self.SNAKE_COLOR)
        # draw the fruit
        # self.render_square(
        #     self.snake_x,
        #     self.snake_y,
        #     self.SNAKE_COLOR
        # )
        pygame.display.flip()

    def loop(self) -> None:
        while True:
            dead: bool = False
            paused: bool = False
            direction: Direction = Direction.RIGHT
            snake: Snake = Snake(
                random.randint(0, self.NUM_TILES_X - 1),
                random.randint(0, self.NUM_TILES_Y - 1),
            )

            while not dead:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        return

                    elif event.type == pygame.KEYDOWN:
                        if event.key in self.key_to_direction_map:
                            direction = self.key_to_direction_map[event.key]

                        elif event.key == pygame.K_SPACE:
                            paused = True

                if not paused:
                    x, y = snake.move(direction)
                    if not self.check_collisions(x, y):
                        self.snake_x = x
                        self.snake_y = y
                    else:
                        dead = True

                self.render()
                self.clock.tick(self.FRAMERATE)


game: Game = Game()
game.loop()
