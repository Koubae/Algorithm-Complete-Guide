import heapq


class Vertex:
    def __init__(self, node):
        self.node = node
        self.adjacent = {}
        self._distance = float('inf')
        self._previous = None
        self.visited = False

    @property
    def distance(self):
        return self._distance

    @distance.setter
    def distance(self, dist):
        self._distance = dist

    @property
    def previous(self):
        return self._previous

    @previous.setter
    def previous(self, prev):
        self._previous = prev

    def add_neighbor(self, neighbor, weight=None):
        self.adjacent[neighbor] = weight

    def get_weight(self, neighbor):
        return self.adjacent[neighbor]

    def __str__(self):
        return f'Node {str(self.node)} adjacent Nodes: {str([x.node for x in self.adjacent])}'

    def __repr__(self):
        return f'Node {str(self.node)}'

    def __hash__(self):
        return hash(self.node)

    def __lt__(self, other):
        return self.distance < other.distance


class Graph:
    def __init__(self):
        self.map = dict()
        self.total_vertices = 0
        self.path_to_target = []
        self._target = None

    @property
    def target(self):
        return self._target

    @target.setter
    def target(self, node):
        target_node = self.map[node]
        if target_node:
            self._target = target_node
        else:
            pass

    def __iter__(self):
        return iter(self.map.values())

    def add_path(self, source, destination, weight=0):
        if source not in self.map:
            self.total_vertices += 1
            self.map[source] = Vertex(source)
        if destination not in self.map:
            self.total_vertices += 1
            self.map[destination] = Vertex(destination)
        self.map[source].add_neighbor(self.map[destination], weight)
        self.map[destination].add_neighbor(self.map[source], weight)

    def shortest_path(self):
        target = self.target
        if target:
            self.path_to_target.append(target.node)

            def get_path(prev_target):
                if prev_target.previous:
                    self.path_to_target.append(prev_target.previous.node)
                    get_path(prev_target.previous)
                else:
                    return
            get_path(target)
            return self.path_to_target[::-1]
        else:
            print('Set a Target First!!!')
            return NotImplemented

    @staticmethod
    def dijkstra(graph, start_node):
        """Dijkstra's shortest path"""

        start_node = graph.map[start_node]
        start_node.distance = 0  # FAQ: Start Node is Always 0
        unvisited_queue = [(v.distance, v) for v in graph]
        heapq.heapify(unvisited_queue)

        for _ in range(len(unvisited_queue)):
            uv = heapq.heappop(unvisited_queue)
            current = uv[1]
            current.visited = True

            for neighbour in current.adjacent:
                if neighbour.visited:
                    continue
                else:
                    neighbour_dist = neighbour.distance

                    new_dist = current.distance + current.get_weight(neighbour)

                    if new_dist < neighbour_dist:
                        neighbour.distance = new_dist
                        neighbour.previous = current
                    else:
                        continue
            unvisited_queue = [(v.distance, v) for v in graph if not v.visited]  # 2. Push unvisited V into the queue


if __name__ == '__main__':
    g = Graph()
    g.add_path('a', 'b', 7)
    g.add_path('a', 'c', 9)
    g.add_path('a', 'f', 14)
    g.add_path('b', 'c', 10)
    g.add_path('b', 'd', 15)
    g.add_path('c', 'd', 11)
    g.add_path('c', 'f', 2)
    g.add_path('d', 'e', 6)
    g.add_path('e', 'f', 9)
    g.target = 'e'
    g.dijkstra(g, 'a')
    print(g.shortest_path()) # ['a', 'c', 'f', 'e']