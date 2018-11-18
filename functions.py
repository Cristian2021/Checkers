

# The position of a particular cell in the board is going to be given by two indexes
# (first idx for the row, and second idx for the column), here's an example:
""""
(0,0) | (0,1) | (0,2)
---------------------
(1,0) | (1,1) | (1,2)
---------------------
(2,0) | (2,1) | (2,2)
"""

blank_board = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"],
]

board_status = {
    "Top-Left": "-",
    "Top-Mid": "-",
    "Top-Right": "-",

    "Mid-Left": "-",
    "Center": "-",
    "Mid-Right": "-",

    "Bottom-Left": "-",
    "Bottom-Mid": "-",
    "Bottom-Right": "-"

}


def print_board(board):
    print(" %c | %c | %c " % (board["Top-Left"], board["Top-Mid"], board["Top-Right"]))
    print("-----------")
    print(" %c | %c | %c " % (board["Mid-Left"], board["Center"], board["Top-Right"]))
    print("-----------")
    print(" %c | %c | %c " % (board["Bottom-Left"], board["Bottom-Mid"], board["Bottom-Right"]))
    print("\n")


def start_new_game(player_1, player_2):
    print("This is a simple game of tic-tac-toe")
    print("How to play: Each player will type either an 'X' or 'O' followed by a set of coordinates "
          "these coordinates are of the form (x,y).")
    print("\n")
    print_board(board_status)
    print(player_1, " = X")
    print(player_2 , "= O")
    print("\n")
    print(player_1, " goes first")


def player_move(board, player, position):
    if player == 1:
        symbol = "X"
    else:
        symbol = "O"

    if position == [0, 0]:
        board["Top-Left"] = symbol
    elif position == [0, 1]:
        board["Top-Mid"] = symbol
    elif position == [0, 2]:
        board["Top-Right"] = symbol
    elif position == [1, 0]:
        board["Mid-Left"] = symbol
    elif position == [1, 1]:
        board["Center"] = symbol
    elif position == [1, 2]:
        board["Mid-Right"] = symbol
    elif position == [2, 0]:
        board["Bottom-Left"] = symbol
    elif position == [2, 1]:
        board["Bottom-Mid"] = symbol
    elif position == [2, 2]:
        board["Bottom-Right"] = symbol
    else:
        print("Error, no coordinates recognised")
        exit(0)

    print_board(board)


def get_winner(board):
    

