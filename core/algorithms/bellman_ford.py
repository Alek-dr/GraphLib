from collections import OrderedDict, deque
from typing import Dict, Tuple, Union

from core.algorithms.utils import update_walks
from core.graphs.graph import AbstractGraph, edge
from core.graphs.walk import Walk


def bellman_ford(
    graph: AbstractGraph, origin: Union[str, int]
) -> Tuple[Dict[Union[int, str], Walk], bool]:
    """
    Bellman–Ford algorithm
    :param graph: graph object
    :param origin: name or id of origin node
    :return: dict of paths, ncc value true, if graph has no negative-weight cycle, false otherwise
    """
    if not graph[origin]:
        raise Exception(f"There no such node: {origin}")
    walks = OrderedDict()
    inqueue = {}
    for v in graph.vertexes:
        walk = Walk(v.name)
        walk.weight = float("inf")
        walks[v.name] = walk
        inqueue[v.name] = False
    walks[origin].weight = 0
    walks[origin].add_step(edge(origin, origin, 0, None))
    queue = deque()
    e = edge(origin, origin, 0, None)
    queue.append(e)
    signal_edge = edge(-1, -1, 0, None)
    queue.append(signal_edge)
    inqueue[origin] = True
    i = 0
    while len(queue) != 1 and i < graph.n_vertex:
        curr_edge = queue.popleft()
        if curr_edge == signal_edge:
            i += 1
            queue.append(signal_edge)
        else:
            inqueue[curr_edge.dst] = False
            for e in graph.get_adj_edges(curr_edge.dst):
                d = walks[e.src].weight + e.weight
                if walks[e.dst].weight > d:
                    walks = update_walks(walks, e, d)
                    if not inqueue[e.dst]:
                        queue.append(e)
                        inqueue[e.dst] = True
    ncc = i < graph.n_vertex
    return walks, ncc
