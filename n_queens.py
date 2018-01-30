# The N Queen is the problem of placing N chess queens on an N×N chessboard
# so that no two queens attack each other.


# 1) Start in the leftmost column
# 2) If all queens are placed
#     return true
# 3) Try all rows in the current column.  Do following for every tried row.
#     a) If the queen can be placed safely in this row then mark this [row,
#         column] as part of the solution and recursively check if placing
#         queen here leads to a solution.
#     b) If placing queen in [row, column] leads to a solution then return
#         true.
#     c) If placing queen doesn't lead to a solution then umark this [row,
#         column] (Backtrack) and go to step (a) to try other rows.
# 3) If all rows have been tried and nothing worked, return false to trigger
#     backtracking.

n = 4


def print_solution(board):
    for i in range(n):
        for j in range(n):
            print(board[i][j]),
        print("")


# A utility function to check if a queen can
# be placed on board[row][col]. Note that this
# function is called when "col" queens are
# already placed in columns from 0 to col -1.
# So we need to check only left side for
# attacking queens
def is_safe(board, row, col):
    # Check this row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_util(board, column):
    # base case: If all queens are placed
    # then return true
    if column >= n:
        return True

    # Consider this column and try placing
    # this queen in all rows one by one
    for i in range(n):
        if is_safe(board, i, column):
            # Place this queen in board[i][col]
            board[i][column] = 1

            # recur to place rest of the queens
            if solve_util(board, column + 1):
                return True

            # backtrack
            board[i][column] = 0

    # if queen can not be place in any row in
    return False


def solve_n_queens():
    board = [[0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0]
             ]

    if solve_util(board, 0):
        print_solution(board)
        return True

    print("Solution does not exist")
    return False


solve_n_queens()
