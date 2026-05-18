"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    count_x = 0
    count_o = 0

    for row in board:
        for cell in row:
            if cell == "X":
                count_x += 1
            elif cell == "O":
                count_o += 1

    if count_o >= count_x:
        return "X"
    else:
        return "O"

def actions(board):
    possible_actions = set()

    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            if board[i][j] == None:
                possible_actions.add((i, j))
    return possible_actions

def result(board, action):
    board_copy = copy.deepcopy(board)

    i, j = action
    if board_copy[i][j] != None:
        raise Exception("Invalid action")
    
    board_copy[i][j] = player(board)
    return board_copy

def winner(board):
    possible_combinations = (
        # Winning combinations for each row
        ((0, 0), (0, 1), (0, 2)),
        ((1, 0), (1, 1), (1, 2)),
        ((2, 0), (2, 1), (2, 2)),

        # Winning combinations for each column
        ((0, 0), (1, 0), (2, 0)),
        ((0, 1), (1, 1), (2, 1)),
        ((0, 2), (1, 2), (2, 2)),

        # Winning combinations for each diagonal
        ((0, 0), (1, 1), (2, 2)),
        ((0, 2), (1, 1), (2, 0))
    )


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
