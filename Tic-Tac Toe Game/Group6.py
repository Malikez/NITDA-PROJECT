import random   # Imports the random module
import time     # Imports the time module


# Function to display the board
def display_board(board):
    """
    Prints the current state of the Tic Tac Toe board.

    Parameters:
    board (list): A list representing the Tic Tac Toe board with 9 elements.
    """
    print("+----+-----+----+")
    print(f"|  {board[0]} |  {board[1]}  |  {board[2]} |")
    print("+----+-----+----+")
    print(f"|  {board[3]} |  {board[4]}  |  {board[5]} |")
    print("+----+-----+----+")
    print(f"|  {board[6]} |  {board[7]}  |  {board[8]} |")
    print("+----+-----+----+")


# Function to check for a win
def check_win(board, player):
    """
    Checks if the specified player has won the game.

    Parameters:
    board (list): A list representing the Tic Tac Toe board with 9 elements.
    player (str): The player's symbol ('X' or 'O').

    Returns:
    bool: True if the player has won, False otherwise.
    """
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]              # diagonals  num = [4, [5, 6, 7, 8] , 6, 7, 8, 9] for i in num
    ]
    # Checks if win conditions are met
    return any(all(board[i] == player for i in condition) for condition in win_conditions)


# Function to check for a draw
def check_draw(board):
    """
    Checks if the game has ended in a draw.

    Parameters:
    board (list): A list representing the Tic Tac Toe board with 9 elements.

    Returns:
    bool: True if the game is a draw, False otherwise.
    """
    # Checks if there isn't a playable space left
    return all(space in ['X', 'O'] for space in board)


# Function for player's move
def player_move(board):
    """
    Handles the player's move by prompting for input and updating the board.

    Parameters:
    board (list): A list representing the Tic Tac Toe board with 9 elements.

    Returns:
    None
    """
    while True:
        try:
            # Assign a player move (X) to a space if it's empty
            move = int(input(f"{name}, Enter your move (1-9): ")) - 1
            if board[move] not in ['X', 'O']:
                board[move] = 'X'
                break
            else:
                # If space is taken, print the string below
                print("This position is already taken. Choose another one.")
        except (ValueError, IndexError):
            # Catch an index or value error
            print("Invalid input. Please enter a number from 1 to 9.")


# Function for computer's move
def computer_move(board):
    """
    Handles the computer's move by selecting a random empty spot on the board.

    Parameters:
    board (list): A list representing the Tic Tac Toe board with 9 elements.

    Returns:
    None
    """
    while True:
        move = random.randint(0, 8)  # Pick a random number between "0 to 8"
        if board[move] not in ['X', 'O']:  # Check if space is not taken
            board[move] = 'O'  # Assign Computer's move to 'O'
            break


# Main game loop
def play_game():
    """
    Runs the main game loop for Tic Tac Toe, alternating between player and computer moves.

    Returns:
    None
    """
    board = [str(i + 1) for i in range(9)]  # Declare the board variables
    display_board(board)  # Display the board

    while True:
        player_move(board)
        display_board(board)
        if check_win(board, 'X'):  # Check if user wins
            print(f"Congratulations!!, {name} You won!")
            break
        if check_draw(board):  # Check if it's a tie
            print("It's a draw!, Try harder next time.")
            break

        computer_move(board)
        print(f"Computer is making its move {name}, relax!..... ")
        time.sleep(3)  # Delays the computer's move for three seconds

        print("Computer's move:")
        display_board(board)
        if check_win(board, 'O'):  # Check if computer wins
            print("Computer wins! Better luck next time.")
            break
        if check_draw(board):  # Check if it's a tie
            print("It's a draw!, Try harder next time.")
            break


# Print welcome message and prompt user to enter their name
print("Welcome to Tic Tac Toe!!!")
name = input("Please, enter your name: ")

play_game()
