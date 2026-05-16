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

def test_actions():
    # Calling the actions function with an empty board, returns all moves
    assert actions(empty_board) == {(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)}

    # Calling the actions function with an full board, returns an empty list
    assert actions(board_full) == set()

    # Calling the board with a half empty board, returns the possible actions (empty fields)
    assert actions(board_half_full) == {(0,1),(1,0),(1,2)}