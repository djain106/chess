"""A chess board and its interactions."""

import csv
import immutabledict

from classes import constants
from classes import pieces

from typing import Sequence

# Aliases.
_Color = constants.Color
_BasePiece = pieces.BasePiece

# Constants.
_EMPTY_STRING = ' '
_BOARD_STR_FIRST_LINE = '  0 1 2 3 4 5 6 7\n'
# Maps the text for each piece to their constructors.
_PIECE_MAPPING = immutabledict.immutabledict({
    'Pawn': pieces.Pawn,
    'Rook': pieces.Rook,
    'Knight': pieces.Knight,
    'Bishop': pieces.Bishop,
    'Queen': pieces.Queen,
    'King': pieces.King,
})

# Maps the text for each color to the enum.
_COLOR_MAPPING = immutabledict.immutabledict({
    'Black': _Color.BLACK,
    'White': _Color.WHITE,
})


class BoardSquare:
    """A square on a chess board."""

    def __init__(self, x: int, y: int, piece: _BasePiece | None = None) -> None:
        constants.validate_coordinates(x, y)
        self._x = x
        self._y = y
        self._color = _Color.BLACK if (x + y) % 2 else _Color.WHITE
        # Ensure that the piece is on the correct square.
        if piece:
            piece.set_x(self._x)
            piece.set_y(self._y)
        self._piece = piece

    def __str__(self) -> str:
        return f'BoardSquare(x: {self._x}, y: {self._y}, color: {self._color.value}, piece: {self._piece})'

    def __repr__(self) -> str:
        return f'BoardSquare(x: {self._x}, y: {self._y}, color: {self._color.value}, piece: {self._piece})'

    def piece(self) -> _BasePiece | None:
        return self._piece

    def color(self) -> _Color:
        return self._color

    def set_piece(self, piece: _BasePiece) -> None:
        if self._piece:
            raise ValueError(
                f'A piece {self._piece} already exists on this square.')
        self._piece = piece

    def get_display(self) -> str:
        if self._piece:
            return self._piece.get_icon()
        elif self.color() == _Color.WHITE:
            return '■'
        elif self.color() == _Color.BLACK:
            return '□'


class Board:
    """A basic chess board."""

    def __init__(self, load: bool = False, path: str = './games/default.csv') -> None:
        """Initializes a basic chess board."""
        self._board: Sequence[Sequence[BoardSquare]] = [[BoardSquare(i, j) for i in range(constants.BOARD_SIZE)]
                                                        for j in range(constants.BOARD_SIZE)]
        if load:
            self.load_board(path)

    def __str__(self) -> str:
        return str(self._board)

    def display_board(self) -> None:
        """Displays the game board in its current state."""
        board_str = _BOARD_STR_FIRST_LINE
        for i in range(len(self._board)):
            curr_line = f'{i} '
            for j in range(len(self._board[i])):
                curr_line += self._board[i][j].get_display() + _EMPTY_STRING
            board_str += curr_line + '\n'
        print(board_str)

    def load_board(self, path='./games/default.csv') -> None:
        """Loads pieces onto a board.

        The game is loaded from a CSV filepath. The file must be in the following
        format:
            x, y, piece, color
        Example:
            0, 1, Pawn, Black

        Parameters:
        -----------
        path : str
            File path for the CSV file to read from. Defaults to a starting game position
                for the board.
        """
        with open(path, newline='\n') as csvfile:
            for row in csv.reader(csvfile):
                x = int(row[0])
                y = int(row[1])
                color = _COLOR_MAPPING.get(row[3], None)
                piece_constructor = _PIECE_MAPPING.get(row[2], None)
                if piece_constructor and color:
                    piece = piece_constructor(x=x, y=y, color=color)
                    self._board[x][y].set_piece(piece)

    def set_piece(self, piece: _BasePiece) -> None:
        constants.validate_coordinates(piece.x(), piece.y())
        self._board[piece.x()][piece.y()].set_piece(piece)

    def get_square(self, x: int, y: int) -> BoardSquare:
        return self._board[x][y]
