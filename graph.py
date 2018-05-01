class Graph(object):
    @classmethod
    def random_graph(cls, num_vertices, vertex_degree):
        """Returns a Graph with the given number of vertices, generated randomly
        according to the Jellyfish algorithm.

        Args:
            num_vertices (int)
            vertex_degree (int)

        Returns:
            Graph
        """
        pass

    def __init__(self, vertices, edges):
        """Creates a graph with these vertices.
        
        Args:
            vertices (list[Vertex])
        """
        pass

    def k_shortest_paths(self, k, start, end):
        """Returns the k shortest paths between start and end.

        Args:
            k (int)
            start (int): index of start Vertex
            end (int): index of end Vertex

        Returns:
            list[list[Vertex]]
        """
        pass


class Vertex(object):
    def __init__(self):
        self._neighbors = set()

    def add_neighbor(self, neighbor):
        self._neighbors.add(neighbor)

    @property
    def degree(self):
        return len(self._neighbors)
