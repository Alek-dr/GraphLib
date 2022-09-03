from collections import OrderedDict, deque
from typing import Dict, Union

from core.graphs.gpath import GPath
from core.graphs.graph import AbstractGraph, edge


def dfs(
    graph: AbstractGraph, origin: Union[str, int], target: Union[str, int] = None
) -> Dict[Union[int, str], GPath]:
    """
    DFS algorithm
    :param graph: graph object
    :param origin: name or id of origin node
    :param target: node to find path. If target is None all paths will be returned
    :return: shortest path to target or all possible paths to all nodes if target is not specified
    """
    if (target is not None) and (not graph[target]):
        raise Exception("There no target node in graph")
    p = GPath(origin)
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
            path = GPath(curr_edge.dst)
            path.add_step(curr_edge)
            if paths.get(curr_edge.src):
                path = paths.get(curr_edge.src) + path
            paths[curr_edge.dst] = path
            edges = [e for e in graph.get_adj_edges(curr_edge.dst)]
            for e in reversed(edges):
                if e.dst not in visited:
                    stack.append(e)
                    if (target is not None) and (paths.get(target)):
                        return {target: paths[target]}
            edges.clear()
    return paths
