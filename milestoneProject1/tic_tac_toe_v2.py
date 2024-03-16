def print_board(board):
    # This function prints the game board.

    # Create horizontal separator to separate rows
    horizontal_sep = '---+---+---'

    # Loop through each row in the board to print it with borders
    for i, row in enumerate(board):
        # Replace '*' with ' ' for a cleaner look
        row_display = [" " if cell == '*' else cell for cell in row]

        # Print the row with vertical separators
        print(' | '.join(row_display))

        # For the first two rows, print the horizontal separator below the row
        if i < 2:
            print(horizontal_sep)


def player_input():
    # This function takes the player's name and their choice of marker
    marker = ''  # Initialize the marker variable.
    while not (marker == 'X' or marker == 'O'):  # Keep asking until the player chooses 'X' or 'O'.
        marker = input("Please pick a marker 'X' or 'O': ").upper()  # Convert the input to uppercase.
    return marker  # Return the chosen marker.


def place_marker(board, marker, position):
    # This function updates the board with the player's marker
    row, col = position  # Unpack the position tuple into row and col variables.
    board[row][col] = marker  # Place the marker on the board at the specified position.


def check_win(board, marker):
    # This function checks if a player has win
    for row in board:
        if all([spot == marker for spot in row]):  # If all cells in a row contain the marker, return True.
            return True
    for col in range(3):  # Check each column for a win.
        # If all cells in a column contain the marker, return True.
        if all([board[row][col] == marker for row in range(3)]):
            return True

    # Check diagonals for a win.
    if all([board[i][i] == marker for i in range(3)]) or all([board[i][2 - i] == marker for i in range(3)]):
        return True  # If either diagonal is filled with the marker, return True.
    return False  # If no win is found, return False.


def check_draw(board):
    # This function checks if the game is a draw
    for row in board:  # Loop through each row in the board.
        if any(spot == '*' for spot in row):  # If any cell is still unselected ('*'), return False.
            return False
    return True


def player_turn(board, player_name, marker):
    # This function manages each player's turn by asking for their move,
    # checking the validity, and placing the marker on the board if valid.
    position = (-1, -1)  # Initialize position with an invalid value.
    while position == (-1, -1) or board[position[0]][position[1]] != '*':  # Validate the move.
        player_input = input(f"{player_name}, enter your move as row col (e.g., 0 2 or 02): ")  # Ask for input.

        # Input validation and parsing logic
        if len(player_input) == 2 and player_input.isdigit():  # Checks if input is 2 digits with no space.
            position = (int(player_input[0]), int(player_input[1]))
        elif len(player_input.split()) == 2:  # Checks if input has two parts separated by space.
            try:
                position = tuple(map(int, player_input.split()))
            except ValueError:
                print("Invalid input. Please ensure you're entering numbers.")
                position = (-1, -1)  # Reset position to invalid if conversion fails.
        else:
            print("Invalid input. Please enter two numbers, either separated by a space or not.")
            continue  # Skip the rest of the loop and ask for input again.

        # Check if the chosen position is within the board's range.
        if not (0 <= position[0] <= 2 and 0 <= position[1] <= 2):
            print("Invalid position. Please enter row and col as 0, 1, or 2.")
            position = (-1, -1)  # Reset position to invalid.
        elif board[position[0]][position[1]] != '*':  # Check if the position is already taken.
            print("This position is already taken. Choose another one.")
            position = (-1, -1)  # Reset position to invalid.

    # Place the marker on the board at the valid position.
    place_marker(board, marker, position)


# Start of the game
print('Welcome to Tic Tac Toe!')

# Initialize the board
board = [['*' for _ in range(3)] for _ in range(3)]

# Get player names
player1_name = input("Player 1, enter your name: ")
player2_name = input("Player 2, enter your name: ")

# Assign markers to players
player1_marker = player_input()
player2_marker = 'O' if player1_marker == 'X' else 'X'


# Ask players if they are ready to start the game.
ready = input("Are you ready to play? Enter Yes or No: ").lower()
if ready != 'yes':
    # If the player's response is not 'yes', cancel the game.
    print("Game cancelled.")
else:
    # If the player is ready, start the game.
    game_on = True   # Flag to keep the game running.
    turn = player1_name  # Start with player 1's turn

    # Game loop continues as long as game_on is True
    while game_on:
        print_board(board)  # Display the current state of the game board.

        if turn == player1_name:  # Check if it's player 1's turn.
            print(f"{player1_name}'s turn.")  # Inform player 1 it's their turn.
            player_turn(board, player1_name, player1_marker)  # Execute player 1's turn.

            # After player 1's move, check if they have won.
            if check_win(board, player1_marker):
                print_board(board)  # Display the final board.
                print(f"Congratulations {player1_name}, you have won the game!")
                game_on = False   # End the game.
            else:
                # If player 1 hasn't won, check for a draw.
                if check_draw(board):
                    print_board(board)  # Display the final board.
                    print("The game is a draw!")  # Announce the draw.
                    game_on = False  # End the game.
                turn = player2_name  # If no win or draw, switch to player 2's turn.
        else:
            # This block is the same as the one for player 1, but for player 2.
            print(f"{player2_name}'s turn.")
            player_turn(board, player2_name, player2_marker)
            if check_win(board, player2_marker):
                print_board(board)
                print(f"Congratulations {player2_name}, you have won the game!")
                game_on = False
            else:
                if check_draw(board):
                    print_board(board)
                    print("The game is a draw!")
                    game_on = False
                turn = player1_name  # Switch back to player 1's turn if the game hasn't ended.
