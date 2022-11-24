from direction import Direction


class Snake:
    def __init__(
        self, x: int = 0, y: int = 0, direction: Direction = Direction.RIGHT
    ) -> None:
        self.x: int = x
        self.y: int = y
        self.direction: Direction = direction

    def move(self, direction: Direction) -> tuple:
        if direction == Direction.UP and self.direction != Direction.DOWN:
            self.direction = Direction.UP
        elif direction == Direction.DOWN and self.direction != Direction.UP:
            self.direction = Direction.DOWN
        elif direction == Direction.RIGHT and self.direction != Direction.LEFT:
            self.direction = Direction.RIGHT
        elif direction == Direction.LEFT and self.direction != Direction.RIGHT:
            self.direction = Direction.LEFT

        if self.direction == Direction.UP:
            self.y += 1
        elif self.direction == Direction.DOWN:
            self.y -= 1
        elif self.direction == Direction.RIGHT:
            self.x += 1
        else:
            self.x -= 1

        return self.x, self.y

    def extend(self) -> None:
        pass
