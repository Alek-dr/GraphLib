from collections import OrderedDict, deque
from typing import Dict, Union

from core.graphs.graph import AbstractGraph, edge
from core.graphs.path import Path


def dfs(
    graph: AbstractGraph, origin: Union[str, int], target: Union[str, int] = None
) -> Dict[Union[int, str], Path]:
    """
    :param origin: name or id of origin node
    :param target: node to find path. If target is None all paths will be returned
    :return: shortest path to target or all possible paths to all nodes if target is not specified
    """
    if (target is not None) and (not graph[target]):
        raise Exception("There no target node in graph")
    p = Path(origin)
    if origin == target:
        return {origin: p}
    stack = deque()
    stack.append(edge(origin, origin, 0, None))
    visited = set()
    paths = OrderedDict()
    while stack:
        curr_edge = stack.pop()
        if curr_edge.dst not in visited:
            visited.add(curr_edge.dst)
            path = Path(curr_edge.dst)
            path.add_step(curr_edge)
            if paths.get(curr_edge.src):
                path = paths.get(curr_edge.src) + path
            paths[curr_edge.dst] = path
            edges = [edge_ for edge_ in graph.get_adj_nodes(curr_edge.dst)]
            for edge_ in reversed(edges):
                if edge_.dst not in visited:
                    stack.append(edge_)
                    if (target is not None) and (paths.get(target)):
                        return {target: paths[target]}
            edges.clear()
    return paths
