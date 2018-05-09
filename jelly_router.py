import numpy as np
from ripl.routing import Routing
from collections import defaultdict


class JellyRouting(Routing):
    def __init__(self, topo):
        self._topo = topo
        self._paths = defaultdict(dict)

    def get_route(self, src, dst, pkt):
        print "Get {} --> {}".format(src, dst)
        if src == dst:
            return [src]
        src = self._topo.id_gen(name=src).dpid
        dst = self._topo.id_gen(name=dst).dpid
        if src not in self._paths or dst not in self._paths[src]:
            print "Not cached"
            graph = self._topo._graph
            #paths = graph.k_shortest_paths(1, src, dst)
            #paths = [self._topo.id_gen(dpid=x.uid).name_str() for path in paths for x in path]
            #self._paths[src][dst] = paths

            #paths = graph.k_shortest_paths(8, src, dst)
            #print "Path: {}".format(paths)
            #paths = [
            #    [self._topo.id_gen(dpid=x.uid).name_str() for x in path] for path in paths]
            #self._paths[src][dst] = paths

            path = graph.k_shortest_paths(1, src, dst)[0]
            print "Path: {}".format(path)
            path = [self._topo.id_gen(dpid=x.uid).name_str() for x in path]
            self._paths[src][dst] = path
        else:
            print "Cached"
        path = self._paths[src][dst]
        print "Self._paths: {}".format(self._paths)
        #self._paths.clear()
        return path
        #return self._paths[src][dst][np.random.randint(len(self._paths[src][dst]))]
