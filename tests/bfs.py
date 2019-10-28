from graph import Graph, Node
import pytest


class TestBFS:

    def test_graph_1(self):
        """
        https://ru.wikipedia.org/wiki/Поиск_в_ширину
        """

        def graph():
            g = Graph().create_graph(type='adjList', oriented=True)
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

            g.add_node(node1)
            g.add_node(node2)
            g.add_node(node3)
            g.add_node(node4)
            g.add_node(node5)
            g.add_node(node6)
            g.add_node(node7)
            g.add_node(node8)
            g.add_node(node9)
            g.add_node(node10)

            g.add_edge(1, 2)
            g.add_edge(1, 3)
            g.add_edge(1, 4)
            g.add_edge(2, 5)
            g.add_edge(5, 9)
            g.add_edge(3, 6)
            g.add_edge(3, 7)
            g.add_edge(6, 10)
            g.add_edge(4, 8)
            return g

        g = graph()
        path = g.bfs(1, 10)
        assert path[10] == [1, 3, 6, 10]
        path = g.bfs(1, 8)
        assert path[8] == [1, 4, 8]
        try:
            path = g.bfs(1, 12)
        except Exception as ex:
            # TODO : implement exception
            assert ex
