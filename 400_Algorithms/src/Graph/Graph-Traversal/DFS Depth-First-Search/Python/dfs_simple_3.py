# noinspection DuplicatedCode


def dfs_traverse(graph: dict) -> list[int]:
    visited: set[int] = set()
    path: list[int] = []

    def _traverse(vertex: int) -> None:
        if vertex in visited:
            return

        visited.add(vertex)
        path.append(vertex)

        for neighbour in graph[vertex]:
            _traverse(neighbour)

    for node in graph:
        _traverse(node)
    return path

def dfs_traverse_route(graph: dict, vertex: int) -> list[int]:
    visited = set()
    path = []

    def _traverse(_vertex: int) -> None:
        if _vertex in visited:
            return

        visited.add(_vertex)
        path.append(_vertex)

        for neighbour in graph[_vertex]:
            _traverse(neighbour)

    _traverse(vertex)
    return path

def main():
    graph = {
        0: [1, 2],  # A connects to B, C
        1: [0, 3],  # B connects to A, D
        2: [0, 3],  # C connects to A, D
        3: [1, 2]   # D connects to B, C
    }

    connections = dfs_traverse(graph)
    print(connections)

    path_from_3 = dfs_traverse_route(graph, 3)
    print(path_from_3)


if __name__ == '__main__':
    main()
