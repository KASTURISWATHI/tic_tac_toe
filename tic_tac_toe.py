import random

# Function to print the Tic-Tac-Toe board
def print_board(board):
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")

# Function to check for a win
def check_win(board, player):
    win_conditions = [
        [0,1,2], [3,4,5], [6,7,8],  # rows
        [0,3,6], [1,4,7], [2,5,8],  # columns
        [0,4,8], [2,4,6]            # diagonals
    ]
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False

# Function to check for a draw
def check_draw(board):
    return all(space != " " for space in board)

# Function for user's move
def player_move(board):
    while True:
        move = input("Enter your move (1-9): ")
        if move.isdigit():
            move = int(move) - 1
            if move >= 0 and move <= 8 and board[move] == " ":
                board[move] = "X"
                break
            else:
                print("Invalid move! Cell already taken or out of range.")
        else:
            print("Please enter a number from 1 to 9.")

# Function for computer's move
def computer_move(board):
    available_moves = [i for i, spot in enumerate(board) if spot == " "]
    move = random.choice(available_moves)
    board[move] = "O"
    print(f"Computer chose position {move + 1}")

# Main game function
def tic_tac_toe():
    board = [" "] * 9
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)
    
    while True:
        # Player's turn
        player_move(board)
        print_board(board)
        if check_win(board, "X"):
            print("Congratulations! You win!")
            break
        if check_draw(board):
            print("It's a draw!")
            break

        # Computer's turn
        computer_move(board)
        print_board(board)
        if check_win(board, "O"):
            print("Computer wins! Better luck next time.")
            break
        if check_draw(board):
            print("It's a draw!")
            break

# Start the game
tic_tac_toe()
