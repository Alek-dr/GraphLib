import networkx as nx
import pytest

from core.graphs import Node, create_graph
from core.graphs.graph import AbstractGraph


def create_nxgraph(graph: AbstractGraph) -> nx.Graph:
    if graph.is_directed:
        G = nx.MultiDiGraph()
    else:
        G = nx.MultiGraph()
    for v in graph.vertexes:
        G.add_node(v.name)
    for edge in graph.get_edges():
        G.add_edge(edge.src, edge.dst, weight=edge.weight)
    return G


def graph_1(graph, weighted=False):
    """
    https://ru.wikipedia.org/wiki/Поиск_в_ширину
    """
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)
    node7 = Node(7)
    node8 = Node(8)
    node9 = Node(9)
    node10 = Node(10)

    graph.add_node(node1)
    graph.add_node(node2)
    graph.add_node(node3)
    graph.add_node(node4)
    graph.add_node(node5)
    graph.add_node(node6)
    graph.add_node(node7)
    graph.add_node(node8)
    graph.add_node(node9)
    graph.add_node(node10)

    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(1, 4)
    graph.add_edge(2, 5)
    graph.add_edge(5, 9)
    graph.add_edge(3, 6)
    graph.add_edge(3, 7)
    graph.add_edge(6, 10)
    graph.add_edge(4, 8)
    return graph


def graph_2(graph, weighted=False) -> AbstractGraph:
    """
    Грокаем алгоритмы. стр.137, 6.1
    """
    nodeS = Node("S")
    nodeB = Node("B")
    nodeD = Node("D")
    nodeE = Node("E")
    nodeC = Node("C")
    nodeF = Node("F")

    graph.add_node(nodeS)
    graph.add_node(nodeB)
    graph.add_node(nodeD)
    graph.add_node(nodeE)
    graph.add_node(nodeC)
    graph.add_node(nodeF)

    graph.add_edge("S", "B")
    graph.add_edge("S", "D")
    graph.add_edge("B", "E")
    graph.add_edge("D", "E")
    graph.add_edge("B", "C")
    graph.add_edge("D", "F")
    graph.add_edge("C", "F")
    return graph


def graph_3_1(graph, weighted=False) -> AbstractGraph:
    """
    Граф из "Грокаем алгоритмы. Алгоритм Дейкстры" стр.181"
    """
    nodeA = Node("A")
    nodeB = Node("B")
    nodeC = Node("C")
    nodeD = Node("D")
    nodeE = Node("E")
    nodeF = Node("F")

    graph.add_node(nodeA)
    graph.add_node(nodeC)
    graph.add_node(nodeB)
    graph.add_node(nodeE)
    graph.add_node(nodeD)
    graph.add_node(nodeF)

    if weighted:
        graph.add_edge("A", "C", 2)
        graph.add_edge("A", "B", 5)
        graph.add_edge("B", "D", 4)
        graph.add_edge("B", "E", 2)
        graph.add_edge("C", "B", 8)
        graph.add_edge("C", "E", 7)
        graph.add_edge("D", "F", 3)
        graph.add_edge("D", "E", 6)
        graph.add_edge("E", "F", 1)
    else:
        graph.add_edge("A", "C")
        graph.add_edge("A", "B")
        graph.add_edge("B", "D")
        graph.add_edge("B", "E")
        graph.add_edge("C", "B")
        graph.add_edge("C", "E")
        graph.add_edge("D", "F")
        graph.add_edge("D", "E")
        graph.add_edge("E", "F")
    return graph


def graph_3_2(graph, weighted=False):
    """
    Граф 3_1, изменен путь B->D на D->B. В D попасть невозможно
    """
    nodeA = Node("A")
    nodeB = Node("B")
    nodeC = Node("C")
    nodeD = Node("D")
    nodeE = Node("E")
    nodeF = Node("F")

    graph.add_node(nodeA)
    graph.add_node(nodeB)
    graph.add_node(nodeC)
    graph.add_node(nodeD)
    graph.add_node(nodeE)
    graph.add_node(nodeF)

    if weighted:
        graph.add_edge("A", "B", 5)
        graph.add_edge("A", "C", 2)
        graph.add_edge("B", "E", 2)
        graph.add_edge("C", "B", 8)
        graph.add_edge("C", "E", 7)
        graph.add_edge("D", "F", 3)
        graph.add_edge("D", "B", 4)
        graph.add_edge("D", "E", 6)
        graph.add_edge("E", "F", 1)
    else:
        graph.add_edge("A", "B")
        graph.add_edge("A", "C")
        graph.add_edge("B", "E")
        graph.add_edge("C", "B")
        graph.add_edge("C", "E")
        graph.add_edge("D", "F")
        graph.add_edge("D", "B")
        graph.add_edge("D", "E")
        graph.add_edge("E", "F")
    return graph


def graph_4_1(graph, weighted=False):
    """
    Граф из "Грокаем алгоритмы. Алгоритм Дейкстры" стр.181"
    """
    nodeA = Node("A")
    nodeB = Node("B")
    nodeC = Node("C")
    nodeD = Node("D")
    nodeE = Node("E")

    graph.add_node(nodeA)
    graph.add_node(nodeB)
    graph.add_node(nodeC)
    graph.add_node(nodeD)
    graph.add_node(nodeE)
    if weighted:
        graph.add_edge("A", "B", 10)
        graph.add_edge("B", "C", 20)
        graph.add_edge("C", "D", 1)
        graph.add_edge("D", "B", 1)
        graph.add_edge("C", "E", 30)
    else:
        graph.add_edge("A", "B")
        graph.add_edge("B", "C")
        graph.add_edge("C", "D")
        graph.add_edge("D", "B")
        graph.add_edge("C", "E")
    return graph


def graph_4_2(graph, weighted=False):
    """
    Граф 4.1, добавлена вершина F и ребра C->F, F->E, D<->F
    """
    nodeA = Node("A")
    nodeB = Node("B")
    nodeC = Node("C")
    nodeD = Node("D")
    nodeE = Node("E")
    nodeF = Node("F")

    graph.add_node(nodeA)
    graph.add_node(nodeB)
    graph.add_node(nodeC)
    graph.add_node(nodeD)
    graph.add_node(nodeE)
    graph.add_node(nodeF)
    if weighted:
        graph.add_edge("A", "B", 10)
        graph.add_edge("B", "C", 20)
        graph.add_edge("C", "D", 1)
        graph.add_edge("D", "B", 1)
        graph.add_edge("C", "E", 30)
        graph.add_edge("C", "F", 10)
        graph.add_edge("F", "E", 5)
        graph.add_edge("D", "F", 2)
        graph.add_edge("F", "D", 2)
    else:
        graph.add_edge("A", "B")
        graph.add_edge("B", "C")
        graph.add_edge("C", "D")
        graph.add_edge("D", "B")
        graph.add_edge("C", "E")
        graph.add_edge("C", "F")
        graph.add_edge("F", "E")
        graph.add_edge("D", "F")
        graph.add_edge("F", "D")
    return graph


def graph_5(graph, weighted=False):
    nodeA = Node("A")
    nodeB = Node("B")
    nodeC = Node("C")
    nodeD = Node("D")

    graph.add_node(nodeA)
    graph.add_node(nodeB)
    graph.add_node(nodeC)
    graph.add_node(nodeD)

    if weighted:
        graph.add_edge("A", "B", 2)
        graph.add_edge("A", "D", 3)
        graph.add_edge("A", "C", 1)
        graph.add_edge("B", "C", 4)
        graph.add_edge("C", "A", 1)
    else:
        graph.add_edge("A", "B")
        graph.add_edge("A", "D")
        graph.add_edge("A", "C")
        graph.add_edge("B", "C")
        graph.add_edge("C", "A")
    return graph


def graph_6(graph, weighted=False):
    nodeA = Node("A")
    nodeB = Node("B")
    nodeC = Node("C")

    graph.add_node(nodeA)
    graph.add_node(nodeB)
    graph.add_node(nodeC)
    if weighted:
        graph.add_edge("A", "B", 2)
        graph.add_edge("B", "B", 3)
        graph.add_edge("B", "C", 2)
    else:
        graph.add_edge("A", "B")
        graph.add_edge("B", "B")
        graph.add_edge("B", "C")
    return graph


def graph_7(graph, weighted=False):
    """
    Грокаем алгоритмы. стр.138, 6.2
    """
    Cab = Node("Cab")
    Car = Node("Car")
    Bar = Node("Bar")
    Cat = Node("Cat")
    Bat = Node("Bat")
    Mat = Node("Mat")

    graph.add_node(Cab)
    graph.add_node(Car)
    graph.add_node(Bar)
    graph.add_node(Cat)
    graph.add_node(Bat)
    graph.add_node(Mat)

    graph.add_edge("Cab", "Car")
    graph.add_edge("Cab", "Cat")
    graph.add_edge("Car", "Bar")
    graph.add_edge("Car", "Cat")
    graph.add_edge("Bar", "Bat")
    graph.add_edge("Cat", "Bat")
    graph.add_edge("Cat", "Mat")
    graph.add_edge("Mat", "Bat")
    return graph


def graph_8(weighted=False):
    graph = create_graph(directed=False, weighted=False)
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)

    graph.add_node(node1)
    graph.add_node(node2)
    graph.add_node(node3)
    graph.add_node(node4)

    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(1, 3)
    graph.add_edge(2, 4)
    graph.add_edge(2, 2)
    graph.add_edge(3, 4)
    graph.add_edge(3, 4)
    graph.add_edge(3, 4)
    return graph


def graph_8_2(weighted=False):
    graph = create_graph(directed=True)
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)

    graph.add_node(node1)
    graph.add_node(node2)
    graph.add_node(node3)
    graph.add_node(node4)

    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(1, 3)
    graph.add_edge(2, 4)
    graph.add_edge(2, 2)
    graph.add_edge(3, 4)
    graph.add_edge(3, 4)
    graph.add_edge(3, 4)
    return graph


def graph_9(weighted=False):
    graph = create_graph(directed=True)
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)

    graph.add_node(node1)
    graph.add_node(node2)
    graph.add_node(node3)

    graph.add_edge(1, 2)
    graph.add_edge(2, 3)
    graph.add_edge(2, 3)
    return graph


def graph_10(weighted=False):
    """Алгоритмы для начинающих. Стр. 196"""
    graph = create_graph(directed=True, weighted=False)
    zero = Node(0)
    one = Node(1)
    two = Node(2)
    three = Node(3)
    four = Node(4)
    five = Node(5)
    six = Node(6)
    seven = Node(7)
    eight = Node(8)
    nine = Node(9)
    ten = Node(10)

    graph.add_node(zero)
    graph.add_node(one)
    graph.add_node(two)
    graph.add_node(three)
    graph.add_node(four)
    graph.add_node(five)
    graph.add_node(six)
    graph.add_node(seven)
    graph.add_node(eight)
    graph.add_node(nine)
    graph.add_node(ten)

    graph.add_edge(0, 1)
    graph.add_edge(1, 2)
    graph.add_edge(0, 3)
    graph.add_edge(3, 4)
    graph.add_edge(4, 2)
    graph.add_edge(4, 5)
    graph.add_edge(6, 3)
    graph.add_edge(6, 7)
    graph.add_edge(8, 6)
    graph.add_edge(8, 9)
    graph.add_edge(9, 7)
    return graph


def graph_11(weighted=False):
    """Алгоритмы для начинающих. Стр. 253"""
    graph = create_graph(directed=True, weighted=True)
    zero = Node(0)
    one = Node(1)
    two = Node(2)
    three = Node(3)
    four = Node(4)

    graph.add_node(zero)
    graph.add_node(one)
    graph.add_node(two)
    graph.add_node(three)
    graph.add_node(four)

    if weighted:
        graph.add_edge(0, 1, 1)
        graph.add_edge(1, 2, 2)
        graph.add_edge(2, 3, 3)
        graph.add_edge(2, 3, 3)
        graph.add_edge(3, 1, -6)
        graph.add_edge(3, 4, 4)
        graph.add_edge(4, 0, 5)
    else:
        graph.add_edge(0, 1)
        graph.add_edge(1, 2)
        graph.add_edge(2, 3)
        graph.add_edge(2, 3)
        graph.add_edge(3, 1)
        graph.add_edge(3, 4)
        graph.add_edge(4, 0)
    return graph


def graph_12(weighted=False):
    """
    https://ru.wikipedia.org/wiki/Компонента_связности_графа
    """
    graph = create_graph(directed=False, weighted=False)
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")
    e = Node("e")
    f = Node("f")
    g = Node("g")

    graph.add_node(a)
    graph.add_node(b)
    graph.add_node(c)
    graph.add_node(d)
    graph.add_node(e)
    graph.add_node(f)
    graph.add_node(g)

    graph.add_edge("a", "b")
    graph.add_edge("b", "c")
    graph.add_edge("c", "d")
    graph.add_edge("f", "g")
    return graph
