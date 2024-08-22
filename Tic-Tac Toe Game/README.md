# Tic Tac Toe Game

This is a simple command-line implementation of the classic Tic Tac Toe game in Python. The game allows a human player to play against a computer opponent.

## Features

- Interactive command-line interface
- Player vs. Computer gameplay
- Randomized computer moves
- Win and draw detection
- Simple board display

## Requirements

- Python 3.6 

## How to Play

1. Run the script using Python:

2. Enter your name when prompted.

3. The game board will be displayed, numbered 1-9 representing the available positions.

4. Enter a number (1-9) to place your 'X' in the corresponding position.

5. The computer will then make its move, placing an 'O'.

6. Continue taking turns until one player wins or the game ends in a draw.

## Game Rules

- The player uses 'X', and the computer uses 'O'.
- Players take turns placing their symbol in an empty cell.
- The first to get three of their symbols in a row (horizontally, vertically, or diagonally) wins.
- If all cells are filled and no player has won, the game is a draw.

## Code Structure

- `display_board(board)`: Displays the current state of the game board.
- `check_win(board, player)`: Checks if the specified player has won.
- `check_draw(board)`: Checks if the game has ended in a draw.
- `player_move(board)`: Handles the human player's move.
- `computer_move(board)`: Handles the computer's move.
- `play_game()`: Main game loop.

## Notes

- The computer's moves are random and do not implement any strategic decision-making.
- There's a 3-second delay after the computer's move to simulate "thinking".

Feel free to modify and expand upon this game! Enjoy playing Tic Tac Toe!