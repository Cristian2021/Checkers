import functions

functions.start_new_game()  # initialise the game

game_complete = False
while game_complete is False:

    p1_move = input("Player 1, Enter your move: ")  # may need to use RegEx to check input format

    p2_move = input("Player 2, Enter your move: ")

    if game_complete is True:
        break
    else:
        continue

# print("Winner: %s", winning_player)


