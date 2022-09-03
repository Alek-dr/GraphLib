import pytest

from core.algorithms import topological_sort
from core.graphs import GraphType, create_graph
from core.graphs.graph import AbstractGraph
from tests.conftest import graph_1, graph_10


def check_topological_sort(graph: AbstractGraph) -> bool:
    sorted_v = topological_sort(graph)
    for i, v in enumerate(sorted_v):
        edges = graph.get_adj_edges(v)
        for edge in edges:
            ind = sorted_v.index(edge.dst)
            if ind < i:
                return False
    return True


def test_graph_10():
    graph = graph_10()
    assert check_topological_sort(graph)


@pytest.mark.parametrize(
    "graph_type, weighted",
    [
        [GraphType.AdjList, True],
        [GraphType.AdjList, False],
    ],
)
def test_graph_1(graph_type: GraphType, weighted):
    graph = create_graph(graph_type, directed=True, weighted=weighted)
    graph = graph_1(graph)
    assert check_topological_sort(graph)
