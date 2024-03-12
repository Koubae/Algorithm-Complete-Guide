"""Rat in a maze problem, Backtracking Algorithm Recursive represented with a Adjacency matrix 2"""


N = 4
START = (0, 0)
TARGET = (N-1, N-1)
RAT_STEP = 'X'

def get_path(path):
    for i in path:
        for j in i:
            print(str(j) + " ", end="")
        print("")


def check_path(maze, x, y):
    if (x, y) >= START and x < N and y < N and maze[x][y] == 1:
        return True


def rat_in_maze(maze):
    RAT_PATH = [[0 for _ in range(4)] for _ in range(4)]

    if not backtracking(maze, 0, 0, RAT_PATH):
        return
    else:
        return RAT_PATH


def backtracking(maze, x, y, path):

    if (x, y) == TARGET and maze[x][y] == 1:   # NOTE: Step 1 is check if target is found
        path[x][y] = RAT_STEP
        return True

    if check_path(maze, x, y):
        path[x][y] = RAT_STEP   # NOTE: Mark Path with Rat steps giving the solution

        if backtracking(maze, x + 1, y, path):  # NOTE: Move RIGHT
            return True
        elif backtracking(maze, x, y + 1, path):  # NOTE: Move DOWN
            return True
        else:
            path[x][y] = 0  # NOTE BACKTRACK: unmark x, y as part of solution path
            return


if __name__ == "__main__":
    maze = [[1, 1, 1, 0],
            [0, 1, 1, 1],
            [0, 1, 0, 0],
            [1, 1, 1, 1]]

    path = rat_in_maze(maze)
    get_path(path)