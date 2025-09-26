# -*- coding: utf-8 -*-
"""
@Author: Federico Bau
@Date: 01/08/2022


"""


def depth_first_search(graph):
    visited = set()
    path = []

    def recursive(graph, vertex, visited):
        if vertex in visited:
            return
        path.append(vertex)
        visited.add(vertex)
        print(vertex, end=' -> ')
        for adj in graph[vertex]:
            recursive(graph, adj, visited)

    recursive(graph, '1', visited)

    return path


def depth_first_search_loop(graph):
    root = '1'

    visited = set()
    stack = [root]

    while stack:

        current_node = stack.pop()
        if current_node in visited:
            continue
        visited.add(current_node)
        print(current_node, end=' -> ')
        # this works because adds into reverse order the nodes into the stack
        # allowing the first encountered node to be immediatelly evaluated
        for adj in graph[current_node][::-1]:
            stack.append(adj)


if __name__ == '__main__':
    graph = {
        '1': ['5', '9'],
        '5': ['2', '4'],
        '9': ['8', '99'],
        '3': ['12', '15'],
        '2': ['4', '3'],
        '4': ['2'],
        '8': [],
        '99': [],
        '15': [],
        '12': ['55', '56'],
        '55': [],
        '56': [],
    }
    result = depth_first_search(graph)
    print("")
    depth_first_search_loop(graph)
    # print(' -> '.join(result))