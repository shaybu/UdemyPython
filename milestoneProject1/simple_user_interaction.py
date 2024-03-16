game_list = [0, 1, 2]


def display_game(game_list):
    print("Here is the current list")
    print(game_list)


def clear_output():
    pass


def position_choice():
    # This original choice value can be anything that isn't an integer
    choice = 'WRONG'

    # while the choice value is not a digit, keep asking for input
    while choice not in ['0', '1', '2']:

        # we shouldn't convert here, otherwise we get an error on the wrong input
        choice = input("Pick a position to replace (0,1,2): ")

        if choice not in ['0', '1', '2']:
            # This clear the current output below the cell
            clear_output()

            print("Sorry, but you did not choose a valid position (0,1,2)")

    # Optionally you can clear everything after running the function
    # clear_output( )

    # we can convert once the while loop above has confirmed we have a digit
    return int(choice)


def replacement_choice(game_list, position):
    user_placement = input("Type a string to replace at the position: ")

    game_list[position] = user_placement

    return game_list


def gameon_choice():
    # This original choice value can be anything that isn't a Y or N
    choice = 'wrong'

    # while the choice is not a digit, keep asking for input.
    while choice not in ['Y', 'N']:

        # we shouldn't convert, here otherwise we get an error on a wrong input
        choice = input("Would you like to keep playing? (Y or N) ")

        if choice not in ['Y', 'N']:
            # this clear the current output below the cell
            # clear_output()

            print("Sorry, I didn't understand. Please make sure to choose Y or N")

    # Optionally you can clear everything after running the function
    # clear_output()
    if choice == "Y":
        # game is still on
        return True
    else:
        # game is over
        return False


# variable to keep game playing
game_on = True

# First game list
# game_list = [0, 1, 2]

# Clear any historical output and show the game list
# clear_output()
while game_on:
    display_game(game_list)

    # Have player choose position
    position = position_choice()

    # Rewrite that position and update game_list
    game_list = replacement_choice(game_list, position)

    # clear Screen and show the updated game_list
    # clear_output()
    display_game(game_list)

    # Ask if you want to keep playing
    game_on = gameon_choice()
