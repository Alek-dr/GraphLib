import pytest

from core.algorithms import bfs
from core.graphs import GraphType, create_graph
from tests.conftest import graph_1, graph_2, graph_3_1


@pytest.mark.parametrize(
    "graph_type, directed, weighted",
    [
        [
            GraphType.AdjList, True, True
        ],
        [
            GraphType.AdjList, True, False
        ],
        [
            GraphType.AdjList, False, True
        ],
        [
            GraphType.AdjList, False, False
        ]
    ]
)
def test_bfs_1(graph_type: GraphType, directed, weighted):
    graph = create_graph(graph_type, directed=directed, weighted=weighted)
    graph = graph_1(graph)
    path = bfs(graph, 1, 10)
    assert path[10].vertexes == [1, 3, 6, 10]
    assert path[10].edges == ["b", "f", "h"]
    path = bfs(graph, 1, 8)
    assert path[8].vertexes == [1, 4, 8]
    assert path[8].edges == ["c", "i"]


@pytest.mark.parametrize(
    "graph_type, directed, weighted",
    [
        [
            GraphType.AdjList, True, True
        ],
        [
            GraphType.AdjList, True, False
        ],
        [
            GraphType.AdjList, False, True
        ],
        [
            GraphType.AdjList, False, False
        ]
    ]
)
def test_bfs_2(graph_type: GraphType, directed, weighted):
    graph = create_graph(graph_type, directed=directed, weighted=weighted)
    graph = graph_2(graph)
    path = bfs(graph, "S", "F")
    assert path["F"].vertexes == ["S", "D", "F"]
    assert path["F"].edges == ["b", "f"]
    path = bfs(graph, "S", "E")
    assert path["E"].vertexes == ["S", "B", "E"]
    assert path["E"].edges == ["a", "c"]
    path = bfs(graph, "S", "C")
    assert path["C"].vertexes == ["S", "B", "C"]
    assert path["C"].edges == ["a", "e"]


@pytest.mark.parametrize(
    "graph_type, directed, weighted",
    [
        [
            GraphType.AdjList, True, True
        ],
        [
            GraphType.AdjList, True, False
        ],
        [
            GraphType.AdjList, False, True
        ],
        [
            GraphType.AdjList, False, False
        ]
    ]
)
def test_bfs_3(graph_type: GraphType, directed, weighted):
    graph = create_graph(graph_type, directed=directed, weighted=weighted)
    graph = graph_3_1(graph)
    path = bfs(graph, "A")
    assert path["A"].vertexes == ["A"]
    assert path["B"].vertexes == ["A", "B"]
    assert path["C"].vertexes == ["A", "C"]
    assert path["D"].vertexes == ["A", "B", "D"]
    assert path["E"].vertexes == ["A", "C", "E"]
    assert path["F"].vertexes == ["A", "C", "E", "F"]
