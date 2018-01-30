# A Maze is given as N*N binary matrix of blocks where source block is the upper left most block i.e., maze[0][0] and destination block is lower rightmost block i.e., maze[N-1][N-1].
#
# A rat starts from source (maze[0][0]) and has to reach destination (maze[n-1][n-1])

# The rat can move only in two directions: forward and down.

# In the maze matrix, 0 means the block is dead end and 1 means the block can be uNote

# that this is a simple version of the typical Maze problem.
# For example, a more complex version can be that the rat can move in 4 directions and a more complex version can be with limited number of moves.sed in the path from source to destination.


# If destination is reached
#     print the solution matrix
# Else
#    a) Mark current cell in solution matrix as 1.
#    b) Move forward in horizontal direction and recursively check if this
#        move leads to a solution.
#    c) If the move chosen in the above step doesn't lead to a solution
#        then move down and check if  this move leads to a solution.
#    d) If none of the above solutions work then unmark this cell as 0
#        (BACKTRACK) and return false.

n = 4


def print_solution(solution):
    for i in solution:
        for j in i:
            print(str(j) + " ", end="")
        print("")


def is_safe(x, y, maze):
    # if (x,y outside maze) return false
    return x >= 0 and x < n and y >= 0 and y < n and maze[x][y] == 1


def solve_maze(maze):
    solution = [[0 for j in range(4)] for i in range(4)]

    if not solve_maze_util(maze, 0, 0, solution):
        print("Solution doesn't exist")
        return False
    else:
        print_solution(solution)
        return True


def solve_maze_util(maze, x, y, solution):
    if (x == n - 1 and y == n - 1):
        solution[x][y] = 1
        return True
    if is_safe(x, y, maze):
        solution[x][y] = 1

        # move forward in x direction
        if solve_maze_util(maze, x + 1, y, solution):
            return True

        if solve_maze_util(maze, x, y + 1, solution):
            return True

        # if noone of the above works then backtrack
        # unmark current field as part of the solution
        solution[x][y] = 0
        return False
    return False


maze = [[1, 0, 0, 0],
        [1, 1, 0, 1],
        [0, 1, 0, 0],
        [1, 1, 1, 1]
        ]
solve_maze(maze)
