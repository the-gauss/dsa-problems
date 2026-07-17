"""Tic Tac Toe.

Notebook execution output: ``Kernel Error: cell could not be executed``
(traceback: ``the kernel is still starting``).
"""

board = [[" ", " ", " "] for _ in range(3)]


def print_board():
    print()
    for i in range(3):
        print(" " + board[i][0] + " | " + board[i][1] + " | " + board[i][2])
        if i < 2:
            print("---+---+---")
    print()


def check_winner(player):
    for row in board:
        if row[0] == player and row[1] == player and row[2] == player:
            return True
    for col in range(3):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            return True
    return ((board[0][0] == player and board[1][1] == player and board[2][2] == player)
            or (board[0][2] == player and board[1][1] == player and board[2][0] == player))


def is_board_full():
    return all(cell != " " for row in board for cell in row)


def make_move(player):
    while True:
        try:
            row = int(input(f"Player {player}, enter row number (1-3): ")) - 1
            col = int(input(f"Player {player}, enter column number (1-3): ")) - 1
            if row < 0 or row > 2 or col < 0 or col > 2:
                print("Invalid position. Row and column must be between 1 and 3.")
            elif board[row][col] != " ":
                print("That position is already taken. Try again.")
            else:
                board[row][col] = player
                break
        except ValueError:
            print("Invalid input. Please enter numbers only.")


def play_game():
    current_player = "X"
    print("Tic Tac Toe")
    print("Player X goes first.")
    while True:
        print_board()
        make_move(current_player)
        if check_winner(current_player):
            print_board()
            print(f"Player {current_player} wins!")
            break
        if is_board_full():
            print_board()
            print("The game is a draw.")
            break
        current_player = "O" if current_player == "X" else "X"


if __name__ == "__main__":
    play_game()
