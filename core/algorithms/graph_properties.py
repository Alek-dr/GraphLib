from collections import deque
from typing import Generator, Set, Union, Tuple

from core.algorithms import bellman_ford
from core.exceptions import GraphTypeException
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
    visited_ = set()
    while stack:
        curr_edge = stack.pop()
        if curr_edge.dst not in visited_:
            visited_.add(curr_edge.dst)
            edges = [e for e in graph.get_adj_edges(curr_edge.dst)]
            for e in reversed(edges):
                if e.dst not in visited_:
                    stack.append(e)
                    if target is not None:
                        return visited_
            edges.clear()
    return visited_


def _bfs(
    graph: AbstractGraph,
    origin: Union[str, int],
):
    edge_counter = 0
    visited_ = set()
    visited_.add(origin)
    queue = deque()
    e = edge(origin, origin, 0, None)
    signal_edge = edge(-1, -1, 0, None)
    queue.append(e)
    queue.appendleft(signal_edge)
    while len(queue) != 1:
        curr_edge = queue.pop()
        if curr_edge == signal_edge:
            edge_counter += 1
            queue.appendleft(signal_edge)
            continue
        for e in graph.get_adj_edges(curr_edge.dst):
            if e.dst not in visited_:
                queue.appendleft(e)
                visited_.add(e.dst)
    return edge_counter


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


def is_connected(graph: AbstractGraph) -> bool:
    """
    True if graph is connected
    """
    # TODO: check graph is simple
    components = []
    for cc in connected_components(graph):
        components.append(cc)
    if len(components) == 1:
        if len(components[0]) == graph.n_vertex:
            return True
    return False


def is_eulerian(graph: AbstractGraph) -> bool:
    if graph.is_directed:
        raise Exception("Not implemented for directed graph")
    else:
        if is_connected(graph):
            for d in graph.deg().values():
                if d // 2 != 0:
                    return False
            return True
        else:
            return False


def diameter(graph: AbstractGraph) -> int:
    """
    Returns the diameter of connceted graph
    """
    if graph.is_directed:
        raise Exception("Not implemented for directed graph")
    if is_connected(graph):
        diameter = 0
        for v in graph.vertexes:
            d = _bfs(graph, v.name)
            if d > diameter:
                diameter = d
        return diameter
    else:
        raise GraphTypeException(
            "Cannot calculate diameter for not connected graph"
        )


def _get_radius(matrix):
    max_ = set()
    for row in matrix:
        max_.add(max(row))
    return min(max_)


def _get_centers(v_names, matrix, r):
    c = set()
    for i, row in enumerate(matrix):
        if max(row) <= r:
            c.add(v_names[i])
    return c


def radius(graph: AbstractGraph) -> Tuple[int, Set[Union[int, str]]]:
    """
    Returns the radius of connceted graph
    """
    if not is_connected(graph):
        raise GraphTypeException(
            "Cannot calculate radius for not connected graph"
        )
    dist_matrix = []
    v_names = sorted([v.name for v in graph.vertexes])
    for v in v_names:
        walks, _ = bellman_ford(graph, v, use_weights=False)
        row = []
        for name in v_names:
            length = walks.get(name).length()
            row.append(length)
        dist_matrix.append(row)
    r = _get_radius(dist_matrix)
    centers = _get_centers(v_names, dist_matrix, r)
    return r, centers
