

# The position of a particular cell in the board is going to be given by two indexes
# (first idx for the row, and second idx for the column), here's an example:
""""
(0,0) | (0,1) | (0,2)
---------------------
(1,0) | (1,1) | (1,2)
---------------------
(2,0) | (2,1) | (2,2)
"""

board = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"],
]


def print_board():
    print("INSERT BOARD HERE")


def start_new_game():
    print("This is a simple game of tic-tac-toe")
    print("How to play: Each player will type either an 'X' or 'O' followed by a set of coordinates "
          "these coordinates are of the form (x,y).")
    print("\n")
    print_board()
    print("Player 1 goes first")


def player_move(board_status, player, position):
    print(board_status, player, position) # This is just to get rid of the parameter errors. Obviously change later

start_new_game()