from collections import deque
from typing import Dict, Union

from core.algorithms.utils import has_multiple_paths
from core.graphs.graph import AbstractGraph


def bfs(
    graph: AbstractGraph, origin: Union[str, int], target: Union[str, int] = None
) -> Dict:
    """
    :param origin: name or id of origin node
    :param target: node to find path. If target is None all paths will be returned
    :return: shortest path to target or all possible paths to all nodes if target is not specified
    """
    if (target is not None) and (not graph[target]):
        raise Exception("There no target node in graph")
    visited = set()
    visited.add(origin)
    queue = deque()
    queue.append(origin)
    paths = {origin: [origin]}
    while queue:
        node = queue.pop()
        for child in graph.get_adj_nodes(node):
            paths = graph._get_paths(child, node, paths)
            if (target is not None) and (child.name == target):
                if has_multiple_paths(paths[target]):
                    return {target: min(paths[target], key=lambda x: len(x))}
                else:
                    return {target: paths[target]}
            visited.add(child.name)
            queue.appendleft(child.name)
    return paths
