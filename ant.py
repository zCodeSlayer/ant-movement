from typing import Tuple
from collections import deque
from enum import IntEnum


class MovementDirection(IntEnum):
    UP: int = 1
    DOWN: int = 2
    LEFT: int = 3
    RIGHT: int = 4


class Ant:
    def __init__(self, x_position: int, y_position: int, movement_direction: int, step: int = 1):
        self.x = x_position
        self.y = y_position
        self.step = step
        self.movement_direction = movement_direction

        if self.movement_direction not in [direction.value for direction in MovementDirection]:
            raise Exception("Unknown movement direction!")

    def move(self, x: int, y: int):
        self.x = x
        self.y = y

    def look_forward_next_position(self) -> Tuple[int, int]:
        match self.movement_direction:
            case MovementDirection.UP:
                return self.x, self.y + self.step
            case MovementDirection.DOWN:
                return self.x, self.y - self.step
            case MovementDirection.RIGHT:
                return self.x + self.step, self.y
            case MovementDirection.LEFT:
                return self.x - self.step, self.y
            case _:
                raise Exception("Unknown movement direction!")

    def rotate_direction(self, expandable_direction: int):
        ordered_direction: deque = deque(
            (MovementDirection.UP, MovementDirection.RIGHT, MovementDirection.DOWN, MovementDirection.LEFT),
            maxlen=4
        )

        direction: MovementDirection = ordered_direction.pop()
        while direction is not self.movement_direction:
            ordered_direction.appendleft(direction)
            direction = ordered_direction.pop()
        else:
            ordered_direction.append(direction)

        match expandable_direction:
            case MovementDirection.LEFT:
                for _ in range(2):
                    direction = ordered_direction.pop()
                    ordered_direction.appendleft(direction)
            case MovementDirection.RIGHT:
                direction = ordered_direction.popleft()
                ordered_direction.append(direction)
            case _:
                raise Exception("Unknown direction to rotation!")

        self.movement_direction = direction
