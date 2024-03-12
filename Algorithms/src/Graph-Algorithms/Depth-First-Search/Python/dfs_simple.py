"""Depth First Search traversal from a given given graph"""
from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def app_path(self, u, v):
        self.graph[u].append(v)

    def algorithm(self, v, visited):  # NOTE: Recursive Function
        visited.add(v)
        print(v, end=' ')
        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.algorithm(neighbour, visited)

    def dfs(self, v):
        visited = set()
        self.algorithm(v, visited)


if __name__ == '__main__':
    g = Graph()
    g.app_path(0, 1)
    g.app_path(0, 2)
    g.app_path(1, 2)
    g.app_path(2, 0)
    g.app_path(2, 3)
    g.app_path(3, 3)
    g.dfs(2)