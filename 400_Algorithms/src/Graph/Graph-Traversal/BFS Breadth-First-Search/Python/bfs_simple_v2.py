"""Breadth First Search in Python with a Directed graph represented Adjacency list V_2"""
import collections


def bfs(graph, source):
    visited  = set()
    queue = collections.deque([source])
    visited.add(source)

    while queue:
        current = queue.popleft()

        for neighbour in graph[current]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)
    return visited


if __name__ == '__main__':
    graph = {0: [1, 2], 1: [2], 2: [3], 3: [1, 2]}
    result = bfs(graph, 0)
    print(result)