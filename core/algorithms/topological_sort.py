from collections import deque
from typing import List, Union

from core.graphs.graph import AbstractGraph


def _dfs(
    graph: AbstractGraph,
    src: Union[int, str],
    visited: set,
    sorted_v: List[Union[int, str]],
    i: int,
) -> [set, List[Union[int, str]], int]:
    if (src is not None) and (not graph[src]):
        raise Exception("There no target node in graph")
    stack = deque()
    stack.append(src)
    visited_at_iteration = deque()
    leafs = deque()
    while stack:
        curr_v = stack.pop()
        if curr_v not in visited:
            visited.add(curr_v)
            visited_at_iteration.append(curr_v)
            edges = [edge_ for edge_ in graph.get_adj_edges(curr_v)]
            if len(edges) == 0:
                leafs.append(curr_v)
            for edge_ in reversed(edges):
                if edge_.dst not in visited:
                    stack.append(edge_.dst)
            edges.clear()
    while leafs:
        v = leafs.pop()
        if v != src:
            sorted_v[i] = v
            i -= 1
    while visited_at_iteration:
        v = visited_at_iteration.pop()
        if v not in sorted_v and v != src:
            sorted_v[i] = v
            i -= 1
    return visited, sorted_v, i


def topological_sort(graph: AbstractGraph) -> List[Union[int, str]]:
    visited = set()
    sorted_v = [None for _ in range(len(graph.vertexes))]
    i = len(sorted_v) - 1
    for v in graph.vertexes:
        if v.name not in visited:
            visited, sorted_v, i = _dfs(graph, v.name, visited, sorted_v, i)
            sorted_v[i] = v.name
            i -= 1
    return sorted_v
