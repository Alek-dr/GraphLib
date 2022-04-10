import pytest

from core.graphs import GraphType, create_graph
from tests.conftest import graph_1, graph_8, graph_8_2, graph_9


@pytest.mark.parametrize(
    "graph_type",
    [
        GraphType.AdjList,
    ],
)
def test_graph_1(graph_type):
    graph = create_graph(graph_type, directed=False, weighted=False)
    graph = graph_1(graph)
    assert graph.is_simple() == True


def test_graph_8():
    graph = graph_8()
    degrees = graph.deg()
    assert degrees == {1: 3, 2: 4, 3: 5, 4: 4}
    assert graph.is_simple() == False


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


def test_graph_9():
    graph = graph_9()
    degrees = graph.deg()
    assert degrees == {
        1: {"in_degree": 0, "out_degree": 1},
        2: {"in_degree": 1, "out_degree": 2},
        3: {"in_degree": 2, "out_degree": 0},
    }
    assert graph.is_simple() == False
