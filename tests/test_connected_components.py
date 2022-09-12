from typing import Callable

import networkx as nx
import pytest

from core.algorithms.connected_components import connected_components
from core.graphs import GraphType, create_graph
from core.graphs.graph import AbstractGraph
from tests.conftest import (
    create_nxgraph,
    graph_1,
    graph_2,
    graph_3_1,
    graph_3_2,
    graph_4_1,
    graph_4_2,
    graph_5,
    graph_6,
    graph_7,
    graph_8,
    graph_12,
)


def get_components(graph: AbstractGraph):
    nx_graph = create_nxgraph(graph)
    conn_comp = nx.connected_components(nx_graph)
    nx_components = set()
    for cc in conn_comp:
        nx_components.add(frozenset(cc))

    components = set()
    for cc in connected_components(graph):
        components.add((frozenset(cc)))
    return nx_components, components


def test_conn_components_8():
    graph = graph_8()
    nx_components, components = get_components(graph)
    assert nx_components == components


def test_conn_components_12():
    graph = graph_12()
    nx_components, components = get_components(graph)
    assert nx_components == components


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
def test_connected_components(
    f_graph: Callable, graph_type: GraphType, directed: bool, weighted: bool
):
    graph = create_graph(graph_type, directed=directed, weighted=weighted)
    graph = f_graph(graph)
    nx_components, components = get_components(graph)
    assert nx_components == components
