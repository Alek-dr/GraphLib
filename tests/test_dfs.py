import pytest

from core.algorithms import dfs
from core.graphs import GraphType, create_graph
from tests.conftest import graph_1, graph_2


@pytest.mark.parametrize(
    "graph_type, directed, weighted",
    [[GraphType.AdjList, True, True], [GraphType.AdjList, True, False]],
)
def test_dfs_1(graph_type: GraphType, directed, weighted):
    graph = create_graph(graph_type, directed=directed, weighted=weighted)
    graph = graph_1(graph)
    path = dfs(graph, 1, 10)
    assert path[10].vertexes == [1, 3, 6, 10]
    path = dfs(graph, 1, 8)
    assert path[8].vertexes == [1, 4, 8]


@pytest.mark.parametrize(
    "graph_type, directed, weighted",
    [[GraphType.AdjList, True, True], [GraphType.AdjList, True, False]],
)
def test_dfs_2(graph_type: GraphType, directed, weighted):
    graph = create_graph(graph_type, directed=directed, weighted=weighted)
    graph = graph_2(graph)
    path = dfs(graph, "S", "F")
    assert path["F"].vertexes == ["S", "B", "C", "F"]
    path = dfs(graph, "S", "E")
    assert path["E"].vertexes == ["S", "B", "E"]
    path = dfs(graph, "D", "E")
    assert path["E"].vertexes == ["D", "E"]
