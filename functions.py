

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


def print_board(board_status):
    print(" %c | %c | %c " % (board_status["Top-Left"], board_status["Top-Mid"], board_status["Top-Right"]))
    print("-----------")
    print(" %c | %c | %c " % (board_status["Mid-Left"], board_status["Center"], board_status["Top-Right"]))
    print("-----------")
    print(" %c | %c | %c " % (board_status["Bottom-Left"], board_status["Bottom-Mid"], board_status["Bottom-Right"]))
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
    if player is 1:
        symbol = "X"
    else:
        symbol = "O"

    if position is (0, 0):
        board["Top_Left"] = symbol
    elif position is (0, 1):
        board["Top-Mid"] = symbol
    elif position is (0, 2):
        board["Top-Right"] = symbol
    elif position is (1, 0):
        board["Mid-Left"] = symbol
    elif position is (1, 1):
        board["Center"] = symbol
    elif position is (1, 2):
        board["Mid-Right"] = symbol
    elif position is (2, 0):
        board["Bottom-Left"] = symbol
    elif position is (2, 1):
        board["Bottom-Mid"] = symbol
    elif position is (2, 2):
        board["Bottom-Right"] = symbol

    print_board(board)



def get_winner(board_status):
    print("placeholder")

