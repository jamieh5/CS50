from testing_boards import *
from tictactoe import *

def test_player():
    # Empty board so first player should be X
    assert player(empty_board) == "X"

    # Checking for alternating turns
    assert player(board_o_turn) == "O"
    assert player(board_x_turn) == "X"

    # 4x X and 4x O on the board so X is next
    assert player(board_nearly_full) == "X"