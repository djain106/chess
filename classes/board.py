"""A chess board and its interactions."""

import constants

from typing import Sequence
from pieces import BasePiece

_BOARD_SIZE = 8


class BoardSquare:
    """A square on a chess board."""

    def __init__(self, x: int, y: int, color: constants.Color, piece: BasePiece | None = None) -> None:
        validate_coordinates(x, y)
        self._x = x
        self._y = y
        self._color = color
        # Ensure that the piece is on the correct square.
        piece.set_x(self._x)
        piece.set_y(self._y)
        self._piece = piece

    def __str__(self) -> str:
        return f'BoardSquare(x: {self._x}, y: {self._y}, color: {self._color.value}, piece: {self._piece})'


class Board:
    """A basic chess board."""

    def __init__(self) -> None:
        """Initializes a basic chess board."""
        board = {}
        for i in range(constants.BOARD_SIZE):
            for j in range(constants.BOARD_SIZE):
                board[(i, j)] = BoardSquare(i, j)


def validate_coordinates(x: int, y: int) -> bool:
    if x < 0 or x >= constants.BOARD_SIZE or y < 0 or y >= constants.BOARD_SIZE:
        raise ValueError(
            f'Invalid x ({x}) or y ({y}) coorindate for board size of {constants.BOARD_SIZE}.')
