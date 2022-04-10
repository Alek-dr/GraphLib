from typing import Dict, Union

from core.graphs.graph import AbstractGraph


def dijkstra(graph: AbstractGraph, origin: Union[str, int]) -> (Dict, Dict):
    """
    :param origin: name or id of origin node
    :return: dict of the shortest paths weights, dict of paths
    """
    if not graph[origin]:
        raise Exception("There no such node")
    unvisited = [v.name for v in graph.vertexes if v.name != origin]
    costs = {v.name: float("inf") for v in graph.vertexes}
    costs[origin] = 0
    paths = {origin: [origin]}
    current_node = origin
    while unvisited:
        for node in graph.get_adj_nodes(current_node):
            if node.dst in unvisited:
                d = node.weight + costs[current_node]
                if costs[node.dst] > d:
                    costs[node.dst] = d
                    paths[node.dst] = paths[current_node] + [node.dst]
        nearest = unvisited[0]
        min_w = costs[nearest]
        for node in unvisited:
            if costs[node] < min_w:
                min_w = costs[node]
                nearest = node
        unvisited.remove(nearest)
        current_node = nearest
    return costs, paths
