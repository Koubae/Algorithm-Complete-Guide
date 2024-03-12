"""
Bread-First-Search solve issue Shortest Distance from All Buildings

Suppose we want to make a house on an empty land which reaches all buildings
in the shortest amount of distance. We can only move four directions like up, down, left and right.
We have a 2D grid of values 0, 1 or 2, where −

    0 represents an empty land which we can pass by freely.

    1 represents a building which we cannot pass through.

    2 represents an obstacle which we cannot pass through.

NOTE OBJECTIVE:

    Find the Node 0 which has the shortest Path to All the Building (Nodes 1).

INPUT:

    [1, 0, 2, 0, 1],
    [0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0]

OUTPUT: 7

NOTE HINT:

    Calculate distance from Node 0 to 1 individually for each node 1 and then sum it up. The
    smaller value is the result

TODO: Implement with collections.deque
"""


def bfs(grid, matrix, row, column, visited):
    queue = [(row, column, 0)]
    len_row = len(grid)
    len_col = len(grid[0])
    while queue:
        cur_row, cur_col, step = queue.pop(0)
        up = (cur_row-1, cur_col); down = (cur_row+1, cur_col); left = (cur_row, cur_col-1); right = (cur_row, cur_col+1)
        directions = [up, down, left, right]  # FAQ: 1
        for row, col in directions:  # FAQ: 2

            if 0<=row<len_row and 0<=col<len_col and grid[row][col] == 0:
                matrix_map = matrix[row][col]
                if matrix_map[1] == visited:
                    matrix_map[0] += step+1    # FAQ: Counts the steps from Node 1 (building) to Node 0 (free)
                    matrix_map[1] = visited+1  # FAQ: Should be 3
                    queue.append((row, col, step+1))
            else:
                continue


def shortest_distance(grid):
    if not grid or not grid[0]:
        return -1

    rows = range(len(grid))
    column = range(len(grid[0]))
    matrix = [[[0, 0] for _ in column] for _ in rows]
    building_counter = 0    # FAQ: Counts all the Building nodes
    best_node = float('inf')
    best_node_index = [0]

    def find_building():
        nonlocal building_counter
        for row in rows:
            for col in column:
                if grid[row][col] == 1:
                    bfs(grid, matrix, row, col, building_counter)
                    building_counter += 1
    find_building()

    for i in rows:
        for j in column:
            if matrix[i][j][1]==building_counter:
                value = min(best_node, matrix[i][j][0])
                if value < best_node:
                    best_node = value
                    best_node_index[0] = (i, j)

    return (best_node, best_node_index) if best_node!=float('inf') else -1


def print_result(result):
    if not result:
        print('Oh oh.. seem you haven\'t find the solution :()')
    else:
        print(f'Best Node to set the House found!!!\nNode is {result[0]} in index --> {result[1]}')


graph = [
    [1, 0, 2, 0, 1],
    [0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0]
]

result = shortest_distance(graph)
print_result(result)


# FAQ: 1 4 Direction 1. Up | 2. Down  | 3. Left | 4. Right

# FAQ: 2.
#  A. Check Current Node in the 4 directions
#  B. Accepts Values >= 0 if -1 means is out f the Grid
#  C. Goes only if we are in 0 step (so not steps 1 or 2) 3.

