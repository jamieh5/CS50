# File where i store all the tictactoe boards for testing

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