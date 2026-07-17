import math

HUMAN = "O"
AI = "X"
EMPTY = " "


def print_board(board):
    print()
    for i in range(3):
        row = board[i * 3:i * 3 + 3]
        print(" " + " | ".join(row))
        if i < 2:
            print("---+---+---")
    print()


def check_winner(board):
    win_positions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # cols
        (0, 4, 8), (2, 4, 6)              # diagonals
    ]
    for a, b, c in win_positions:
        if board[a] != EMPTY and board[a] == board[b] == board[c]:
            return board[a]
    if EMPTY not in board:
        return "Draw"
    return None


def minimax(board, depth, is_maximizing, alpha, beta):
    result = check_winner(board)
    if result == AI:
        return 10 - depth
    if result == HUMAN:
        return depth - 10
    if result == "Draw":
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == EMPTY:
                board[i] = AI
                score = minimax(board, depth + 1, False, alpha, beta)
                board[i] = EMPTY
                best_score = max(best_score, score)
                alpha = max(alpha, score)
                if beta <= alpha:
                    break
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == EMPTY:
                board[i] = HUMAN
                score = minimax(board, depth + 1, True, alpha, beta)
                board[i] = EMPTY
                best_score = min(best_score, score)
                beta = min(beta, score)
                if beta <= alpha:
                    break
        return best_score


def best_move(board):
    best_score = -math.inf
    move = -1
    for i in range(9):
        if board[i] == EMPTY:
            board[i] = AI
            score = minimax(board, 0, False, -math.inf, math.inf)
            board[i] = EMPTY
            if score > best_score:
                best_score = score
                move = i
    return move


def play_game():
    board = [EMPTY] * 9
    print("Welcome to Tic-Tac-Toe!")
    print("You are 'O', AI is 'X'.")
    print("Positions are numbered 1-9, left to right, top to bottom.\n")
    print_board([str(i + 1) if c == EMPTY else c for i, c in enumerate(board)])

    while True:
        
        while True:
            try:
                pos = int(input("Enter your move (1-9): ")) - 1
                if 0 <= pos <= 8 and board[pos] == EMPTY:
                    break
                print("Invalid move, try again.")
            except ValueError:
                print("Please enter a number between 1 and 9.")

        board[pos] = HUMAN
        result = check_winner(board)
        print_board(board)
        if result:
            announce_result(result)
            break

        print("AI is thinking...")
        ai_pos = best_move(board)
        board[ai_pos] = AI
        result = check_winner(board)
        print_board(board)
        if result:
            announce_result(result)
            break


def announce_result(result):
    if result == "Draw":
        print("It's a draw!")
    elif result == AI:
        print("AI wins! Better luck next time.")
    else:
        print("Congratulations, you win!")


if __name__ == "__main__":
    play_game()