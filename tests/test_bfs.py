import pytest

from core.algorithms import bfs
from core.graphs import create_graph, GraphType
from tests.conftest import graph_1, graph_2


@pytest.mark.parametrize(
    "graph_type",
    [
        GraphType.AdjList,
    ],
)
def test_bfs_1(graph_type: GraphType):
    graph = create_graph(graph_type, oriented=True)
    graph = graph_1(graph)
    path = bfs(graph, 1, 10)
    assert path[10] == [1, 3, 6, 10]
    path = bfs(graph, 1, 8)
    assert path[8] == [1, 4, 8]


@pytest.mark.parametrize(
    "graph_type",
    [
        GraphType.AdjList,
    ],
)
def test_bfs_2(graph_type: GraphType):
    graph = create_graph(graph_type, oriented=True)
    graph = graph_2(graph)
    path = bfs(graph, 'S', 'F')
    assert path['F'] == ['S', 'D', 'F']
    path = bfs(graph, 'D', 'E')
    assert path['E'] == ['D', 'E']
    path = bfs(graph, 'S', 'C')
    assert path['C'] == ['S', 'B', 'C']
