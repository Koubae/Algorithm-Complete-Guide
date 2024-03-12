"""Rat in a maze problem, Backtracking Algorithm Recursive represented with a Adjacency matrix"""


SIZE = 5
MAZE = [
    [0, 1, 0, 1, 1],
    [0, 0, 0, 0, 0],
    [1, 0, 1, 0, 1],
    [0, 0, 1, 0, 0],
    [1, 0, 0, 1, 0]
]

START = (0, 0)
TARGET = (4, 4)
RAT_PATH = [[0]*SIZE for _ in range(SIZE)]
WALL = 1
RAT_STEP = 1


def rat_in_maze():

    def backtracking(y, x):

        if (y == TARGET[0]) and (x == TARGET[1]):  # NOTE: First step is checking if we found the target
            RAT_PATH[y][x] = 1
            return True

        if (y, x) >= START and (y < SIZE and x < SIZE):  # NOTE: 1 check footnotes
            visited = RAT_PATH[y][x]
            current = MAZE[y][x]
            if visited == 0 and current != WALL:
                RAT_PATH[y][x] = RAT_STEP  # NOTE: RAT makes a step
                if backtracking(y+1, x) or backtracking(y, x+1):  # NOTE: DOWN  | RIGHT
                    return True
                else:
                    if backtracking(y-1, x) or backtracking(y, x-1):  # NOTE: UP  | LEFT
                        return True
                RAT_PATH[y][x] = 0
                return
        return

    backtracking(START[0], START[1])
    for step in RAT_PATH:
        print(step)


if __name__ == '__main__':
    rat_in_maze()

# NOTE: 1 visited = solution[y][x] Check if Node is visited or not  | current = MAZE[y][x]
#  check if Node is not a 1 (so not a wall)

