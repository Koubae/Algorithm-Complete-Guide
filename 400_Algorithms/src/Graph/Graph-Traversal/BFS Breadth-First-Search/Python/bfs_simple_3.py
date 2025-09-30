# noinspection DuplicatedCode
from collections import deque

def bfs_traverse(graph: dict) -> list[int]:
    visited: set[int] = set()
    path: list[int] = []


    def _traverse(vertex: int) -> None:
        if vertex in visited:
            return

        queue = deque([vertex])
        while queue:
            current = queue.pop()
            if current in visited:
                continue

            visited.add(current)
            path.append(current)

            for neighbour in graph[current]:
                queue.appendleft(neighbour)

    for node in graph:
        _traverse(node)
    return path

def bfs_traverse_route(graph: dict, vertex: int) -> list[int]:
    visited = set()
    queue = deque([vertex])
    path = []

    while queue:
        current = queue.pop()
        if current in visited:
            continue

        visited.add(current)
        path.append(current)

        for neighbour in graph[current]:
            if neighbour not in visited:
                queue.appendleft(neighbour)
    return path

def main():
    graph = {
        0: [1, 2],  # A connects to B, C
        1: [0, 3],  # B connects to A, D
        2: [0, 3],  # C connects to A, D
        3: [1, 2]   # D connects to B, C
    }

    connections = bfs_traverse(graph)
    print(connections)

    path_from_3 = bfs_traverse_route(graph, 3)
    print(path_from_3)


if __name__ == '__main__':
    main()
