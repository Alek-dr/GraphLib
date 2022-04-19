from collections import OrderedDict
from typing import Union

from core.graphs.graph import AbstractGraph, edge
from core.graphs.path import Path


def dijkstra(graph: AbstractGraph, origin: Union[str, int]):
    """
    :param origin: name or id of origin node
    :return: dict of the shortest paths weights, dict of paths
    """
    if not graph[origin]:
        raise Exception("There no such node")
    unvisited = [v.name for v in graph.vertexes if v.name != origin]
    paths = OrderedDict()
    for v in graph.vertexes:
        path = Path(v.name)
        path.path_weight = float("inf")
        paths[v.name] = path
    paths[origin].path_weight = 0
    paths[origin].add_step(edge(origin, origin, 0, None))
    current_node = origin
    while unvisited:
        for edge_ in graph.get_adj_edges(current_node):
            if edge_.dst in unvisited:
                d = edge_.weight + paths[current_node].path_weight
                if paths[edge_.dst].path_weight > d:
                    if len(paths[edge_.dst].edges) == 0:
                        paths[edge_.dst].add_step(edge_)
                        paths[edge_.dst] = paths[edge_.src] + paths[edge_.dst]
                    else:
                        path = Path(edge_.dst)
                        path.add_step(edge_)
                        paths[edge_.dst] = paths[edge_.src] + path
                    paths[edge_.dst].path_weight = d
        nearest = unvisited[0]
        min_w = paths[nearest].path_weight
        for node in unvisited:
            if paths[node].path_weight < min_w:
                min_w = paths[node].path_weight
                nearest = node
        unvisited.remove(nearest)
        current_node = nearest
    return paths
