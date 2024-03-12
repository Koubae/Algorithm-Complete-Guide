class Dijkstra:

    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = None
        self.v_distance = [float("inf")] * self.vertices
        self.shortest_path = [False] * self.vertices  # FAQ: Checks if a Vertices' shortest route has been found.
      #  self.ShortestPathTree = namedtuple('ShortestPathTree', ['V_' + str(V+1) for V in range(self.vertices)])

    def min_distance(self):
        check_node = float("inf")
        min_index = 0
        for v in range(self.vertices):
            if not self.v_distance[v]:
                continue
            elif self.v_distance[v] < check_node and not self.shortest_path[v]:
                check_node = self.v_distance[v]  # FAQ: Set min_dist to Current Dist[v]
                min_index = v
        return min_index

    def dijkstra(self, source):

        self.v_distance[source] = 0  # FAQ: Set Starting Node by Index as 0

        for idx, _ in enumerate(range(self.vertices)):
            if idx != 0:  # FAQ: Algorithm will always start at index 0 because the Graph is relative to source
                current = self.min_distance()  # Index of Vertex with shortest route
            else:
                current = idx
                self.shortest_path[idx] = True
            self.neighbour_path(current)


        # shortest_path = self.ShortestPathTree(*self.v_distance)
        return self.v_distance

    def neighbour_path(self, current):
        # FAQ: Check neighbour Nodes and Update distance
        for v in range(self.vertices):
            neighbour = self.graph[current][v]
            if neighbour <= 0:
                continue
            n_path = self.v_distance[current] + neighbour
            if v == current:  # FAQ: Skip himself in the check as it's always 0
                continue
            elif self.v_distance[v] > n_path:
                self.shortest_path[current] = True
                self.v_distance[v] = n_path
            else:
                continue
                
if __name__ == '__main__':    
    g = Dijkstra(8+1)
    g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],  # 0
                [4, 0, 8, 0, 0, 0, 0, 11, 0], # 1
                [0, 8, 0, 7, 0, 4, 0, 0, 2],  # 2
                [0, 0, 7, 0, 9, 14, 0, 0, 0],  # 3
                [0, 0, 0, 9, 0, 10, 0, 0, 0], # 4
                [0, 0, 4, 14, 10, 0, 2, 0, 0], # 5
                [0, 0, 0, 0, 0, 2, 0, 1, 6], # 6
                [8, 11, 0, 0, 0, 0, 1, 0, 7], # 7
                [0, 0, 2, 0, 0, 0, 6, 7, 0] # 8
                ]
    
    print(g.dijkstra(0))