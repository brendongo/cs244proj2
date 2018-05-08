from ripl.routing import Routing
from collections import defaultdict


class JellyRouting(Routing):
    def __init__(self, topo):
        self._topo = topo
        self._paths = defaultdict(dict)

    def get_route(self, src, dst, pkt):
        if src == dst:
            return [src]
        if src not in self._paths or dst not in self._paths[src]:
            graph = self._topo._graph
            src = self._topo.id_gen(name=src).dpid
            dst = self._topo.id_gen(name=dst).dpid
            path = graph.k_shortest_paths(1, src, dst)[0]
            path = [self._topo.id_gen(dpid=x.uid).name_str() for x in path]
            self._paths[src][dst] = path
        return self._paths[src][dst]
