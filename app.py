import math

# Constants
HUMAN = 'O'
AI = 'X'
EMPTY = ' '

# Initialize board
board = [[EMPTY for _ in range(3)] for _ in range(3)]

# Print the board
def print_board(b):
    for row in b:
        print('|'.join(row))
        print('-' * 5)

# Check for winner
def check_winner(b):
    # Rows, Columns, Diagonals
    for i in range(3):
        if b[i][0] == b[i][1] == b[i][2] != EMPTY:
            return b[i][0]
        if b[0][i] == b[1][i] == b[2][i] != EMPTY:
            return b[0][i]
    if b[0][0] == b[1][1] == b[2][2] != EMPTY:
        return b[0][0]
    if b[0][2] == b[1][1] == b[2][0] != EMPTY:
        return b[0][2]
    return None

# Check if board is full
def is_full(b):
    return all(cell != EMPTY for row in b for cell in row)

# Minimax with alpha-beta pruning
def minimax(b, depth, is_maximizing, alpha, beta):
    winner = check_winner(b)
    if winner == AI:
        return 10 - depth
    elif winner == HUMAN:
        return depth - 10
    elif is_full(b):
        return 0

    if is_maximizing:
        max_eval = -math.inf
        for i in range(3):
            for j in range(3):
                if b[i][j] == EMPTY:
                    b[i][j] = AI
                    eval = minimax(b, depth + 1, False, alpha, beta)
                    b[i][j] = EMPTY
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval
    else:
        min_eval = math.inf
        for i in range(3):
            for j in range(3):
                if b[i][j] == EMPTY:
                    b[i][j] = HUMAN
                    eval = minimax(b, depth + 1, True, alpha, beta)
                    b[i][j] = EMPTY
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval

# AI chooses the best move
def best_move():
    best_val = -math.inf
    move = (-1, -1)
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                board[i][j] = AI
                move_val = minimax(board, 0, False, -math.inf, math.inf)
                board[i][j] = EMPTY
                if move_val > best_val:
                    best_val = move_val
                    move = (i, j)
    board[move[0]][move[1]] = AI
    print(f"AI plays: {move[0] + 1}, {move[1] + 1}")

# Human move
def human_move():
    while True:
        try:
            row = int(input("Enter row (1-3): ")) - 1
            col = int(input("Enter column (1-3): ")) - 1
            if board[row][col] == EMPTY:
                board[row][col] = HUMAN
                break
            else:
                print("Cell is already taken!")
        except (ValueError, IndexError):
            print("Invalid input. Try again!")

# Main game loop
def play_game():
    print("Welcome to Tic-Tac-Toe!")
    print("You are 'O'. AI is 'X'.")
    player_first = input("Do you want to play first? (y/n): ").lower() == 'y'
    
    while True:
        print_board(board)
        if check_winner(board) or is_full(board):
            break

        if player_first:
            human_move()
        else:
            best_move()
        player_first = not player_first

    print_board(board)
    winner = check_winner(board)
    if winner:
        print(f"{'You win!' if winner == HUMAN else 'AI wins!'}")
    else:
        print("It's a draw!")

# Run the game
if __name__ == "__main__":
    play_game()
