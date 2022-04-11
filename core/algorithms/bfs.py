from collections import deque
from typing import Dict, Union, List

from core.algorithms.utils import has_multiple_paths
from core.exceptions import VertexNotFound
from core.graphs.graph import AbstractGraph
from core.graphs.path import Path


def bfs(
        graph: AbstractGraph, origin: Union[str, int], target: Union[str, int] = None
) -> Dict[Union[int, str], Path]:
    """
    :param origin: name or id of origin node
    :param target: node to find path. If target is None all paths will be returned
    :return: shortest path to target or all possible paths to all nodes if target is not specified
    """
    if (target is not None) and (not graph[target]):
        raise VertexNotFound(f"Cannot find vertex {target}")
    p = Path(origin)
    p.add_step(origin, None, 0)
    if origin == target:
        return {origin: p}
    visited = set()
    visited.add(origin)
    queue = deque()
    queue.append(origin)
    paths = {origin: p}
    while queue:
        node = queue.pop()
        for edge_ in graph.get_adj_nodes(node):
            if edge_.dst not in visited:
                p = Path(edge_.dst)
                p.add_step(edge_.src, edge_.name, edge_.weight)
                paths[edge_.dst] = paths[node] + p
                if (target is not None) and (edge_.dst == target):
                    return {target: paths[target]}
                visited.add(edge_.dst)
                queue.appendleft(edge_.dst)
    return paths
