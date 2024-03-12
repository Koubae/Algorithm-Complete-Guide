"""Graph represented with Adjacency Matrix Credit: https://ide.geeksforgeeks.org/9je5j6jJ13 Rajat Singhal"""
from string import ascii_lowercase


class Graph:
    def __init__(self, num_vertex):
        self.graph_matrix = [[-1] * num_vertex for _ in range(num_vertex)]  # FAQ: Creates Graph's Matrix set Default w to -1
        self.num_vertex = num_vertex   # FAQ: Stores N of V
        self.vertices = {}   # FAQ: Dict Key=V.name Value= V.index
        self.vertices_list = [0] * num_vertex   # Stores V Name by Index
        self.set_vertex()

    def set_vertex(self):
        for v in range(self.num_vertex):
            id = ascii_lowercase[v]
            self.vertices[id] = v
            self.vertices_list[v] = id

    def set_path(self, u, v, cost=0):  # FAQ: Set path from Vertex u to Vertex v using IDs
        u = self.vertices[u]
        v = self.vertices[v]
        self.graph_matrix[u][v] = cost  # NOTE: Add Path from u to v and not vice versa!
        self.graph_matrix[v][u] = cost  # NOTE: for directed graph do not add this  | This makes it possible 2 ways path

    def get_vertex(self):
        return self.vertices_list

    def get_edges(self):
        edges = []
        for i in range(self.num_vertex):
            for j in range(self.num_vertex):
                if self.graph_matrix[i][j] > -1:  # FAQ: If value is -1 means that there isn't a edge
                    edges.append((self.vertices_list[i], self.vertices_list[j], self.graph_matrix[i][j]))
        return edges

    def get_matrix(self):
        return self.graph_matrix
#
#
G = Graph(6)
G.set_path('a', 'e', 10)
G.set_path('a', 'c', 20)
G.set_path('c', 'b', 30)
G.set_path('b', 'e', 40)
G.set_path('e', 'd', 50)
G.set_path('f', 'e', 60)
print(f"Vertices of Graph => {G.get_vertex()}\n")
print(f"Edges of Graph:\n{G.get_edges()}\n", '==='*30, '\n')
print(f"Adjacency Matrix of Graph =>\n{G.get_matrix()}")