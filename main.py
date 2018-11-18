import functions

p1_name = input("Please enter the name of player 1: ")
p2_name = input("Please enter the name of player 2: ")

functions.start_new_game(p1_name, p2_name)  # initialise the game

game_complete = False
while game_complete is False:

    p1_move_row = int(input(p1_name + " Enter your row: ")) # typecast to int since input only reads strings
    p1_move_col = int(input(p1_name+ " Enter your column: "))

    p1_move = [p1_move_row, p1_move_col]

    functions.player_move(functions.board_status, 1, p1_move)

    p2_move_row = int(input(p2_name + " Enter your row: "))
    p2_move_col = int(input(p2_name + " Enter your column: "))

    p2_move = [p2_move_row, p2_move_col]
    functions.player_move(functions.board_status, 2, p2_move)

    functions.get_winner(functions.board_status)

    if game_complete is True:
        break
    else:
        continue

# print("Winner: %s", winning_player)


