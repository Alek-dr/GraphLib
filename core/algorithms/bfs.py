from collections import OrderedDict, deque
from typing import Dict, Union

from core.exceptions import VertexNotFound
from core.graphs.graph import AbstractGraph, edge
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
    if origin == target:
        return {origin: p}
    visited = set()
    visited.add(origin)
    queue = deque()
    e = edge(origin, origin, 0, None)
    queue.append(e)
    paths = OrderedDict()
    path = Path(origin)
    path.add_step(e)
    paths[origin] = path
    while queue:
        curr_edge = queue.pop()
        for edge_ in graph.get_adj_edges(curr_edge.dst):
            if edge_.dst not in visited:
                path = Path(edge_.dst)
                path.add_step(edge_)
                paths[edge_.dst] = paths[edge_.src] + path
                if (target is not None) and (paths.get(target)):
                    return {target: paths[target]}
                queue.appendleft(edge_)
                visited.add(edge_.dst)
    return paths
