"""
    Breadth First Search for Graph
    Count Number of Nodes given a depth level in a tree

    @date: 1 - Jan - 2021
"""


def create_graph(nodes, paths):
    nodes = [[node, False, 0] for node in range(nodes)] # Idx 1 Node, Idx 2 Visited bool, Idx 3 count step
    paths_map = dict()
    for node, path in paths:
        if node in paths_map:
            paths_map[node] += [path]
        else:
            paths_map.setdefault(node, [path])
    return nodes, paths_map


def bfs_find_nodes(input, target):

    nodes, paths_map = input
    visited_flags = [visited[1] for visited in nodes]
    neighbour_nodes = []
    current_node_idx = 0
    while True:

        if all(visited_flags):
            break
        neighbours = paths_map.get(current_node_idx, None)
        if not neighbours:
            visited_flags[current_node_idx] = True
        else:
            neighbour_nodes += neighbours
            current_path_count = nodes[current_node_idx][2] + 1 # Add The Prev count plus one
            for node in neighbours:
                nodes[node][2] += current_path_count
            visited_flags[current_node_idx] = True  # Set Current Node to Visited

        if neighbour_nodes: # Check if Queue is empty
            next_node = neighbour_nodes.pop(0)
            current_node_idx = next_node

    count = 0
    for node in nodes:
        if node[2] == target:
            count += 1
    return count


if __name__ == '__main__':
    nodes = 7
    target_depth = 2
    paths = [
        (0, 1),
        (0, 2),
        (1, 3),
        (1, 4),
        (1, 5),
        (2, 6)
    ]

    expected_result = 4
    graph = create_graph(nodes, paths)
    answer_1 = bfs_find_nodes(graph, target_depth)
    print(answer_1)  # 4
    assert answer_1 == expected_result

    nodes = 6
    target_depth = 2
    paths = [
        (0, 1),
        (0, 2),
        (1, 3),
        (2, 4),
        (2, 5)
    ]

    expected_result = 3
    graph = create_graph(nodes, paths)
    answer_2 = bfs_find_nodes(graph, target_depth)
    print(answer_2)
    assert answer_2 == expected_result
    