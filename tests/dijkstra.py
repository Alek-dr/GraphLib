from core.graph import Graph, Node


class TestDijkstra:

    def test_graph_1(self):
        """
        Граф из "Грокаем алгоритмы. Алгоритм Дейкстры" стр.181"
        """

        def graph():
            g = Graph().create_graph(type='adjList', oriented=True)
            nodeA = Node("A")
            nodeB = Node('B')
            nodeC = Node('C')
            nodeD = Node('D')
            nodeE = Node('E')
            nodeF = Node('F')

            g.add_node(nodeA)
            g.add_node(nodeB)
            g.add_node(nodeC)
            g.add_node(nodeD)
            g.add_node(nodeE)
            g.add_node(nodeF)

            g.add_edge('A', 'B', 5)
            g.add_edge('A', 'C', 2)
            g.add_edge('B', 'D', 4)
            g.add_edge('B', 'E', 2)
            g.add_edge('C', 'B', 8)
            g.add_edge('C', 'E', 7)
            g.add_edge('D', 'F', 3)
            g.add_edge('D', 'E', 6)
            g.add_edge('E', 'F', 1)
            return g

        g = graph()
        w, p = g.dijkstra('A')
        assert w == {'A': 0, 'B': 5, 'C': 2, 'D': 9, 'E': 7, 'F': 8}
        assert p['A'] == ['A']
        assert p['B'] == ['A', 'B']
        assert p['C'] == ['A', 'C']
        assert p['D'] == ['A', 'B', 'D']
        assert p['E'] == ['A', 'B', 'E']
        assert p['F'] == ['A', 'B', 'E', 'F']

        w, p = g.dijkstra('B')
        assert w == {'A': float('inf'), 'B': 0, 'C': float('inf'), 'D': 4, 'E': 2, 'F': 3}
        assert p.get('A') is None
        assert p['B'] == ['B']
        assert p.get('C') is None
        assert p['D'] == ['B', 'D']
        assert p['E'] == ['B', 'E']
        assert p['F'] == ['B', 'E', 'F']

        w, p = g.dijkstra('C')
        assert w == {'A': float('inf'), 'B': 8, 'C': 0, 'D': 12, 'E': 7, 'F': 8}
        assert p.get('A') is None
        assert p['B'] == ['C', 'B']
        assert p['C'] == ['C']
        assert p['D'] == ['C', 'B', 'D']
        assert p['E'] == ['C', 'E']
        assert p['F'] == ['C', 'E', 'F']

        w, p = g.dijkstra('D')
        assert w == {'A': float('inf'), 'B': float('inf'), 'C': float('inf'), 'D': 0, 'E': 6, 'F': 3}
        assert p.get('A') is None
        assert p.get('B') is None
        assert p.get('C') is None
        assert p['D'] == ['D']
        assert p['E'] == ['D', 'E']
        assert p['F'] == ['D', 'F']

        w, p = g.dijkstra('E')
        assert w == {'A': float('inf'), 'B': float('inf'), 'C': float('inf'), 'D': float('inf'), 'E': 0,
                     'F': 1}
        assert p.get('A') is None
        assert p.get('B') is None
        assert p.get('C') is None
        assert p.get('D') is None
        assert p['E'] == ['E']
        assert p['F'] == ['E', 'F']

        w, p = g.dijkstra('F')
        assert w == {'A': float('inf'), 'B': float('inf'), 'C': float('inf'), 'D': float('inf'),
                     'E': float('inf'), 'F': 0}
        assert p.get('A') is None
        assert p.get('B') is None
        assert p.get('C') is None
        assert p.get('D') is None
        assert p.get('E') is None
        assert p['F'] == ['F']

    def test_graph_2(self):
        """
        Тот же граф, изменен путь B->D на D->B. В D попасть невозможно
        """

        def graph():
            g = Graph().create_graph(type='adjList', oriented=True)
            nodeA = Node("A")
            nodeB = Node('B')
            nodeC = Node('C')
            nodeD = Node('D')
            nodeE = Node('E')
            nodeF = Node('F')

            g.add_node(nodeA)
            g.add_node(nodeB)
            g.add_node(nodeC)
            g.add_node(nodeD)
            g.add_node(nodeE)
            g.add_node(nodeF)

            g.add_edge('A', 'B', 5)
            g.add_edge('A', 'C', 2)
            g.add_edge('B', 'E', 2)
            g.add_edge('C', 'B', 8)
            g.add_edge('C', 'E', 7)
            g.add_edge('D', 'F', 3)
            g.add_edge('D', 'B', 4)
            g.add_edge('D', 'E', 6)
            g.add_edge('E', 'F', 1)
            return g

        g = graph()
        w, p = g.dijkstra('A')
        assert w == {'C': 2, 'B': 5, 'A': 0, 'D': float('inf'), 'E': 7, 'F': 8}
        assert p['A'] == ['A']
        assert p['B'] == ['A', 'B']
        assert p['C'] == ['A', 'C']
        assert p.get('D') is None
        assert p['E'] == ['A', 'B', 'E']
        assert p['F'] == ['A', 'B', 'E', 'F']

        w, p = g.dijkstra('B')
        assert w == {'A': float('inf'), 'B': 0, 'C': float('inf'), 'D': float('inf'), 'E': 2, 'F': 3}
        assert p.get('A') is None
        assert p['B'] == ['B']
        assert p.get('C') is None
        assert p.get('D') is None
        assert p['E'] == ['B', 'E']
        assert p['F'] == ['B', 'E', 'F']

        w, p = g.dijkstra('C')
        assert w == {'A': float('inf'), 'B': 8, 'C': 0, 'D': float('inf'), 'E': 7, 'F': 8}
        assert p.get('A') is None
        assert p['B'] == ['C', 'B']
        assert p['C'] == ['C']
        assert p.get('D') is None
        assert p['E'] == ['C', 'E']
        assert p['F'] == ['C', 'E', 'F']

        w, p = g.dijkstra('D')
        assert w == {'A': float('inf'), 'B': 4, 'C': float('inf'), 'D': 0, 'E': 6, 'F': 3}
        assert p.get('A') is None
        assert p['B'] == ['D', 'B']
        assert p.get('C') is None
        assert p['D'] == ['D']
        assert p['E'] == ['D', 'E']
        assert p['F'] == ['D', 'F']

        w, p = g.dijkstra('E')
        assert w == {'A': float('inf'), 'B': float('inf'), 'C': float('inf'), 'D': float('inf'), 'E': 0, 'F': 1}
        assert p.get('A') is None
        assert p.get('B') is None
        assert p.get('C') is None
        assert p.get('D') is None
        assert p['E'] == ['E']
        assert p['F'] == ['E', 'F']

        w, p = g.dijkstra('F')
        assert w == {'A': float('inf'), 'B': float('inf'), 'C': float('inf'), 'D': float('inf'), 'E': float('inf'),
                     'F': 0}
        assert p.get('A') is None
        assert p.get('B') is None
        assert p.get('C') is None
        assert p.get('D') is None
        assert p.get('E') is None
        assert p['F'] == ['F']

    def test_graph_3(self):
        """
        Граф из "Грокаем алгоритмы. Алгоритм Дейкстры" стр.181"
        """

        def graph():
            g = Graph().create_graph(type='adjList', oriented=True)
            nodeA = Node("A")
            nodeB = Node('B')
            nodeC = Node('C')
            nodeD = Node('D')
            nodeE = Node('E')

            g.add_node(nodeA)
            g.add_node(nodeB)
            g.add_node(nodeC)
            g.add_node(nodeD)
            g.add_node(nodeE)

            g.add_edge('A', 'B', 10)
            g.add_edge('B', 'C', 20)
            g.add_edge('C', 'D', 1)
            g.add_edge('D', 'B', 1)
            g.add_edge('C', 'E', 30)
            return g

        g = graph()
        w, p = g.dijkstra('A')
        assert w == {'A': 0, 'B': 10, 'C': 30, 'D': 31, 'E': 60}
        assert p['A'] == ['A']
        assert p['B'] == ['A', 'B']
        assert p['C'] == ['A', 'B', 'C']
        assert p['D'] == ['A', 'B', 'C', 'D']
        assert p['E'] == ['A', 'B', 'C', 'E']

        w, p = g.dijkstra('B')
        assert w == {'A': float('inf'), 'B': 0, 'C': 20, 'D': 21, 'E': 50}
        assert p.get('A') is None
        assert p['B'] == ['B']
        assert p['C'] == ['B', 'C']
        assert p['D'] == ['B', 'C', 'D']
        assert p['E'] == ['B', 'C', 'E']

        w, p = g.dijkstra('C')
        assert w == {'A': float('inf'), 'B': 2, 'C': 0, 'D': 1, 'E': 30}
        assert p.get('A') is None
        assert p['B'] == ['C', 'D', 'B']
        assert p['C'] == ['C']
        assert p['D'] == ['C', 'D']
        assert p['E'] == ['C', 'E']

        w, p = g.dijkstra('D')
        assert w == {'A': float('inf'), 'B': 1, 'C': 21, 'D': 0, 'E': 51}
        assert p.get('A') is None
        assert p['B'] == ['D', 'B']
        assert p['C'] == ['D', 'B', 'C']
        assert p['D'] == ['D']
        assert p['E'] == ['D', 'B', 'C', 'E']

        w, p = g.dijkstra('E')
        assert w == {'A': float('inf'), 'B': float('inf'), 'C': float('inf'), 'D': float('inf'), 'E': 0}
        assert p.get('A') is None
        assert p.get('B') is None
        assert p.get('C') is None
        assert p.get('D') is None
        assert p['E'] == ['E']

    #
    def test_graph_4(self):
        """
        Тот же граф, добавлена вершина F и ребра C->F, F->E, D<->F
        """

        def graph():
            g = Graph().create_graph(type='adjList', oriented=True)
            nodeA = Node("A")
            nodeB = Node('B')
            nodeC = Node('C')
            nodeD = Node('D')
            nodeE = Node('E')
            nodeF = Node('F')

            g.add_node(nodeA)
            g.add_node(nodeB)
            g.add_node(nodeC)
            g.add_node(nodeD)
            g.add_node(nodeE)
            g.add_node(nodeF)

            g.add_edge('A', 'B', 10)
            g.add_edge('B', 'C', 20)
            g.add_edge('C', 'D', 1)
            g.add_edge('D', 'B', 1)
            g.add_edge('C', 'E', 30)
            g.add_edge('C', 'F', 10)
            g.add_edge('F', 'E', 5)
            g.add_edge('D', 'F', 2)
            g.add_edge('F', 'D', 2)
            return g

        g = graph()
        w, p = g.dijkstra('A')
        assert w == {'A': 0, 'B': 10, 'C': 30, 'D': 31, 'E': 38, 'F': 33}
        assert p['A'] == ['A']
        assert p['B'] == ['A', 'B']
        assert p['C'] == ['A', 'B', 'C']
        assert p['D'] == ['A', 'B', 'C', 'D']
        assert p['E'] == ['A', 'B', 'C', 'D', 'F', 'E']
        assert p['F'] == ['A', 'B', 'C', 'D', 'F']

        w, p = g.dijkstra('B')
        assert w == {'A': float('inf'), 'B': 0, 'C': 20, 'D': 21, 'E': 28, 'F': 23}
        assert p.get('A') is None
        assert p['B'] == ['B']
        assert p['C'] == ['B', 'C']
        assert p['D'] == ['B', 'C', 'D']
        assert p['E'] == ['B', 'C', 'D', 'F', 'E']
        assert p['F'] == ['B', 'C', 'D', 'F']

        w, p = g.dijkstra('C')
        assert w == {'A': float('inf'), 'B': 2, 'C': 0, 'D': 1, 'E': 8, 'F': 3}
        assert p.get('A') is None
        assert p['B'] == ['C', 'D', 'B']
        assert p['C'] == ['C']
        assert p['D'] == ['C', 'D']
        assert p['E'] == ['C', 'D', 'F', 'E']
        assert p['F'] == ['C', 'D', 'F']

        w, p = g.dijkstra('D')
        assert w == {'A': float('inf'), 'B': 1, 'C': 21, 'D': 0, 'E': 7, 'F': 2}
        assert p.get('A') is None
        assert p['B'] == ['D', 'B']
        assert p['C'] == ['D', 'B', 'C']
        assert p['D'] == ['D']
        assert p['E'] == ['D', 'F', 'E']
        assert p['F'] == ['D', 'F']

        w, p = g.dijkstra('E')
        assert w == {'A': float('inf'), 'B': float('inf'), 'C': float('inf'), 'D': float('inf'), 'E': 0,
                     'F': float('inf')}
        assert p.get('A') is None
        assert p.get('B') is None
        assert p.get('C') is None
        assert p.get('D') is None
        assert p['E'] == ['E']
        assert p.get('F') is None

        w, p = g.dijkstra('F')
        assert w == {'A': float('inf'), 'B': 3, 'C': 23, 'D': 2, 'E': 5, 'F': 0}
        assert p.get('A') is None
        assert p['B'] == ['F', 'D', 'B']
        assert p['C'] == ['F', 'D', 'B', 'C']
        assert p['D'] == ['F', 'D']
        assert p['E'] == ['F', 'E']
        assert p['F'] == ['F']

    def test_graph_5(self):
        def graph():
            g = Graph().create_graph(type='adjList', oriented=True)
            nodeA = Node("A")
            nodeB = Node('B')
            nodeC = Node('C')
            nodeD = Node('D')

            g.add_node(nodeA)
            g.add_node(nodeB)
            g.add_node(nodeC)
            g.add_node(nodeD)

            g.add_edge('A', 'B', 2)
            g.add_edge('A', 'D', 3)
            g.add_edge('A', 'C', 1)
            g.add_edge('B', 'C', 4)
            g.add_edge('C', 'A', 1)
            return g

        g = graph()
        w, p = g.dijkstra('A')
        assert w == {'A': 0, 'B': 2, 'C': 1, 'D': 3}
        assert p['A'] == ['A']
        assert p['B'] == ['A', 'B']
        assert p['C'] == ['A', 'C']
        assert p['D'] == ['A', 'D']

        w, p = g.dijkstra('B')
        assert w == {'A': 5, 'B': 0, 'C': 4, 'D': 8}
        assert p['A'] == ['B', 'C', 'A']
        assert p['B'] == ['B']
        assert p['C'] == ['B', 'C']
        assert p['D'] == ['B', 'C', 'A', 'D']

        w, p = g.dijkstra('C')
        assert w == {'A': 1, 'B': 3, 'C': 0, 'D': 4}
        assert p['A'] == ['C', 'A']
        assert p['B'] == ['C', 'A', 'B']
        assert p['C'] == ['C']
        assert p['D'] == ['C', 'A', 'D']

        w, p = g.dijkstra('D')
        assert w == {'A': float('inf'), 'B': float('inf'), 'C': float('inf'), 'D': 0}
        assert p.get('A') is None
        assert p.get('B') is None
        assert p.get('C') is None
        assert p['D'] == ['D']

    def test_graph_6(self):
        def graph():
            g = Graph().create_graph(type='adjList', oriented=True)
            nodeA = Node("A")
            nodeB = Node('B')
            nodeC = Node('C')

            g.add_node(nodeA)
            g.add_node(nodeB)
            g.add_node(nodeC)

            g.add_edge('A', 'B', 2)
            g.add_edge('B', 'B', 3)
            g.add_edge('B', 'C', 2)
            return g

        g = graph()
        w, p = g.dijkstra('A')
        assert w == {'A': 0, 'B': 2, 'C': 4}
        assert p['A'] == ['A']
        assert p['B'] == ['A', 'B']
        assert p['C'] == ['A', 'B', 'C']

        w, p = g.dijkstra('B')
        assert w == {'A': float('inf'), 'B': 0, 'C': 2}
        assert p.get('A') is None
        assert p['B'] == ['B']
        assert p['C'] == ['B', 'C']

        w, p = g.dijkstra('C')
        assert w == {'A': float('inf'), 'B': float('inf'), 'C': 0}
        assert p.get('A') is None
        assert p.get('B') is None
        assert p['C'] == ['C']

    def test_7(self):
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
        w, p = g.dijkstra('Cab')
        assert w == {'Cab': 0, 'Car': 1, 'Bar': 2, 'Cat': 1, 'Bat': 2, 'Mat': 2}
        assert p['Cab'] == ['Cab']
        assert p['Car'] == ['Cab', 'Car']
        assert p['Cat'] == ['Cab', 'Cat']
        assert p['Bar'] == ['Cab', 'Car', 'Bar']
        assert p['Bat'] == ['Cab', 'Cat', 'Bat']
        assert p['Mat'] == ['Cab', 'Cat', 'Mat']
