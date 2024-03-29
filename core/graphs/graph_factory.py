from enum import Enum

from core.graphs.adjacency_list import AdjListGraph
from core.graphs.graph import AbstractGraph


class GraphType(Enum):
    AdjList = 0


def create_graph(
    graph_type: GraphType = GraphType.AdjList,
    directed: bool = False,
    weighted: bool = False,
) -> AbstractGraph:
    graphs = {GraphType.AdjList: AdjListGraph}
    return graphs[graph_type](directed, weighted)
