from typing import Callable

import pytest
import networkx as nx
from networkx.exception import NetworkXError

from core.exceptions import GraphTypeException
from core.graphs import GraphType, create_graph
from tests.conftest import (
    graph_1,
    graph_8,
    graph_8_2,
    graph_9,
    graph_2,
    graph_3_1,
    graph_3_2,
    graph_4_1,
    graph_4_2,
    graph_5,
    graph_6,
    graph_7,
    create_nxgraph,
    graph_10,
    graph_11,
    graph_12,
)

# region Check vertex degree


def check_degree_sum(graph):
    degrees = graph.deg()
    E = 0
    for _ in graph.get_edges():
        E += 1
    deg_sum = 0
    if graph.directed:
        for d in degrees.values():
            deg_sum += d["in_degree"] + d["out_degree"]
    else:
        deg_sum = sum(degrees.values())
    assert deg_sum == 2 * E


@pytest.mark.parametrize(
    "graph_type, directed, weighted",
    [
        [GraphType.AdjList, True, True],
        [GraphType.AdjList, True, False],
        [GraphType.AdjList, False, True],
        [GraphType.AdjList, False, False],
    ],
)
def test_graph_1(graph_type: GraphType, directed, weighted):
    graph = create_graph(graph_type, directed=directed, weighted=weighted)
    graph = graph_1(graph)
    simple = not (directed or weighted)
    assert graph.is_simple() == simple
    check_degree_sum(graph)


def test_graph_8():
    graph = graph_8()
    degrees = graph.deg()
    assert degrees == {1: 3, 2: 4, 3: 5, 4: 4}
    assert graph.is_simple() == False
    check_degree_sum(graph)


def test_graph_8_2():
    graph = graph_8_2()
    degrees = graph.deg()
    assert degrees == {
        1: {"in_degree": 0, "out_degree": 3},
        2: {"in_degree": 2, "out_degree": 2},
        3: {"in_degree": 2, "out_degree": 3},
        4: {"in_degree": 4, "out_degree": 0},
    }
    assert graph.is_simple() == False
    check_degree_sum(graph)


def test_graph_9():
    graph = graph_9()
    degrees = graph.deg()
    assert degrees == {
        1: {"in_degree": 0, "out_degree": 1},
        2: {"in_degree": 1, "out_degree": 2},
        3: {"in_degree": 2, "out_degree": 0},
    }
    assert graph.is_simple() == False
    check_degree_sum(graph)


# endregion

# region Check undirected graph properties: connected, diameter, eulerian


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
def test_not_directed_graph_1(
    f_graph: Callable, graph_type: GraphType, directed: bool, weighted: bool
):
    graph = create_graph(graph_type, directed=directed, weighted=weighted)
    graph = f_graph(graph)
    nx_graph = create_nxgraph(graph)
    assert graph.is_eulerian() == nx.is_eulerian(nx_graph)
    assert nx.is_connected(nx_graph) == graph.is_connected()
    try:
        nx.diameter(nx_graph)
    except NetworkXError:
        with pytest.raises(GraphTypeException):
            graph.diameter()
    else:
        assert nx.diameter(nx_graph) == graph.diameter()


@pytest.mark.parametrize(
    "f_graph",
    [graph_8, graph_8_2, graph_9, graph_10, graph_11, graph_12],
)
def test_not_directed_graph_2(f_graph: Callable):
    graph = f_graph()
    if not graph.is_directed:
        nx_graph = create_nxgraph(graph)
        assert nx.is_connected(nx_graph) == graph.is_connected()
        assert graph.is_eulerian() == nx.is_eulerian(nx_graph)
        try:
            nx.diameter(nx_graph)
        except NetworkXError:
            with pytest.raises(GraphTypeException):
                graph.diameter()
        else:
            assert nx.diameter(nx_graph) == graph.diameter()


# endregion


def plot_nx():
    import matplotlib.pyplot as plt
    import matplotlib

    matplotlib.use("tkagg")
    graph = graph_8()
    nx_graph = create_nxgraph(graph)
    conn = nx.is_connected(nx_graph)
    nx.draw(nx_graph, with_labels=True, font_weight="bold")
    plt.show()


if __name__ == "__main__":
    g = graph_8()
    nx_graph = create_nxgraph(g)
    dnx = nx.diameter(nx_graph)
    print(dnx)
    d = g.diameter()
    print(d)
