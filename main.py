import functions

p1_name = input("Please enter the name of player 1: ")
p2_name = input("Please enter the name of player 2: ")

functions.start_new_game(p1_name, p2_name)  # initialise the game

game_complete = False
while game_complete is False:

    p1_move = input("Player 1, Enter your move: ")  # may need to use RegEx to check input format
    functions.player_move(functions.board_status, 1, p1_move)

    p2_move = input("Player 2, Enter your move: ")
    functions.player_move(functions.board_status, 2, p2_move)

    if game_complete is True:
        break
    else:
        continue

# print("Winner: %s", winning_player)


