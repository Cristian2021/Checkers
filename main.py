import constants


def play_human_opponent():
    import functions

    winning_player = "Not yet determined"
    p1_name = input("Please enter the name of player 1: ")
    p2_name = input("Please enter the name of player 2: ")

    functions.start_new_game(p1_name, p2_name)  # initialise the game

    game_complete = (False, "Incomplete Game")
    while game_complete[0] is False:

        p1_move_row = int(input(p1_name + " Enter your row: "))  # typecast to int since input only reads strings
        p1_move_col = int(input(p1_name + " Enter your column: "))

        p1_move = [p1_move_row, p1_move_col]

        functions.player_move(functions.board_status, 1, p1_move)

        game_complete = functions.check_game_status(functions.board_status)

        if game_complete[0] is True:
            if game_complete[1] == "X":
                winning_player = p1_name
            else:
                winning_player = p2_name
            break

        p2_move_row = int(input(p2_name + " Enter your row: "))
        p2_move_col = int(input(p2_name + " Enter your column: "))

        p2_move = [p2_move_row, p2_move_col]
        functions.player_move(functions.board_status, 2, p2_move)

        game_complete = functions.check_game_status(functions.board_status)

        if game_complete[0] is True:
            if game_complete[1] == "X":
                winning_player = p1_name
            else:
                winning_player = p2_name
            break
        else:
            continue

    print("Winner: %s" % winning_player)


def play_bot_opponent():
    import functions
    import time  # used to add a pause when bot is making a move

    winning_player = "Not yet determined"
    player_name = input("Enter your name: ")

    functions.start_new_game(player_name, "bot")

    spaces_covered = 0  # how much of the board has been filled up
    game_complete = (False, "Incomplete Game")
    while game_complete[0] is False:

        player_move_row = int(input(player_name + " Enter your row: "))  # typecast to int since input only reads strings
        player_move_col = int(input(player_name + " Enter your column: "))

        p1_move = [player_move_row, player_move_col]

        functions.player_move(functions.board_status, 1, p1_move)
        spaces_covered += 1

        game_complete = functions.check_game_status(functions.board_status)

        if spaces_covered == constants.TOTAL_BOXES and game_complete[0] is not True:
            game_complete = [True, "Tie"]

        if game_complete[0] is True:
            if game_complete[1] == "X":
                winning_player = player_name
            elif game_complete[1] == "O":
                winning_player = "bot"
            elif game_complete[1] == "Tie":
                winning_player = "None"
            break

        print("Bot is making a move...")
        time.sleep(2)
        functions.bot_move(functions.board_status)
        spaces_covered += 1

        game_complete = functions.check_game_status(functions.board_status)

        if spaces_covered == constants.TOTAL_BOXES and game_complete[0] is not True:
            game_complete = [True, "Tie"]

        if game_complete[0] is True:
            if game_complete[1] == "X":
                winning_player = player_name
            elif game_complete[1] == "O":
                winning_player = "bot"
            elif game_complete[1] == "Tie":
                winning_player = "None"
            break

    if winning_player != "None":
        print("Winner: %s" % winning_player)
    else:
        print("The game is a tie!")


game_type = input("Would you like to play against a bot or another human opponent? "
                  "please type 'bot' or 'human': ")

if game_type != "bot" and game_type != "human":
    while game_type != "bot" and game_type != "human":
        game_type = input("Please enter either 'bot' or 'human': ")

if game_type == "bot":
    play_bot_opponent()
else:
    play_human_opponent()


