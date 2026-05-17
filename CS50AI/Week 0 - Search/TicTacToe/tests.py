from tictactoe import *

import pytest

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

def test_result():
    assert result(empty_board, (0, 0)) == [["X", None, None],
                                          [None, None, None],
                                          [None, None, None]]
    
    # Checking if the correct player is getting added
    assert result(board_x_turn, (0, 0)) == [["X", None, None],
                                           [None, "X", None],
                                           [None, None, "O"]] 
    
    assert result(board_o_turn, (2, 2)) == [[None, None, None],
                                           [None, "X", None],
                                           [None, None, "O"]]

    # Checking if a deep copy was made
    original = copy.deepcopy(empty_board)
    result(empty_board, (0, 0))
    assert empty_board == original

    # Checking for invalid action
    with pytest.raises(Exception):
        result(board_full, (2,2))

def test_winner():
    assert winner(board_draw) == None
    assert winner(empty_board) == None
    assert winner(board_full) == "X"
    assert winner(board_half_full) == "O"

# All the board i use for testing

empty_board = [[None, None, None],
         [None, None, None],
         [None, None, None]]

board_o_turn = [[None, None, None],
         [None, "X", None],
         [None, None, None]]

board_x_turn = [[None, None, None],
         [None, "X", None],
         [None, None, "O"]]

board_nearly_full = [["X", "O", "X"],
                     ["O", "X", "O"],
                     ["O", "X", None]]

board_full = [["X", "O", "X"],
             ["O", "X", "O"],
             ["O", "X", "X"]]

board_half_full = [["X", None, "X"],
         [None, "X", None],
         ["O", "O", "O"]]

board_draw = [["X", "O", "X"],
         ["O", "X", "X"],
         ["O", "X", "O"]]