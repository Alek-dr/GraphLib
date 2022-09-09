import pydot
from jinja2 import Template

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


def graph_8():
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


def graph_12():
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


def _edge(v1, v2, line_style, **kwargs):
    edge = f"{v1} {line_style} {v2}"
    if len(kwargs):
        edge += " ["
        for k, v in kwargs.items():
            edge += f"{k}={v}"
        edge += "]"
    return edge


def _vertex(v, **kwargs):
    v = f"{v}"
    if len(kwargs):
        v += " ["
        for k, v in kwargs.items():
            v += f"{k}={v}"
        v += "]"
    return v


def convert_to_dot(
    graph: AbstractGraph, graph_name: str, edge_label: bool
) -> str:
    graph_components = []
    graph_type = "digraph" if graph.directed else "graph"
    edge_style = "->" if graph.directed else "--"
    attrs = {}
    v_set = set()
    for adj in graph.get_edges():
        if edge_label:
            attrs["label"] = adj.name
        e = _edge(adj.src, adj.dst, edge_style, **attrs)
        v_set.add(adj.src)
        v_set.add(adj.dst)
        graph_components.append(e)
    for v in graph.vertexes:
        if v.name not in v_set:
            vertex_ = _vertex(v)
            graph_components.append(vertex_)
        else:
            v_set.remove(v.name)
    template = """{{ graph_type }} {{ graph_name }} {
    {% for v in graph_components %}
        {{ v }}
    {% endfor %}
    }
    """
    attrs = {
        "graph_type": graph_type,
        "graph_name": graph_name,
        "graph_components": graph_components,
    }
    j2_template = Template(template)
    return j2_template.render(attrs)


def save_graph_img(
    graph: AbstractGraph, graph_name: str, output: str, edge_label: bool = True
):
    s = convert_to_dot(graph, graph_name, edge_label)
    dot = pydot.graph_from_dot_data(s)[0]
    dot.write_png(output)


if __name__ == "__main__":
    # g = create_graph(directed=True)
    graph = graph_8()
    save_graph_img(graph, "graph_2", f"../tests/graph_images/graph_8.png")
