"""Constants for the chess game."""

import enum

BOARD_SIZE = 8


class Color(enum.Enum):
    BLACK = 'black'
    WHITE = 'white'


def validate_coordinates(x: int, y: int) -> bool:
    if x < 0 or x >= BOARD_SIZE or y < 0 or y >= BOARD_SIZE:
        raise ValueError(
            f'Invalid x ({x}) or y ({y}) coorindate for board size of {BOARD_SIZE}.')
