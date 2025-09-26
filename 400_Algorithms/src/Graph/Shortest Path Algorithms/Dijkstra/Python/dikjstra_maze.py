# CREDIT of this code all to realpython
# The Python heapq Module: Using Heaps and Priority Queues
# https://realpython.com/python-heapq-module/

import heapq


map = """\
.......X..
.......X..
....XXXX..
..........
..........
"""


def parse_map(map):
    lines = map.splitlines()
    origin = 0, 0
    destination = len(lines[-1]) - 1, len(lines) - 1  # (9, 4)
    return lines, origin, destination


def get_neighbors(lines, current):
    x, y = current  # FAQ: GEts coordinates of current Node
    graph_lines = len(lines)
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:   # Skips Coords which are the starting points (0,0)
                continue
            x_ = x+dx
            y_ = y + dy
            if not (0 <= y_ < graph_lines and 0 <= x_ < len(lines[y_])):
                continue
            elif lines[y_][x_] == 'X':
                continue
            else:
                yield x_, y_


def find_path(map):
    # , (0, 0), (9,4)
    graph, origin, destination = parse_map(map)

    connections = {origin: []}
    next_nodes = [(0, origin)]  # Nodes push in the queue to be checked 
    visited = set()

    while destination not in visited:

        _ignored, current = heapq.heappop(next_nodes)
        if current in visited:  # FAQ: Checks if current node has been visited
            continue
        visited.add(current)    # FAQ: If not, adds the current Node to visited set.
        neighbors = set(get_neighbors(graph, current)) - visited

        def get_shorter_paths():
            path = connections[current] + [current]
            for node in neighbors:
                if node in connections and len(connections[node]) <= len(path):
                    continue
                yield node, path

        shorter = get_shorter_paths()

        for neighbor, path in shorter:
            connections[neighbor] = path
            heapq.heappush(next_nodes, (len(path), neighbor))

    if destination in connections:
        return connections[destination] + [destination]
    else:

        raise ValueError("no path")


def show_path(path, map):
    lines = map.splitlines()

    for x, y in path:
        lines[y] = lines[y][:x] + "@" + lines[y][x + 1 :]
    return "\n".join(lines) + "\n"


if __name__ == '__main__':    
    path = find_path(map)
    # print(path)  # [(0, 0), (1, 0), (2, 1), (3, 2), (4, 3), (5, 3), (6, 3), (7, 3), (8, 3), (9, 4)]
    print(show_path(path, map))


# NOTE: The Graph is rapresented with Dots in a 2 D plane with X and Y coordinates
#  The starting Point and coodrdinate (x=0,Y=0) is the top left corner of the Graph, namely index (0,0)
#  From any node you can move up, down, left, right and diagonal
#  X means a Wall