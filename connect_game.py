# Connect Four Game

def create_board(rows, columns):
    board = [[' ' for _ in range(columns)] for _ in range(rows)]
    return board

def display_board(board):
    for row in board:
        print("| " + " | ".join(row) + " |")
        print("-" * (len(board[0]) * 4 + 1))  # Moved this line inside the loop

def is_valid_move(board, column):
    return 0 <= column < len(board[0]) and board[0][column] == ' '

def drop_piece(board, column, player_piece):
    for row in range(len(board) - 1, -1, -1):
        if board[row][column] == ' ':
            board[row][column] = player_piece
            break

def check_win(board, player_piece):
    # Check horizontally
    for row in board:
        if f'{player_piece * 4}' in ''.join(row):
            return True

    # Check vertically
    for col in range(len(board[0])):
        if f'{player_piece * 4}' in ''.join([board[row][col] for row in range(len(board))]):
            return True

    # Check diagonally (from bottom-left to top-right)
    for row in range(len(board) - 3):
        for col in range(len(board[0]) - 3):  # Fixed an error here
            if all(board[row + i][col + i] == player_piece for i in range(4)):
                return True

    # Check diagonally (from top-left to bottom-right)
    for row in range(3, len(board)):
        for col in range(len(board[0]) - 3):  # Fixed an error here
            if all(board[row - i][col + i] == player_piece for i in range(4)):
                return True

    return False

def main():
    rows = 6
    columns = 7
    player1_piece = 'X'
    player2_piece = 'O'
    board = create_board(rows, columns)
    current_player = 1

    while True:
        display_board(board)
        column = int(input(f"Player {current_player}, choose a column (0-{columns - 1}): "))

        if is_valid_move(board, column):
            player_piece = player1_piece if current_player == 1 else player2_piece
            drop_piece(board, column, player_piece)

            if check_win(board, player_piece):
                display_board(board)
                print(f"Player {current_player} wins!")
                break

            current_player = 3 - current_player  # Switch players (1 -> 2, 2 -> 1)
        else:
            print("Invalid move. Please choose a valid column.")

if __name__ == "__main__":
    main()
