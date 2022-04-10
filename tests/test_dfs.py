import pytest

from core.algorithms import dfs
from core.graphs import GraphType, create_graph
from tests.conftest import graph_1, graph_2


@pytest.mark.parametrize(
    "graph_type",
    [
        GraphType.AdjList,
    ],
)
def test_dfs_1(graph_type: GraphType):
    graph = create_graph(graph_type, directed=True)
    graph = graph_1(graph)
    path = dfs(graph, 1, 10)
    assert path[10] == [1, 3, 6, 10]
    path = dfs(graph, 1, 8)
    assert path[8] == [1, 4, 8]


@pytest.mark.parametrize(
    "graph_type",
    [
        GraphType.AdjList,
    ],
)
def test_dfs_2(graph_type: GraphType):
    graph = create_graph(graph_type, directed=True)
    graph = graph_2(graph)
    path = dfs(graph, "S", "F")
    assert path["F"] == ["S", "D", "F"]
    path = dfs(graph, "D", "E")
    assert path["E"] == ["D", "E"]
    path = dfs(graph, "S", "C")
    assert path["C"] == ["S", "B", "C"]
