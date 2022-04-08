from collections import deque
from typing import Union, Dict

from core.algorithms.utils import has_multiple_paths
from core.graphs.graph import AbstractGraph


def dfs(graph: AbstractGraph, origin: Union[str, int], target: Union[str, int] = None) -> Dict:
    """
    :param origin: name or id of origin node
    :param target: node to find path. If target is None all paths will be returned
    :return: shortest path to target or all possible paths to all nodes if target is not specified
    """
    if (target is not None) and (not graph[target]):
        raise Exception("There no target node in graph")
    queue = deque()
    queue.append(origin)
    visited = set()
    paths = {origin: [origin]}
    while queue:
        node = queue.pop()
        if node not in visited:
            visited.add(node)
            for child in graph.get_adj_nodes(node):
                queue.append(child.name)
                paths = graph._get_paths(child, node, paths)
    if target is not None:
        if has_multiple_paths(paths[target]):
            return {target: min(paths[target], key=lambda x: len(x))}
        else:
            return {target: paths[target]}
    return paths
