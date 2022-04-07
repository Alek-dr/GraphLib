from core.graph_impl import *


class Graph(object):

    def create_graph(self, type: str, oriented=False) -> AbstractGraph:
        if type == 'adjList':
            return AdjListGraph(oriented)
        else:
            raise Exception("Unknown type")
