from collections import OrderedDict
from typing import Dict, Union

from core.algorithms.utils import update_path
from core.graphs.gpath import GPath
from core.graphs.graph import AbstractGraph, edge


def dijkstra(
        graph: AbstractGraph, origin: Union[str, int]
) -> Dict[Union[int, str], GPath]:
    """
    Dijkstra's algorithm
    :param graph: graph object
    :param origin: name or id of origin node
    :return: dict of paths
    """
    if not graph[origin]:
        raise Exception(f"There no such node: {origin}")
    unvisited = [v.name for v in graph.vertexes if v.name != origin]
    paths = OrderedDict()
    for v in graph.vertexes:
        path = GPath(v.name)
        path.path_weight = float("inf")
        paths[v.name] = path
    paths[origin].path_weight = 0
    paths[origin].add_step(edge(origin, origin, 0, None))
    current_node = origin
    while unvisited:
        for e in graph.get_adj_edges(current_node):
            if e.dst in unvisited:
                d = e.weight + paths[current_node].path_weight
                if paths[e.dst].path_weight > d:
                    paths = update_path(paths, e, d)
        nearest = unvisited[0]
        min_w = paths[nearest].path_weight
        for node in unvisited:
            if paths[node].path_weight < min_w:
                min_w = paths[node].path_weight
                nearest = node
        unvisited.remove(nearest)
        current_node = nearest
    return paths
