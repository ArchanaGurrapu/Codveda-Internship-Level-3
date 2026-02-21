def print_board(board):
    for row in board:
        print(row)
    print("\n")


def is_safe(board, row, col, n):
    # Check column
    for i in range(row):
        if board[i][col] == "Q":
            return False

    # Check left diagonal
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == "Q":
            return False
        i -= 1
        j -= 1

    # Check right diagonal
    i, j = row, col
    while i >= 0 and j < n:
        if board[i][j] == "Q":
            return False
        i -= 1
        j += 1

    return True


def solve_nqueens(board, row, n):
    if row == n:
        print_board(board)
        return True

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = "Q"
            if solve_nqueens(board, row + 1, n):
                return True
            board[row][col] = "."  # Backtrack

    return False


# Main
n = int(input("Enter number of queens: "))
board = [["." for _ in range(n)] for _ in range(n)]

solve_nqueens(board, 0, n)