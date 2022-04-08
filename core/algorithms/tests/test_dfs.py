from core.algorithms.dfs import dfs
from core.graphs import Node
from core.graphs.graph_factory import create_graph, GraphType


class TestDFS:

    def test_graph_1(self):
        """
        https://ru.wikipedia.org/wiki/Поиск_в_ширину
        """

        def graph_1(graph_type: GraphType):
            graph = create_graph(graph_type, oriented=True)
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

        g = graph_1(GraphType.AdjList)
        path = dfs(g, 1, 10)
        assert path[10] == [1, 3, 6, 10]
        path = dfs(g, 1, 8)
        assert path[8] == [1, 4, 8]
        try:
            path = dfs(g, 1, 12)
        except Exception as ex:
            # TODO : implement exception
            assert ex

    def test_graph_2(self):
        """
        Грокаем алгоритмы. стр.137, 6.1
        """

        def graph_2(graph_type: GraphType):
            graph = create_graph(graph_type, oriented=True)
            nodeS = Node('S')
            nodeD = Node('D')
            nodeB = Node('B')
            nodeE = Node('E')
            nodeC = Node('C')
            nodeF = Node('F')

            graph.add_node(nodeS)
            graph.add_node(nodeD)
            graph.add_node(nodeB)
            graph.add_node(nodeE)
            graph.add_node(nodeF)
            graph.add_node(nodeC)

            graph.add_edge('S', 'D')
            graph.add_edge('S', 'B')
            graph.add_edge('D', 'E')
            graph.add_edge('B', 'E')
            graph.add_edge('B', 'C')
            graph.add_edge('D', 'F')
            graph.add_edge('C', 'F')
            return graph

        g = graph_2(GraphType.AdjList)
        path = dfs(g, 'S', 'F')
        assert path['F'] == ['S', 'D', 'F']
        path = dfs(g, 'D', 'E')
        assert path['E'] == ['D', 'E']
        path = dfs(g, 'S', 'C')
        assert path['C'] == ['S', 'B', 'C']
