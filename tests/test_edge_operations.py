import pytest

from core.exceptions import EdgeAddError, EdgeRemoveError
from core.graphs import GraphType, create_graph
from tests.conftest import graph_2


def check_edge_not_exists(graph, src, dst):
    assert all([not ((edge.src == src) and (edge.dst == dst)) for edge in graph.get_edges()])


def check_edge_exists(graph, name):
    found = False
    for edge in graph.get_edges():
        if edge.name == name:
            found = True
            break
    assert found


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
def test_remove_by_src_dst(graph_type: GraphType, directed, weighted):
    graph = create_graph(graph_type, directed=directed, weighted=weighted)
    graph = graph_2(graph)
    graph.remove_edge_by_vertexes("C", "F")
    check_edge_not_exists(graph, "C", "F")


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
def test_remove_by_name(graph_type: GraphType, directed, weighted):
    graph = create_graph(graph_type, directed=directed, weighted=weighted)
    graph = graph_2(graph)
    graph.remove_edge_by_name("b")
    check_edge_not_exists(graph, "S", "D")

    graph = create_graph(graph_type, directed=directed, weighted=weighted)
    graph = graph_2(graph)
    graph.remove_edge_by_name("g")
    check_edge_not_exists(graph, "C", "F")


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
def test_add_edge(graph_type: GraphType, directed, weighted):
    graph = create_graph(graph_type, directed=directed, weighted=weighted)
    graph = graph_2(graph)
    graph.add_edge("D", "C", name="DC")
    check_edge_exists(graph, "DC")


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
def test_add_edge_error(graph_type: GraphType, directed, weighted):
    graph = create_graph(graph_type, directed=directed, weighted=weighted)
    graph = graph_2(graph)
    with pytest.raises(EdgeAddError):
        graph.add_edge("S", "D", name="b")


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
def test_remove_edge_error_1(graph_type: GraphType, directed, weighted):
    graph = create_graph(graph_type, directed=directed, weighted=weighted)
    graph = graph_2(graph)
    with pytest.raises(EdgeRemoveError):
        graph.remove_edge_by_name("P")


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
def test_remove_edge_error_2(graph_type: GraphType, directed, weighted):
    graph = create_graph(graph_type, directed=directed, weighted=weighted)
    graph = graph_2(graph)
    with pytest.raises(EdgeRemoveError):
        graph.remove_edge_by_vertexes("D", "C")

    with pytest.raises(EdgeRemoveError):
        graph.remove_edge_by_vertexes("D", "B")
