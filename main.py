"""File to run and play the chess game."""

from classes.board import Board
from classes.pieces import King
from classes.constants import Color


# Basic game testing.
board = Board()
king = King(color=Color.BLACK)
board.set_piece(king)
print(board)
