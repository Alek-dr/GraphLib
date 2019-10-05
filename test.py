from graph import Graph, Node

if __name__ == '__main__':
    g = Graph().create_graph(type='adjList')
    nodeA = Node("A")
    nodeB = Node('B')
    g.add_node(nodeA)
    g.add_node(nodeB)
    g.add_edge(src='A', dst='B')
