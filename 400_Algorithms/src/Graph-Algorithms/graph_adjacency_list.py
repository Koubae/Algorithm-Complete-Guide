"""Graph represented with Adjacency list"""


class Node:
    def __init__(self, v):
        self.vertex = v
        self.neighbour = None

    def __repr__(self):
        return f'Vertex={self.vertex}'


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.path = [None] * self.V
        self.paths = []

    def add_path(self, u, v):
        node_u = Node(u)
        node_v = Node(v)

        node_u.neighbour = self.path[v]
        self.path[v] = node_u

        node_v.neighbour = self.path[u]
        self.path[u] = node_v

    def print_graph(self):
        for i in range(self.V):
            print(f"Adjacency list of vertex {i}\n Source Node {i}", end="")
            temp = self.path[i]
            while temp:
                print(f" -> {temp.vertex}", end="")
                temp = temp.neighbour
            print(" \n")

    def gen_path(self):
        for i in range(self.V):
            arr = []
            node = self.path[i]
            arr.append(f'Vertex={i}')
            while node:
                arr.append(node.vertex)
                node = node.neighbour
            self.paths.append(arr)


if __name__ == "__main__":
    V = 5
    graph = Graph(V)
    graph.add_path(0, 1)
    graph.add_path(0, 4)
    graph.add_path(1, 2)
    graph.add_path(1, 3)
    graph.add_path(1, 4)
    graph.add_path(2, 3)
    graph.add_path(3, 4)

    graph.print_graph()
    graph.gen_path()
    print(graph.paths)