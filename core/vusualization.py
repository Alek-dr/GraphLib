from jinja2 import Template
import pydot

from core.graphs import Node, create_graph
from core.graphs.graph import AbstractGraph


def graph_1(graph):
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


def graph_2(graph) -> AbstractGraph:
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


def _edge(v1, v2, line_style, **kwargs):
    edge = f"{v1} {line_style} {v2}"
    return edge


def convert_to_dot(graph: AbstractGraph, graph_name: str) -> str:
    graph_components = []
    graph_type = "digraph" if graph.directed else "graph"
    edge_style = "->" if graph.directed else "--"
    for adg in graph.get_edges():
        e = _edge(adg.src, adg.dst, edge_style)
        graph_components.append(e)
    template = """{{ graph_type }} {{ graph_name }} {
    {% for v in graph_components %}
        {{ v }}
    {% endfor %}
    }
    """
    attrs = {
        "graph_type": graph_type,
        "graph_name": graph_name,
        "graph_components": graph_components
    }
    j2_template = Template(template)
    return j2_template.render(attrs)


def save_graph_img(graph, graph_name, output):
    s = convert_to_dot(graph, graph_name)
    dot = pydot.graph_from_dot_data(s)[0]
    dot.write_png(output)


if __name__ == '__main__':
    graph = create_graph(directed=True)
    graph = graph_2(graph)
    save_graph_img(graph, "graph_2", f"../tests/graph_images/graph_2.png")
