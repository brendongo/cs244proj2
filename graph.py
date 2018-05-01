import numpy as np


class Graph(object):
    @classmethod
    def rrg(cls, num_vertices, vertex_degree):
        """Returns a Graph with the given number of vertices, generated randomly
        according to the Jellyfish algorithm.

        Args:
            num_vertices (int)
            vertex_degree (int)

        Returns:
            Graph
        """
        def unconnected_vertices(vertices):
            candidates = []
            for i in xrange(len(vertices)):
                for j in xrange(i, len(vertices)):
                    if vertices[i].degree < vertex_degree and \
                            vertices[j].degree < vertex_degree and \
                            vertices[i] not in vertices[j].neighbors:
                        candidates.append((vertices[i], vertices[j]))
            return candidates

        vertices = [Vertex(i) for i in xrange(num_vertices)]
        while True:
            candidates = unconnected_vertices(vertices)
            if not candidates:
                break
            selected_edge = candidates[np.random.randint(len(candidates))]
            selected_edge[0].add_neighbor(selected_edge[1])
            selected_edge[1].add_neighbor(selected_edge[0])

        free_vertices = \
            [v for v in vertices if v.degree <= vertex_degree - 2]
        edges = [(v, neighbor) for v in vertices
                 for neighbor in v.neighbors if v.uid < neighbor.uid]

        while len(free_vertices) > 0:
            selected_vertex = np.random.choice(free_vertices)
            selected_edge = edges[np.random.randint(len(edges))]
            if selected_vertex != selected_edge[0] and \
                    selected_vertex != selected_edge[1]:
                selected_edge[0].remove_neighbor(selected_edge[1])
                selected_edge[1].remove_neighbor(selected_edge[0])
                edges.remove(selected_edge)

                # Add the new edges
                selected_vertex.add_neighbor(selected_edge[0])
                selected_edge[0].add_neighbor(selected_vertex)
                selected_vertex.add_neighbor(selected_edge[1])
                selected_edge[1].add_neighbor(selected_vertex)

                if selected_vertex.uid < selected_edge[0].uid:
                    edges.append((selected_vertex, selected_edge[0]))
                    edges.append((selected_vertex, selected_edge[1]))
                elif selected_vertex.uid < selected_edge[1].uid:
                    edges.append((selected_edge[0], selected_vertex))
                    edges.append((selected_vertex, selected_edge[1]))
                else:
                    edges.append((selected_edge[0], selected_vertex))
                    edges.append((selected_edge[1], selected_vertex))

                # Update free vertices
                if selected_vertex.degree >= vertex_degree - 1:
                    free_vertices.remove(selected_vertex)
        return Graph(vertices)

    def __init__(self, vertices):
        """Creates a graph with these vertices.

        Args:
            vertices (list[Vertex])
        """
        self._vertices = vertices

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

    def __str__(self):
        s = ""
        for v in self._vertices:
            s += "{}\n".format(v)
        return s
    __repr__ = __str__


class Vertex(object):
    def __init__(self, uid):
        """
        Args:
            uid (int): unique identifier
        """
        self.uid = uid
        self._neighbors = set()

    def add_neighbor(self, neighbor):
        self._neighbors.add(neighbor)

    def remove_neighbor(self, neighbor):
        self._neighbors.remove(neighbor)

    @property
    def neighbors(self):
        return self._neighbors

    @property
    def degree(self):
        return len(self._neighbors)

    def __str__(self):
        return "[{}] --> {}".format(self.uid, [n.uid for n in self.neighbors])
    __repr__ = __str__


print Graph.rrg(11, 4)
