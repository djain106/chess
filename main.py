"""File to run and play the chess game."""

from classes.board import Board


# Basic game testing.
board = Board(load=True)
board.display_board()
