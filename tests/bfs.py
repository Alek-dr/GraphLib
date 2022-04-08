from core.graph import Graph, Node


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

    def test_graph_2(self):
        """
        Грокаем алгоритмы. стр.137, 6.1
        """

        def graph():
            g = Graph().create_graph(type='adjList', oriented=True)
            nodeS = Node('S')
            nodeD = Node('D')
            nodeB = Node('B')
            nodeE = Node('E')
            nodeC = Node('C')
            nodeF = Node('F')

            g.add_node(nodeS)
            g.add_node(nodeD)
            g.add_node(nodeB)
            g.add_node(nodeE)
            g.add_node(nodeF)
            g.add_node(nodeC)

            g.add_edge('S', 'D')
            g.add_edge('S', 'B')
            g.add_edge('D', 'E')
            g.add_edge('B', 'E')
            g.add_edge('B', 'C')
            g.add_edge('D', 'F')
            g.add_edge('C', 'F')
            return g

        g = graph()
        path = g.bfs('S', 'F')
        assert path['F'] == ['S', 'D', 'F']

    def test_graph_3(self):
        """
        Грокаем алгоритмы. стр.138, 6.2
        """

        def graph():
            g = Graph().create_graph(type='adjList', oriented=True)
            Cab = Node('Cab')
            Car = Node('Car')
            Bar = Node('Bar')
            Cat = Node('Cat')
            Bat = Node('Bat')
            Mat = Node('Mat')

            g.add_node(Cab)
            g.add_node(Car)
            g.add_node(Bar)
            g.add_node(Cat)
            g.add_node(Bat)
            g.add_node(Mat)

            g.add_edge('Cab', 'Car')
            g.add_edge('Cab', 'Cat')
            g.add_edge('Car', 'Bar')
            g.add_edge('Car', 'Cat')
            g.add_edge('Bar', 'Bat')
            g.add_edge('Cat', 'Bat')
            g.add_edge('Cat', 'Mat')
            g.add_edge('Mat', 'Bat')
            return g

        g = graph()
        path = g.bfs('Cab', 'Bat')
        assert path['Bat'] == ['Cab', 'Cat', 'Bat']
        path = g.bfs('Cab', 'Mat')
        assert path['Mat'] == ['Cab', 'Cat', 'Mat']
        path = g.bfs('Cab', 'Bar')
        assert path['Bar'] == ['Cab', 'Car', 'Bar']
