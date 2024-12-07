import random

def print_board(board):
    """Prints the current state of the Tic Tac Toe board."""
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board):
    """Checks if there's a winner or the game is a draw."""
    # Check rows and columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != " ":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != " ":
            return board[0][i]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]

    # Check for draw
    if all(cell != " " for row in board for cell in row):
        return "Draw"

    return None

def player_move(board):
    """Handles the player's move."""
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            row, col = divmod(move, 3)
            if board[row][col] == " ":
                board[row][col] = "X"
                break
            else:
                print("Cell is already occupied. Choose another.")
        except (ValueError, IndexError):
            print("Invalid input. Enter a number between 1 and 9.")

def ai_move(board):
    """Handles the AI's move using random selection."""
    empty_cells = [(r, c) for r in range(3) for c in range(3) if board[r][c] == " "]
    if empty_cells:
        row, col = random.choice(empty_cells)
        board[row][col] = "O"
        print(f"AI chooses position {row * 3 + col + 1}.")

def display_help():
    """Displays instructions for the game."""
    print("""
    Welcome to Tic Tac Toe!
    
    Instructions:
    - The board has positions numbered 1 through 9 as follows:

      1 | 2 | 3
     -----------
      4 | 5 | 6
     -----------
      7 | 8 | 9

    - You will play as 'X'. The AI will play as 'O'.
    - Take turns selecting a position by entering the corresponding number.
    - The first to get three in a row (horizontally, vertically, or diagonally) wins.
    - If the board fills up with no winner, the game ends in a draw.
    
    Good luck!
    """)

def main():
    """Main function to run the Tic Tac Toe game."""
    print("Welcome to Tic Tac Toe!")
    display_help()

    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "Player"  # Alternates between 'Player' and 'AI'

    while True:
        print_board(board)
        if current_player == "Player":
            player_move(board)
        else:
            ai_move(board)

        winner = check_winner(board)
        if winner:
            print_board(board)
            if winner == "Draw":
                print("It's a draw!")
            else:
                print(f"{winner} wins!")
            break

        # Switch turns
        current_player = "AI" if current_player == "Player" else "Player"

if __name__ == "__main__":
    main()
