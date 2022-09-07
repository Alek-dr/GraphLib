from collections import OrderedDict, deque
from typing import Dict, Union

from core.exceptions import VertexNotFound
from core.graphs.graph import AbstractGraph, edge
from core.graphs.walk import Walk


def bfs(
    graph: AbstractGraph, origin: Union[str, int], target: Union[str, int] = None
) -> Dict[Union[int, str], Walk]:
    """
    BFS algorithm
    :param graph: graph object
    :param origin: name or id of origin node
    :param target: node to find path. If target is None all paths will be returned
    :return: shortest path to target or all possible paths to all nodes if target is not specified
    """
    if (target is not None) and (not graph[target]):
        raise VertexNotFound(f"Cannot find vertex {target}")
    p = Walk(origin)
    if origin == target:
        return {origin: p}
    visited = set()
    visited.add(origin)
    queue = deque()
    e = edge(origin, origin, 0, None)
    queue.append(e)
    walks = OrderedDict()
    walk = Walk(origin)
    walk.add_step(e)
    walks[origin] = walk
    while queue:
        curr_edge = queue.pop()
        for e in graph.get_adj_edges(curr_edge.dst):
            if e.dst not in visited:
                path = Walk(e.dst)
                path.add_step(e)
                walks[e.dst] = walks[e.src] + path
                if (target is not None) and (walks.get(target)):
                    return {target: walks[target]}
                queue.appendleft(e)
                visited.add(e.dst)
    return walks
