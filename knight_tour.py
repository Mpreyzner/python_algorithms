# Solution rewritten from java from https://www.geeksforgeeks.org/backtracking-set-1-the-knights-tour-problem/

# Backtracking works in an incremental way to attack problems.
# Typically, we start from an empty solution vector and one by one add items (Meaning of item varies from problem to problem.
# In context of Knight’s tour problem, an item is a Knight’s move).
#
# When we add an item, we check if adding the current item violates the problem constraint,
# if it does then we remove the item and try other alternatives.

# If none of the alternatives work out then we go to previous stage and remove the item added in the previous stage.
# If we reach the initial stage back then we say that no solution exists.
# If adding an item doesn’t violate constraints then we recursively add items one by one.
# If the solution vector becomes complete then we print the solution.

# knight can visit a field only once

# chess board size is 8x8


# If all squares are visited
#     print the solution
# Else
#    a) Add one of the next moves to solution vector and recursively
#    check if this move leads to a solution. (A Knight can make maximum
#    eight moves. We choose one of the 8 moves in this step).
#    b) If the move chosen in the above step doesn't lead to a solution
#    then remove this move from the solution vector and try other
#    alternative moves.
#    c) If none of the alternatives work then return false (Returning false
#    will remove the previously added item in recursion and if false is
#    returned by the initial call of recursion then "no solution exists" )

n = 8


def is_safe(x, y, solution):
    # check if x and y are in the board range,
    # then check if their value is -1
    # -1 means that given field was not visited yet (or it was backtracked)
    return 0 <= x < n and 0 <= y < n and solution[x][y] == -1


def print_solution(solution):
    for x in range(n - 1):
        for y in range(n - 1):
            print(str(solution[x][y]) + " ")
        print("\n")


def solve_tour():
    solution = [[-1 for x in range(n)] for y in range(n)]
    #    /* xMove[] and yMove[] define possible move patters of Knight.
    #       xMove[] is for next value of x coordinate
    #       yMove[] is for next value of y coordinate */
    xMove = [2, 1, -1, -2, -2, -1, 1, 2]
    yMove = [1, 2, 2, 1, -1, -2, -2, -1]

    # Since the Knight is initially at the first block
    solution[0][0] = 0
    # Start from 0,0 and explore all tours using
    if not solve_util(0, 0, 1, solution, xMove, yMove):
        print("Solution does not exist")
        return False
    else:
        print_solution(solution)

    return True


def solve_util(x, y, moveCounter, solution, xMove, yMove):
    if moveCounter == n ** 2:
        return True
    # Try all next moves from the current coordinate x, y
    for k in range(8):
        next_x = x + xMove[k]
        next_y = y + yMove[k]
        # if the move is not safe try other possible moves
        if is_safe(next_x, next_y, solution):
            solution[x][y] = moveCounter
            if solve_util(next_x, next_y, moveCounter + 1, solution, xMove, yMove):
                # explore further steps recursively
                return True
            else:
                solution[next_x][next_y] = -1  # backtrack


print(solve_tour())
