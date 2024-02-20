"""An instance of a chess game."""

from classes import board
from classes import constants

# Aliases.
_Color = constants.Color


class ChessGame:

    def __init__(self):
        self._board = board.Board(load=True)
        self._curr_color = None
        self.start_game()

    def start_game(self):
        while not self._is_checkmate():
            self._curr_color = self.get_next_turn_color()
            self._board.display_board()
            self._play_next_turn()
        print(f'Congrats! {self._curr_color.value.capitalize()} wins!')
    
    def _is_checkmate(self) -> bool:
        # TODO: Add logic to check that the game is in a checkmate state.
        return False

    def _play_next_turn(self):
        playing_turn = True
        while playing_turn:
            # Get input for the coordinates of the piece.
            x, y = self._get_input_coords()

            # Validate that a piece exists and is for the correct player.
            selected_square = self._board.get_square(x, y)
            selected_piece = selected_square.piece()
            if not selected_piece:
                print('There is no piece on this square. Please select new coordinates.')
                continue
            if selected_piece.color() != self._curr_color:
                print('This piece is not your color! Please select your own piece!')
                continue
            
    def get_next_turn_color(self) -> _Color:
        if not self._curr_color or self._curr_color == _Color.BLACK:
            return _Color.WHITE
        return _Color.BLACK

    def _get_input_coords(self) -> tuple[int, int]:
        while True:
            try:
                x = int(input('Choose x coord of piece (0-7): '))
                y = int(input('Choose y coord of piece (0-7): '))
                constants.validate_coordinates(x, y)
                return (x, y)
            except ValueError as e:
                print(e)