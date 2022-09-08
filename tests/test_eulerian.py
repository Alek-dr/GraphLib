from typing import Callable

import networkx as nx
import pytest

from core.graphs import GraphType, create_graph
from tests.conftest import (create_nxgraph, graph_1, graph_2, graph_3_1,
                            graph_3_2, graph_4_1, graph_4_2, graph_5, graph_6,
                            graph_7, graph_8, graph_12, graph_8_2, graph_9, graph_10, graph_11)


@pytest.mark.parametrize(
    "f_graph, graph_type, directed, weighted",
    [
        [graph_1, GraphType.AdjList, False, False],
        [graph_1, GraphType.AdjList, False, True],
        [graph_2, GraphType.AdjList, False, False],
        [graph_2, GraphType.AdjList, False, False],
        [graph_3_1, GraphType.AdjList, False, False],
        [graph_3_1, GraphType.AdjList, False, True],
        [graph_3_2, GraphType.AdjList, False, False],
        [graph_4_1, GraphType.AdjList, False, False],
        [graph_4_2, GraphType.AdjList, False, False],
        [graph_4_2, GraphType.AdjList, False, True],
        [graph_5, GraphType.AdjList, False, False],
        [graph_6, GraphType.AdjList, False, False],
        [graph_7, GraphType.AdjList, False, False],
    ],
)
def test_is_eulerian_1(
        f_graph: Callable, graph_type: GraphType, directed: bool, weighted: bool
):
    graph = create_graph(graph_type, directed=directed, weighted=weighted)
    graph = f_graph(graph)
    nx_graph = create_nxgraph(graph)
    assert graph.is_eulerian() == nx.is_eulerian(nx_graph)


@pytest.mark.parametrize(
    "f_graph",
    [
        graph_8, graph_8_2, graph_9, graph_10, graph_11, graph_12
    ],
)
def test_is_eulerian_2(
        f_graph: Callable
):
    graph = f_graph()
    if not graph.is_directed:
        nx_graph = create_nxgraph(graph)
        assert graph.is_eulerian() == nx.is_eulerian(nx_graph)

if __name__ == '__main__':
    g = graph_12()
    nx_graph = create_nxgraph(g)
    e = nx.is_eulerian(nx_graph)
    p = g.is_eulerian()
    print(e)