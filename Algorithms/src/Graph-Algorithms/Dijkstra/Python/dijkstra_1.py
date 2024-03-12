from heapq import heappop, heappush


# Data structure to store graph edges
class Path:
    def __init__(self, source, dest, weight):
        self.source = source
        self.dest = dest
        self.weight = weight


# Data structure to store heap nodes
class Node:
    def __init__(self, vertex, weight):
        self.vertex = vertex
        self.weight = weight

    # 'Override the __lt__() function to make `Node` class work with min heap
    def __lt__(self, other):
        return self.weight < other.weight


# class to represent a graph object
class Graph:
    def __init__(self, paths, N):
        # allocate memory for the adjacency list
        self.adj = [[] for _ in range(N)]
        # add paths to the undirected graph by Index or Node u
        for path in paths:
            self.adj[path.source].append(path)


def get_route(prev, i, route):
    if i >= 0:
        get_route(prev, prev[i], route)
        route.append(i)


# Run Dijkstra's algorithm on given graph
def shortest_path(graph, source, N):
    # create min heap and push source node having distance 0
    pq = []
    heappush(pq, Node(source, 0))
    # set distance from source to v infinite initially
    dist = [float('inf')] * N

    # distance from source to itself is zero
    dist[source] = 0

    # list to track vertices for which minimum cost is already found
    visited = [False] * N
    visited[source] = True

    # stores predecessor of a vertex (to print path)
    prev = [-1] * N
    route = []

    # run till min heap is empty
    while pq:

        node = heappop(pq)  # Remove and return best vertex
        u = node.vertex  # get vertex number

        # do for each neighbor v of u
        for path in graph.adj[u]:
            v = path.dest
            weight = dist[u] + path.weight

            # Relaxation step
            if not visited[v] and weight < dist[v]:
                dist[v] = weight
                prev[v] = u
                heappush(pq, Node(v, dist[v]))

        # marked vertex u as visited
        visited[u] = True

    for i in range(1, N):
        if i != source and dist[i] != float('inf'):
            get_route(prev, i, route)
            # print(f"Path ({source} -> {i}): Minimum Cost = {dist[i]}, Route = {route}")
            route.clear()


if __name__ == '__main__':
    # initialize paths as per above diagram
    # (u, v, w) triplet represent undirected path from
    # vertex u to vertex v having weight w
    paths = [Path(0, 1, 10), Path(0, 4, 3), Path(1, 2, 2),
             Path(1, 4, 4), Path(2, 3, 9), Path(3, 2, 7),
             Path(4, 1, 1), Path(4, 2, 8), Path(4, 3, 2)]

    # Set number of vertices in the graph
    N = 5

    # construct graph
    graph = Graph(paths, N)

    source = 0
    shortest_path(graph, source, N)

# Path (0 -> 1): Minimum Cost = 4, Route = [0, 4, 1]
# Path (0 -> 2): Minimum Cost = 6, Route = [0, 4, 1, 2]
# Path (0 -> 3): Minimum Cost = 5, Route = [0, 4, 3]
# Path (0 -> 4): Minimum Cost = 3, Route = [0, 4]