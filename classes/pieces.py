"""Pieces that are played/used in a chess game."""

from classes import constants
from typing import Sequence

# Alises.
_Color = constants.Color


class BasePiece:
    """Basic implementation for a chess piece."""
    PIECE_NAME = 'BasePiece'
    _ICONS = {}

    def __init__(self, x: int = 0, y: int = 0, color: _Color = _Color.WHITE) -> None:
        """Initializes a chess piece

        Parameters
        ----------
        x : int
            x-coordinate of the chess piece. Defaults to 0.
        y : int
            y-coordinate fo the chess piece. Defaults to 0.
        color : Color
            Color for the chess piece. Defaults to WHITE.
        """
        self._x = x
        self._y = y
        self._color = color

    def __str__(self) -> str:
        return f'{self.PIECE_NAME}(x: {self._x}, y: {self._y}, color: {self._color.value})'

    def x(self) -> int:
        """Gets the x coordinate of the piece."""
        return self._x

    def set_x(self, x: int) -> None:
        """Sets the x coordinate of the piece."""
        self._x = x

    def y(self) -> int:
        """Gets the y coordinate of the piece."""
        return self._y

    def set_y(self, y: int) -> None:
        """Sets the y coordinate of the piece."""
        self._y = y

    def color(self) -> _Color:
        """Gets teh color of the piece."""
        return self._color

    def valid_moves(self) -> Sequence[tuple[int, int]]:
        """Returns the list of valid moves for this given piece."""

    def get_icon(self) -> str:
        return self._ICONS[self._color]


class Pawn(BasePiece):
    """Pawn piece on a chess board."""
    PIECE_NAME = 'Pawn'
    _ICONS = {_Color.BLACK: '♙', _Color.WHITE: '♟︎'}
    ...


class Rook(BasePiece):
    """Rook piece on a chess board."""
    PIECE_NAME = 'Rook'
    _ICONS = {_Color.BLACK: '♖', _Color.WHITE: '♜'}
    ...


class Bishop(BasePiece):
    """Bishop piece on a chess board."""
    PIECE_NAME = 'Bishop'
    _ICONS = {_Color.BLACK: '♗', _Color.WHITE: '♝'}
    ...


class Knight(BasePiece):
    """Knight piece on a chess board."""
    PIECE_NAME = 'Knight'
    _ICONS = {_Color.BLACK: '♘', _Color.WHITE: '♞'}
    ...


class King(BasePiece):
    """King piece on a chess board."""
    PIECE_NAME = 'King'
    _ICONS = {_Color.BLACK: '♔', _Color.WHITE: '♚'}
    ...


class Queen(BasePiece):
    """Queen piece on a chesss board."""
    PIECE_NAME = 'Queen'
    _ICONS = {_Color.BLACK: '♕', _Color.WHITE: '♛'}
    ...
