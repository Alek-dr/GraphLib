import pytest

from core.algorithms import bellman_ford
from core.graphs import GraphType, create_graph
from tests.conftest import (
    graph_3_1,
    graph_3_2,
    graph_4_1,
    graph_4_2,
    graph_5,
    graph_6,
    graph_7,
    graph_11,
)


@pytest.mark.parametrize(
    "graph_type",
    [
        GraphType.AdjList,
    ],
)
def test_bellman_ford_3_1(graph_type: GraphType):
    graph = create_graph(graph_type, directed=True, weighted=True)
    graph = graph_3_1(graph)
    paths, ncc = bellman_ford(graph, "A")
    assert ncc
    assert paths["A"].vertexes == ["A"]
    assert paths["A"].path_weight == 0
    assert paths["B"].vertexes == ["A", "B"]
    assert paths["B"].path_weight == 5
    assert paths["C"].vertexes == ["A", "C"]
    assert paths["C"].path_weight == 2
    assert paths["D"].vertexes == ["A", "B", "D"]
    assert paths["D"].path_weight == 9
    assert paths["E"].vertexes == ["A", "B", "E"]
    assert paths["E"].path_weight == 7
    assert paths["F"].vertexes == ["A", "B", "E", "F"]
    assert paths["F"].path_weight == 8

    paths, ncc = bellman_ford(graph, "B")
    assert ncc
    assert len(paths["A"].vertexes) == 0
    assert paths["A"].path_weight == float("inf")
    assert paths["B"].vertexes == ["B"]
    assert paths["B"].path_weight == 0
    assert len(paths["C"].vertexes) == 0
    assert paths["C"].path_weight == float("inf")
    assert paths["D"].vertexes == ["B", "D"]
    assert paths["D"].path_weight == 4
    assert paths["E"].vertexes == ["B", "E"]
    assert paths["E"].path_weight == 2
    assert paths["F"].vertexes == ["B", "E", "F"]
    assert paths["F"].path_weight == 3

    paths, ncc = bellman_ford(graph, "C")
    assert ncc
    assert len(paths["A"].vertexes) == 0
    assert paths["A"].path_weight == float("inf")
    assert paths["B"].vertexes == ["C", "B"]
    assert paths["B"].path_weight == 8
    assert paths["C"].vertexes == ["C"]
    assert paths["C"].path_weight == 0
    assert paths["D"].vertexes == ["C", "B", "D"]
    assert paths["D"].path_weight == 12
    assert paths["E"].vertexes == ["C", "E"]
    assert paths["E"].path_weight == 7
    assert paths["F"].vertexes == ["C", "E", "F"]
    assert paths["F"].path_weight == 8

    paths, ncc = bellman_ford(graph, "D")
    assert ncc
    assert len(paths["A"].vertexes) == 0
    assert paths["A"].path_weight == float("inf")
    assert len(paths["B"].vertexes) == 0
    assert paths["B"].path_weight == float("inf")
    assert len(paths["C"].vertexes) == 0
    assert paths["C"].path_weight == float("inf")
    assert paths["D"].vertexes == ["D"]
    assert paths["D"].path_weight == 0
    assert paths["E"].vertexes == ["D", "E"]
    assert paths["E"].path_weight == 6
    assert paths["F"].vertexes == ["D", "F"]
    assert paths["F"].path_weight == 3

    paths, ncc = bellman_ford(graph, "E")
    assert ncc
    assert len(paths["A"].vertexes) == 0
    assert paths["A"].path_weight == float("inf")
    assert len(paths["B"].vertexes) == 0
    assert paths["B"].path_weight == float("inf")
    assert len(paths["C"].vertexes) == 0
    assert paths["C"].path_weight == float("inf")
    assert len(paths["D"].vertexes) == 0
    assert paths["D"].path_weight == float("inf")
    assert paths["E"].vertexes == ["E"]
    assert paths["E"].path_weight == 0
    assert paths["F"].vertexes == ["E", "F"]
    assert paths["F"].path_weight == 1

    paths, ncc = bellman_ford(graph, "F")
    assert ncc
    assert len(paths["A"].vertexes) == 0
    assert paths["A"].path_weight == float("inf")
    assert len(paths["B"].vertexes) == 0
    assert paths["B"].path_weight == float("inf")
    assert len(paths["C"].vertexes) == 0
    assert paths["C"].path_weight == float("inf")
    assert len(paths["D"].vertexes) == 0
    assert paths["D"].path_weight == float("inf")
    assert len(paths["E"].vertexes) == 0
    assert paths["E"].path_weight == float("inf")
    assert paths["F"].vertexes == ["F"]
    assert paths["F"].path_weight == 0


@pytest.mark.parametrize(
    "graph_type",
    [
        GraphType.AdjList,
    ],
)
def test_bellman_ford_3_2(graph_type: GraphType):
    graph = create_graph(graph_type, directed=True, weighted=True)
    graph = graph_3_2(graph)
    paths, ncc = bellman_ford(graph, "A")
    assert ncc
    assert paths["A"].vertexes == ["A"]
    assert paths["A"].path_weight == 0
    assert paths["B"].vertexes == ["A", "B"]
    assert paths["B"].path_weight == 5
    assert paths["C"].vertexes == ["A", "C"]
    assert paths["C"].path_weight == 2
    assert len(paths["D"].vertexes) == 0
    assert paths["D"].path_weight == float("inf")
    assert paths["E"].vertexes == ["A", "B", "E"]
    assert paths["E"].path_weight == 7
    assert paths["F"].vertexes == ["A", "B", "E", "F"]
    assert paths["F"].path_weight == 8

    paths, ncc = bellman_ford(graph, "B")
    assert ncc
    assert len(paths["A"].vertexes) == 0
    assert paths["A"].path_weight == float("inf")
    assert paths["B"].vertexes == ["B"]
    assert paths["B"].path_weight == 0
    assert len(paths["C"].vertexes) == 0
    assert paths["C"].path_weight == float("inf")
    assert len(paths["D"].vertexes) == 0
    assert paths["D"].path_weight == float("inf")
    assert paths["E"].vertexes == ["B", "E"]
    assert paths["E"].path_weight == 2
    assert paths["F"].vertexes == ["B", "E", "F"]
    assert paths["F"].path_weight == 3

    paths, ncc = bellman_ford(graph, "C")
    assert ncc
    assert len(paths["A"].vertexes) == 0
    assert paths["A"].path_weight == float("inf")
    assert paths["B"].vertexes == ["C", "B"]
    assert paths["B"].path_weight == 8
    assert paths["C"].vertexes == ["C"]
    assert paths["C"].path_weight == 0
    assert len(paths["D"].vertexes) == 0
    assert paths["D"].path_weight == float("inf")
    assert paths["E"].vertexes == ["C", "E"]
    assert paths["E"].path_weight == 7
    assert paths["F"].vertexes == ["C", "E", "F"]
    assert paths["F"].path_weight == 8

    paths, ncc = bellman_ford(graph, "D")
    assert ncc
    assert len(paths["A"].vertexes) == 0
    assert paths["A"].path_weight == float("inf")
    assert paths["B"].vertexes == ["D", "B"]
    assert paths["B"].path_weight == 4
    assert len(paths["C"].vertexes) == 0
    assert paths["C"].path_weight == float("inf")
    assert paths["D"].vertexes == ["D"]
    assert paths["D"].path_weight == 0
    assert paths["E"].vertexes == ["D", "E"]
    assert paths["E"].path_weight == 6
    assert paths["F"].vertexes == ["D", "F"]
    assert paths["F"].path_weight == 3

    paths, ncc = bellman_ford(graph, "E")
    assert ncc
    assert len(paths["A"].vertexes) == 0
    assert paths["A"].path_weight == float("inf")
    assert len(paths["B"].vertexes) == 0
    assert paths["B"].path_weight == float("inf")
    assert len(paths["C"].vertexes) == 0
    assert paths["C"].path_weight == float("inf")
    assert len(paths["D"].vertexes) == 0
    assert paths["D"].path_weight == float("inf")
    assert paths["E"].vertexes == ["E"]
    assert paths["E"].path_weight == 0
    assert paths["F"].vertexes == ["E", "F"]
    assert paths["F"].path_weight == 1

    paths, ncc = bellman_ford(graph, "F")
    assert ncc
    assert len(paths["A"].vertexes) == 0
    assert paths["A"].path_weight == float("inf")
    assert len(paths["B"].vertexes) == 0
    assert paths["B"].path_weight == float("inf")
    assert len(paths["C"].vertexes) == 0
    assert paths["C"].path_weight == float("inf")
    assert len(paths["D"].vertexes) == 0
    assert paths["D"].path_weight == float("inf")
    assert len(paths["E"].vertexes) == 0
    assert paths["E"].path_weight == float("inf")
    assert paths["F"].vertexes == ["F"]
    assert paths["F"].path_weight == 0


@pytest.mark.parametrize(
    "graph_type",
    [
        GraphType.AdjList,
    ],
)
def test_bellman_ford_4_1(graph_type: GraphType):
    graph = create_graph(graph_type, directed=True, weighted=True)
    graph = graph_4_1(graph)
    paths, ncc = bellman_ford(graph, "A")
    assert ncc
    assert paths["A"].vertexes == ["A"]
    assert paths["A"].path_weight == 0
    assert paths["B"].vertexes == ["A", "B"]
    assert paths["B"].path_weight == 10
    assert paths["C"].vertexes == ["A", "B", "C"]
    assert paths["C"].path_weight == 30
    assert paths["D"].vertexes == ["A", "B", "C", "D"]
    assert paths["D"].path_weight == 31
    assert paths["E"].vertexes == ["A", "B", "C", "E"]
    assert paths["E"].path_weight == 60

    paths, ncc = bellman_ford(graph, "B")
    assert ncc
    assert len(paths["A"].vertexes) == 0
    assert paths["A"].path_weight == float("inf")
    assert paths["B"].vertexes == ["B"]
    assert paths["B"].path_weight == 0
    assert paths["C"].vertexes == ["B", "C"]
    assert paths["C"].path_weight == 20
    assert paths["D"].vertexes == ["B", "C", "D"]
    assert paths["D"].path_weight == 21
    assert paths["E"].vertexes == ["B", "C", "E"]
    assert paths["E"].path_weight == 50

    paths, ncc = bellman_ford(graph, "C")
    assert ncc
    assert len(paths["A"].vertexes) == 0
    assert paths["A"].path_weight == float("inf")
    assert paths["B"].vertexes == ["C", "D", "B"]
    assert paths["B"].path_weight == 2
    assert paths["C"].vertexes == ["C"]
    assert paths["C"].path_weight == 0
    assert paths["D"].vertexes == ["C", "D"]
    assert paths["D"].path_weight == 1
    assert paths["E"].vertexes == ["C", "E"]
    assert paths["E"].path_weight == 30

    paths, ncc = bellman_ford(graph, "D")
    assert ncc
    assert len(paths["A"].vertexes) == 0
    assert paths["A"].path_weight == float("inf")
    assert paths["B"].vertexes == ["D", "B"]
    assert paths["B"].path_weight == 1
    assert paths["C"].vertexes == ["D", "B", "C"]
    assert paths["C"].path_weight == 21
    assert paths["D"].vertexes == ["D"]
    assert paths["D"].path_weight == 0
    assert paths["E"].vertexes == ["D", "B", "C", "E"]
    assert paths["E"].path_weight == 51

    paths, ncc = bellman_ford(graph, "E")
    assert ncc
    assert len(paths["A"].vertexes) == 0
    assert paths["A"].path_weight == float("inf")
    assert len(paths["B"].vertexes) == 0
    assert paths["B"].path_weight == float("inf")
    assert len(paths["C"].vertexes) == 0
    assert paths["C"].path_weight == float("inf")
    assert len(paths["D"].vertexes) == 0
    assert paths["D"].path_weight == float("inf")
    assert paths["E"].vertexes == ["E"]
    assert paths["E"].path_weight == 0


@pytest.mark.parametrize(
    "graph_type",
    [
        GraphType.AdjList,
    ],
)
def test_bellman_ford_4_2(graph_type: GraphType):
    graph = create_graph(graph_type, directed=True, weighted=True)
    graph = graph_4_2(graph)
    paths, ncc = bellman_ford(graph, "A")
    assert ncc
    assert paths["A"].vertexes == ["A"]
    assert paths["A"].path_weight == 0
    assert paths["B"].vertexes == ["A", "B"]
    assert paths["B"].path_weight == 10
    assert paths["C"].vertexes == ["A", "B", "C"]
    assert paths["C"].path_weight == 30
    assert paths["D"].vertexes == ["A", "B", "C", "D"]
    assert paths["D"].path_weight == 31
    assert paths["E"].vertexes == ["A", "B", "C", "D", "F", "E"]
    assert paths["E"].path_weight == 38
    assert paths["F"].vertexes == ["A", "B", "C", "D", "F"]
    assert paths["F"].path_weight == 33

    paths, ncc = bellman_ford(graph, "B")
    assert ncc
    assert len(paths["A"].vertexes) == 0
    assert paths["A"].path_weight == float("inf")
    assert paths["B"].vertexes == ["B"]
    assert paths["B"].path_weight == 0
    assert paths["C"].vertexes == ["B", "C"]
    assert paths["C"].path_weight == 20
    assert paths["D"].vertexes == ["B", "C", "D"]
    assert paths["D"].path_weight == 21
    assert paths["E"].vertexes == ["B", "C", "D", "F", "E"]
    assert paths["E"].path_weight == 28
    assert paths["F"].vertexes == ["B", "C", "D", "F"]
    assert paths["F"].path_weight == 23

    paths, ncc = bellman_ford(graph, "C")
    assert ncc
    assert len(paths["A"].vertexes) == 0
    assert paths["A"].path_weight == float("inf")
    assert paths["B"].vertexes == ["C", "D", "B"]
    assert paths["B"].path_weight == 2
    assert paths["C"].vertexes == ["C"]
    assert paths["C"].path_weight == 0
    assert paths["D"].vertexes == ["C", "D"]
    assert paths["D"].path_weight == 1
    assert paths["E"].vertexes == ["C", "D", "F", "E"]
    assert paths["E"].path_weight == 8
    assert paths["F"].vertexes == ["C", "D", "F"]
    assert paths["F"].path_weight == 3

    paths, ncc = bellman_ford(graph, "D")
    assert ncc
    assert len(paths["A"].vertexes) == 0
    assert paths["A"].path_weight == float("inf")
    assert paths["B"].vertexes == ["D", "B"]
    assert paths["B"].path_weight == 1
    assert paths["C"].vertexes == ["D", "B", "C"]
    assert paths["C"].path_weight == 21
    assert paths["D"].vertexes == ["D"]
    assert paths["D"].path_weight == 0
    assert paths["E"].vertexes == ["D", "F", "E"]
    assert paths["E"].path_weight == 7
    assert paths["F"].vertexes == ["D", "F"]
    assert paths["F"].path_weight == 2

    paths, ncc = bellman_ford(graph, "E")
    assert ncc
    assert len(paths["A"].vertexes) == 0
    assert paths["A"].path_weight == float("inf")
    assert len(paths["B"].vertexes) == 0
    assert paths["B"].path_weight == float("inf")
    assert len(paths["C"].vertexes) == 0
    assert paths["C"].path_weight == float("inf")
    assert len(paths["D"].vertexes) == 0
    assert paths["D"].path_weight == float("inf")
    assert paths["E"].vertexes == ["E"]
    assert paths["E"].path_weight == 0
    assert len(paths["F"].vertexes) == 0
    assert paths["F"].path_weight == float("inf")

    paths, ncc = bellman_ford(graph, "F")
    assert ncc
    assert len(paths["A"].vertexes) == 0
    assert paths["A"].path_weight == float("inf")
    assert paths["B"].vertexes == ["F", "D", "B"]
    assert paths["B"].path_weight == 3
    assert paths["C"].vertexes == ["F", "D", "B", "C"]
    assert paths["C"].path_weight == 23
    assert paths["D"].vertexes == ["F", "D"]
    assert paths["D"].path_weight == 2
    assert paths["E"].vertexes == ["F", "E"]
    assert paths["E"].path_weight == 5
    assert paths["F"].vertexes == ["F"]
    assert paths["F"].path_weight == 0


@pytest.mark.parametrize(
    "graph_type",
    [
        GraphType.AdjList,
    ],
)
def test_bellman_ford_5(graph_type: GraphType):
    graph = create_graph(graph_type, directed=True, weighted=True)
    graph = graph_5(graph)
    paths, ncc = bellman_ford(graph, "A")
    assert ncc

    assert paths["A"].vertexes == ["A"]
    assert paths["A"].path_weight == 0
    assert paths["B"].vertexes == ["A", "B"]
    assert paths["B"].path_weight == 2
    assert paths["C"].vertexes == ["A", "C"]
    assert paths["C"].path_weight == 1
    assert paths["D"].vertexes == ["A", "D"]
    assert paths["D"].path_weight == 3

    paths, ncc = bellman_ford(graph, "B")
    assert ncc
    assert paths["A"].vertexes == ["B", "C", "A"]
    assert paths["A"].path_weight == 5
    assert paths["B"].vertexes == ["B"]
    assert paths["B"].path_weight == 0
    assert paths["C"].vertexes == ["B", "C"]
    assert paths["C"].path_weight == 4
    assert paths["D"].vertexes == ["B", "C", "A", "D"]
    assert paths["D"].path_weight == 8

    paths, ncc = bellman_ford(graph, "C")
    assert ncc
    assert paths["A"].vertexes == ["C", "A"]
    assert paths["A"].path_weight == 1
    assert paths["B"].vertexes == ["C", "A", "B"]
    assert paths["B"].path_weight == 3
    assert paths["C"].vertexes == ["C"]
    assert paths["C"].path_weight == 0
    assert paths["D"].vertexes == ["C", "A", "D"]
    assert paths["D"].path_weight == 4

    paths, ncc = bellman_ford(graph, "D")
    assert ncc
    assert len(paths["A"].vertexes) == 0
    assert paths["A"].path_weight == float("inf")
    assert len(paths["B"].vertexes) == 0
    assert paths["B"].path_weight == float("inf")
    assert len(paths["C"].vertexes) == 0
    assert paths["C"].path_weight == float("inf")
    assert paths["D"].vertexes == ["D"]
    assert paths["D"].path_weight == 0


@pytest.mark.parametrize(
    "graph_type",
    [
        GraphType.AdjList,
    ],
)
def test_bellman_ford_6(graph_type: GraphType):
    graph = create_graph(graph_type, directed=True, weighted=True)
    graph = graph_6(graph)
    paths, ncc = bellman_ford(graph, "A")
    assert ncc
    assert paths["A"].vertexes == ["A"]
    assert paths["A"].path_weight == 0
    assert paths["B"].vertexes == ["A", "B"]
    assert paths["B"].path_weight == 2
    assert paths["C"].vertexes == ["A", "B", "C"]
    assert paths["C"].path_weight == 4

    paths, ncc = bellman_ford(graph, "B")
    assert ncc
    assert len(paths["A"].vertexes) == 0
    assert paths["A"].path_weight == float("inf")
    assert paths["B"].vertexes == ["B"]
    assert paths["B"].path_weight == 0
    assert paths["C"].vertexes == ["B", "C"]
    assert paths["C"].path_weight == 2

    paths, ncc = bellman_ford(graph, "C")
    assert ncc
    assert len(paths["A"].vertexes) == 0
    assert paths["A"].path_weight == float("inf")
    assert len(paths["B"].vertexes) == 0
    assert paths["B"].path_weight == float("inf")
    assert paths["C"].vertexes == ["C"]
    assert paths["C"].path_weight == 0


@pytest.mark.parametrize(
    "graph_type, directed, weighted",
    [
        [GraphType.AdjList, True, True],
        [GraphType.AdjList, True, False],
        [GraphType.AdjList, False, True],
        [GraphType.AdjList, False, False],
    ],
)
def test_bellman_ford_7(graph_type: GraphType, directed, weighted):
    graph = create_graph(graph_type, directed=directed, weighted=weighted)
    graph = graph_7(graph)
    paths, ncc = bellman_ford(graph, "Cab")
    assert ncc
    assert paths["Cab"].vertexes == ["Cab"]
    assert paths["Cab"].path_weight == 0
    assert paths["Car"].vertexes == ["Cab", "Car"]
    assert paths["Car"].path_weight == 1
    assert paths["Cat"].vertexes == ["Cab", "Cat"]
    assert paths["Cat"].path_weight == 1
    assert paths["Bar"].vertexes == ["Cab", "Car", "Bar"]
    assert paths["Bar"].path_weight == 2
    assert paths["Bat"].vertexes == ["Cab", "Cat", "Bat"]
    assert paths["Bat"].path_weight == 2
    assert paths["Mat"].vertexes == ["Cab", "Cat", "Mat"]
    assert paths["Mat"].path_weight == 2


def test_bellman_ford_11():
    graph = graph_11()
    paths, ncc = bellman_ford(graph, 0)
    assert not ncc
    assert paths[0].vertexes == [0]
    assert paths[0].path_weight == 0
    assert paths[1].vertexes == [0, 1, 2, 3, 1]
    assert paths[1].path_weight == 0
    assert paths[2].vertexes == [0, 1, 2, 3, 1, 2]
    assert paths[2].path_weight == 2
    assert paths[3].vertexes == [0, 1, 2, 3]
    assert paths[3].path_weight == 6
    assert paths[4].vertexes == [0, 1, 2, 3, 4]
    assert paths[4].path_weight == 10

    paths, ncc = bellman_ford(graph, 1)
    assert not ncc
    assert paths[0].vertexes == [1, 2, 3, 4, 0]
    assert paths[0].path_weight == 14
    assert paths[1].vertexes == [1, 2, 3, 1]
    assert paths[1].path_weight == -1
    assert paths[2].vertexes == [1, 2, 3, 1, 2]
    assert paths[2].path_weight == 1
    assert paths[3].vertexes == [1, 2, 3, 1, 2, 3]
    assert paths[3].path_weight == 4
    assert paths[4].vertexes == [1, 2, 3, 4]
    assert paths[4].path_weight == 9


if __name__ == '__main__':
    test_bellman_ford_11()
