"""
A breadth-first search implementation from:
"Python Algorithms: Mastering Basic Algorithms in the Python Language"
by      Magnus Lie Hetland
Modified Federico Bau
ISBN:   9781484200551
Input consists of a simple graph of { node: [list of neighbors] } plus a source and target node.
"""
from collections import deque


def bfs(graph, source, target):
    """Return the shortest path from the source (source) to the target (target) in the graph"""

    if source not in graph:
        raise AttributeError(f"ERROR! The source Node'{source}' is not in the graph")
    if target not in graph:
        raise AttributeError(f"ERROR! The target '{target}' is not in the graph")

    parents = {source: None}
    queue = deque([source])
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if neighbor not in parents:
                parents[neighbor] = node
                queue.append(neighbor)
                if node == target:
                    break

    path = [target]
    while parents[target] is not None:
        path.insert(0, parents[target])
        target = parents[target]

    return deque(path)


"""
Test using the graph from: 
https://commons.wikimedia.org/wiki/File:Graph_with_Chordless_and_Chorded_Cycles.svg
"""

map = {
    "a": ["b", "f"],
    "b": ["a", "c", "g"],
    "c": ["b", "d", "g", "l"],
    "d": ["c", "e", "k"],
    "e": ["d", "f"],
    "f": ["a", "e"],
    "g": ["b", "c", "h", "l"],
    "h": ["g", "i"],
    "i": ["h", "j", "k"],
    "j": ["i", "k"],
    "k": ["d", "i", "j", "l"],
    "l": ["c", "g", "k"],
}


def get_shortest_path(route):
    """Funciont that Pretty prints the shortest route given a best route (route)"""
    source_node = route[0]
    target_node = route[-1]
    print('\n' + '==='*10 + ' < ' + f'Shortest Path from Node {source_node.upper()} to '
                             f'Node {target_node.upper()}' + ' > ' + '==='*10)
    for node in route:
        print(node.upper(), end='')
        if node != target_node:
            print(' -> ', end='')
        else:
            continue
    print()
    print('==='*34)


route_a_1 = bfs(map, 'a', 'e')
route_a_2 = bfs(map, 'a', 'd')
route_a_3 = bfs(map, 'a', 'l')
route_a_4 = bfs(map, 'a', 'i')
route_a_5 = bfs(map, 'a', 'j')

route_d_1 = bfs(map, 'd', 'h')
route_d_2 = bfs(map, 'd', 'b')
route_d_3 = bfs(map, 'd', 'g')

route_h_1 = bfs(map, 'h', 'f')
route_h_2 = bfs(map, 'h', 'l')
route_h_3 = bfs(map, 'h', 'e')

routes = [
    route_a_1,
    route_a_2,
    route_a_3,
    route_a_4,
    route_a_5,
    route_d_1,
    route_d_2,
    route_d_3,
    route_h_1,
    route_h_2,
    route_h_3
]

for route in routes:
    get_shortest_path(route)
    
