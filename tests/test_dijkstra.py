import pytest

from core.algorithms import dijkstra
from core.graphs import create_graph, GraphType
from tests.conftest import graph_3_1, graph_3_2, graph_4_1, graph_4_2, graph_5, graph_6, graph_7


@pytest.mark.parametrize(
    "graph_type",
    [
        GraphType.AdjList,
    ],
)
def test_dijkstra_3_1(graph_type: GraphType):
    graph = create_graph(graph_type, oriented=True)
    graph = graph_3_1(graph)
    w, p = dijkstra(graph, 'A')
    assert w == {'A': 0, 'B': 5, 'C': 2, 'D': 9, 'E': 7, 'F': 8}
    assert p['A'] == ['A']
    assert p['B'] == ['A', 'B']
    assert p['C'] == ['A', 'C']
    assert p['D'] == ['A', 'B', 'D']
    assert p['E'] == ['A', 'B', 'E']
    assert p['F'] == ['A', 'B', 'E', 'F']

    w, p = dijkstra(graph, 'B')
    assert w == {'A': float('inf'), 'B': 0, 'C': float('inf'), 'D': 4, 'E': 2, 'F': 3}
    assert p.get('A') is None
    assert p['B'] == ['B']
    assert p.get('C') is None
    assert p['D'] == ['B', 'D']
    assert p['E'] == ['B', 'E']
    assert p['F'] == ['B', 'E', 'F']

    w, p = dijkstra(graph, 'C')
    assert w == {'A': float('inf'), 'B': 8, 'C': 0, 'D': 12, 'E': 7, 'F': 8}
    assert p.get('A') is None
    assert p['B'] == ['C', 'B']
    assert p['C'] == ['C']
    assert p['D'] == ['C', 'B', 'D']
    assert p['E'] == ['C', 'E']
    assert p['F'] == ['C', 'E', 'F']

    w, p = dijkstra(graph, 'D')
    assert w == {'A': float('inf'), 'B': float('inf'), 'C': float('inf'), 'D': 0, 'E': 6, 'F': 3}
    assert p.get('A') is None
    assert p.get('B') is None
    assert p.get('C') is None
    assert p['D'] == ['D']
    assert p['E'] == ['D', 'E']
    assert p['F'] == ['D', 'F']

    w, p = dijkstra(graph, 'E')
    assert w == {'A': float('inf'), 'B': float('inf'), 'C': float('inf'), 'D': float('inf'), 'E': 0,
                 'F': 1}
    assert p.get('A') is None
    assert p.get('B') is None
    assert p.get('C') is None
    assert p.get('D') is None
    assert p['E'] == ['E']
    assert p['F'] == ['E', 'F']

    w, p = dijkstra(graph, 'F')
    assert w == {'A': float('inf'), 'B': float('inf'), 'C': float('inf'), 'D': float('inf'),
                 'E': float('inf'), 'F': 0}
    assert p.get('A') is None
    assert p.get('B') is None
    assert p.get('C') is None
    assert p.get('D') is None
    assert p.get('E') is None
    assert p['F'] == ['F']


@pytest.mark.parametrize(
    "graph_type",
    [
        GraphType.AdjList,
    ],
)
def test_dijkstra_3_2(graph_type: GraphType):
    graph = create_graph(graph_type, oriented=True)
    graph = graph_3_2(graph)
    w, p = dijkstra(graph, 'A')
    assert w == {'C': 2, 'B': 5, 'A': 0, 'D': float('inf'), 'E': 7, 'F': 8}
    assert p['A'] == ['A']
    assert p['B'] == ['A', 'B']
    assert p['C'] == ['A', 'C']
    assert p.get('D') is None
    assert p['E'] == ['A', 'B', 'E']
    assert p['F'] == ['A', 'B', 'E', 'F']

    w, p = dijkstra(graph, 'B')
    assert w == {'A': float('inf'), 'B': 0, 'C': float('inf'), 'D': float('inf'), 'E': 2, 'F': 3}
    assert p.get('A') is None
    assert p['B'] == ['B']
    assert p.get('C') is None
    assert p.get('D') is None
    assert p['E'] == ['B', 'E']
    assert p['F'] == ['B', 'E', 'F']

    w, p = dijkstra(graph, 'C')
    assert w == {'A': float('inf'), 'B': 8, 'C': 0, 'D': float('inf'), 'E': 7, 'F': 8}
    assert p.get('A') is None
    assert p['B'] == ['C', 'B']
    assert p['C'] == ['C']
    assert p.get('D') is None
    assert p['E'] == ['C', 'E']
    assert p['F'] == ['C', 'E', 'F']

    w, p = dijkstra(graph, 'D')
    assert w == {'A': float('inf'), 'B': 4, 'C': float('inf'), 'D': 0, 'E': 6, 'F': 3}
    assert p.get('A') is None
    assert p['B'] == ['D', 'B']
    assert p.get('C') is None
    assert p['D'] == ['D']
    assert p['E'] == ['D', 'E']
    assert p['F'] == ['D', 'F']

    w, p = dijkstra(graph, 'E')
    assert w == {'A': float('inf'), 'B': float('inf'), 'C': float('inf'), 'D': float('inf'), 'E': 0, 'F': 1}
    assert p.get('A') is None
    assert p.get('B') is None
    assert p.get('C') is None
    assert p.get('D') is None
    assert p['E'] == ['E']
    assert p['F'] == ['E', 'F']

    w, p = dijkstra(graph, 'F')
    assert w == {'A': float('inf'), 'B': float('inf'), 'C': float('inf'), 'D': float('inf'), 'E': float('inf'),
                 'F': 0}
    assert p.get('A') is None
    assert p.get('B') is None
    assert p.get('C') is None
    assert p.get('D') is None
    assert p.get('E') is None
    assert p['F'] == ['F']


@pytest.mark.parametrize(
    "graph_type",
    [
        GraphType.AdjList,
    ],
)
def test_dijkstra_4_1(graph_type: GraphType):
    graph = create_graph(graph_type, oriented=True)
    graph = graph_4_1(graph)
    w, p = dijkstra(graph, 'A')
    assert w == {'A': 0, 'B': 10, 'C': 30, 'D': 31, 'E': 60}
    assert p['A'] == ['A']
    assert p['B'] == ['A', 'B']
    assert p['C'] == ['A', 'B', 'C']
    assert p['D'] == ['A', 'B', 'C', 'D']
    assert p['E'] == ['A', 'B', 'C', 'E']

    w, p = dijkstra(graph, 'B')
    assert w == {'A': float('inf'), 'B': 0, 'C': 20, 'D': 21, 'E': 50}
    assert p.get('A') is None
    assert p['B'] == ['B']
    assert p['C'] == ['B', 'C']
    assert p['D'] == ['B', 'C', 'D']
    assert p['E'] == ['B', 'C', 'E']

    w, p = dijkstra(graph, 'C')
    assert w == {'A': float('inf'), 'B': 2, 'C': 0, 'D': 1, 'E': 30}
    assert p.get('A') is None
    assert p['B'] == ['C', 'D', 'B']
    assert p['C'] == ['C']
    assert p['D'] == ['C', 'D']
    assert p['E'] == ['C', 'E']

    w, p = dijkstra(graph, 'D')
    assert w == {'A': float('inf'), 'B': 1, 'C': 21, 'D': 0, 'E': 51}
    assert p.get('A') is None
    assert p['B'] == ['D', 'B']
    assert p['C'] == ['D', 'B', 'C']
    assert p['D'] == ['D']
    assert p['E'] == ['D', 'B', 'C', 'E']

    w, p = dijkstra(graph, 'E')
    assert w == {'A': float('inf'), 'B': float('inf'), 'C': float('inf'), 'D': float('inf'), 'E': 0}
    assert p.get('A') is None
    assert p.get('B') is None
    assert p.get('C') is None
    assert p.get('D') is None
    assert p['E'] == ['E']


@pytest.mark.parametrize(
    "graph_type",
    [
        GraphType.AdjList,
    ],
)
def test_dijkstra_4_2(graph_type: GraphType):
    graph = create_graph(graph_type, oriented=True)
    graph = graph_4_2(graph)
    w, p = dijkstra(graph, 'A')
    assert w == {'A': 0, 'B': 10, 'C': 30, 'D': 31, 'E': 38, 'F': 33}
    assert p['A'] == ['A']
    assert p['B'] == ['A', 'B']
    assert p['C'] == ['A', 'B', 'C']
    assert p['D'] == ['A', 'B', 'C', 'D']
    assert p['E'] == ['A', 'B', 'C', 'D', 'F', 'E']
    assert p['F'] == ['A', 'B', 'C', 'D', 'F']

    w, p = dijkstra(graph, 'B')
    assert w == {'A': float('inf'), 'B': 0, 'C': 20, 'D': 21, 'E': 28, 'F': 23}
    assert p.get('A') is None
    assert p['B'] == ['B']
    assert p['C'] == ['B', 'C']
    assert p['D'] == ['B', 'C', 'D']
    assert p['E'] == ['B', 'C', 'D', 'F', 'E']
    assert p['F'] == ['B', 'C', 'D', 'F']

    w, p = dijkstra(graph, 'C')
    assert w == {'A': float('inf'), 'B': 2, 'C': 0, 'D': 1, 'E': 8, 'F': 3}
    assert p.get('A') is None
    assert p['B'] == ['C', 'D', 'B']
    assert p['C'] == ['C']
    assert p['D'] == ['C', 'D']
    assert p['E'] == ['C', 'D', 'F', 'E']
    assert p['F'] == ['C', 'D', 'F']

    w, p = dijkstra(graph, 'D')
    assert w == {'A': float('inf'), 'B': 1, 'C': 21, 'D': 0, 'E': 7, 'F': 2}
    assert p.get('A') is None
    assert p['B'] == ['D', 'B']
    assert p['C'] == ['D', 'B', 'C']
    assert p['D'] == ['D']
    assert p['E'] == ['D', 'F', 'E']
    assert p['F'] == ['D', 'F']

    w, p = dijkstra(graph, 'E')
    assert w == {'A': float('inf'), 'B': float('inf'), 'C': float('inf'), 'D': float('inf'), 'E': 0,
                 'F': float('inf')}
    assert p.get('A') is None
    assert p.get('B') is None
    assert p.get('C') is None
    assert p.get('D') is None
    assert p['E'] == ['E']
    assert p.get('F') is None

    w, p = dijkstra(graph, 'F')
    assert w == {'A': float('inf'), 'B': 3, 'C': 23, 'D': 2, 'E': 5, 'F': 0}
    assert p.get('A') is None
    assert p['B'] == ['F', 'D', 'B']
    assert p['C'] == ['F', 'D', 'B', 'C']
    assert p['D'] == ['F', 'D']
    assert p['E'] == ['F', 'E']
    assert p['F'] == ['F']


@pytest.mark.parametrize(
    "graph_type",
    [
        GraphType.AdjList,
    ],
)
def test_dijkstra_5(graph_type: GraphType):
    graph = create_graph(graph_type, oriented=True)
    graph = graph_5(graph)
    w, p = dijkstra(graph, 'A')
    assert w == {'A': 0, 'B': 2, 'C': 1, 'D': 3}
    assert p['A'] == ['A']
    assert p['B'] == ['A', 'B']
    assert p['C'] == ['A', 'C']
    assert p['D'] == ['A', 'D']

    w, p = dijkstra(graph, 'B')
    assert w == {'A': 5, 'B': 0, 'C': 4, 'D': 8}
    assert p['A'] == ['B', 'C', 'A']
    assert p['B'] == ['B']
    assert p['C'] == ['B', 'C']
    assert p['D'] == ['B', 'C', 'A', 'D']

    w, p = dijkstra(graph, 'C')
    assert w == {'A': 1, 'B': 3, 'C': 0, 'D': 4}
    assert p['A'] == ['C', 'A']
    assert p['B'] == ['C', 'A', 'B']
    assert p['C'] == ['C']
    assert p['D'] == ['C', 'A', 'D']

    w, p = dijkstra(graph, 'D')
    assert w == {'A': float('inf'), 'B': float('inf'), 'C': float('inf'), 'D': 0}
    assert p.get('A') is None
    assert p.get('B') is None
    assert p.get('C') is None
    assert p['D'] == ['D']


@pytest.mark.parametrize(
    "graph_type",
    [
        GraphType.AdjList,
    ],
)
def test_dijkstra_6(graph_type: GraphType):
    graph = create_graph(graph_type, oriented=True)
    graph = graph_6(graph)
    w, p = dijkstra(graph, 'A')
    assert w == {'A': 0, 'B': 2, 'C': 4}
    assert p['A'] == ['A']
    assert p['B'] == ['A', 'B']
    assert p['C'] == ['A', 'B', 'C']

    w, p = dijkstra(graph, 'B')
    assert w == {'A': float('inf'), 'B': 0, 'C': 2}
    assert p.get('A') is None
    assert p['B'] == ['B']
    assert p['C'] == ['B', 'C']

    w, p = dijkstra(graph, 'C')
    assert w == {'A': float('inf'), 'B': float('inf'), 'C': 0}
    assert p.get('A') is None
    assert p.get('B') is None
    assert p['C'] == ['C']


@pytest.mark.parametrize(
    "graph_type",
    [
        GraphType.AdjList,
    ],
)
def test_dijkstra_7(graph_type: GraphType):
    graph = create_graph(graph_type, oriented=True)
    graph = graph_7(graph)
    w, p = dijkstra(graph, 'Cab')
    assert w == {'Cab': 0, 'Car': 1, 'Bar': 2, 'Cat': 1, 'Bat': 2, 'Mat': 2}
    assert p['Cab'] == ['Cab']
    assert p['Car'] == ['Cab', 'Car']
    assert p['Cat'] == ['Cab', 'Cat']
    assert p['Bar'] == ['Cab', 'Car', 'Bar']
    assert p['Bat'] == ['Cab', 'Cat', 'Bat']
    assert p['Mat'] == ['Cab', 'Cat', 'Mat']
