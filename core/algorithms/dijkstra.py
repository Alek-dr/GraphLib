from collections import OrderedDict
from typing import Dict, Union

from core.algorithms.utils import update_walks
from core.graphs.graph import AbstractGraph, edge
from core.graphs.walk import Walk


def dijkstra(
    graph: AbstractGraph, origin: Union[str, int]
) -> Dict[Union[int, str], Walk]:
    """
    Dijkstra's algorithm
    :param graph: graph object
    :param origin: name or id of origin node
    :return: dict of paths
    """
    if not graph[origin]:
        raise Exception(f"There no such node: {origin}")
    unvisited = [v.name for v in graph.vertexes if v.name != origin]
    walks = OrderedDict()
    for v in graph.vertexes:
        walk = Walk(v.name)
        walk.weight = float("inf")
        walks[v.name] = walk
    walks[origin].weight = 0
    walks[origin].add_step(edge(origin, origin, 0, None))
    current_node = origin
    while unvisited:
        for e in graph.get_adj_edges(current_node):
            if e.dst in unvisited:
                d = e.weight + walks[current_node].weight
                if walks[e.dst].weight > d:
                    walks = update_walks(walks, e, d)
        nearest = unvisited[0]
        min_w = walks[nearest].weight
        for node in unvisited:
            if walks[node].weight < min_w:
                min_w = walks[node].weight
                nearest = node
        unvisited.remove(nearest)
        current_node = nearest
    return walks
