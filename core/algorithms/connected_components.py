from collections import deque
from typing import Generator, Set, Union

from core.graphs.graph import AbstractGraph, edge


def _dfs(
    graph: AbstractGraph,
    origin: Union[str, int],
    target: Union[str, int] = None,
):
    if (target is not None) and (not graph[target]):
        raise Exception("There no target node in graph")
    if origin == target:
        return {origin}
    stack = deque()
    stack.append(edge(origin, origin, 0, None))
    visited = set()
    while stack:
        curr_edge = stack.pop()
        if curr_edge.dst not in visited:
            visited.add(curr_edge.dst)
            edges = [e for e in graph.get_adj_edges(curr_edge.dst)]
            for e in reversed(edges):
                if e.dst not in visited:
                    stack.append(e)
                    if target is not None:
                        return visited
            edges.clear()
    return visited


def connected_components(
    graph: AbstractGraph,
) -> Generator[Set[Union[str, int]], None, None]:
    """
    Return set of connected components
    """
    visited = set()
    for v in graph.vertexes:
        if v.name not in visited:
            connected = _dfs(graph, v.name)
            for vertex in connected:
                visited.add(vertex)
            yield connected
