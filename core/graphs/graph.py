from abc import ABCMeta, abstractmethod
from collections import namedtuple, deque
from typing import Dict, Union, Generator, Set

from core.graphs.utils import edge_name_generator

from .node import AbstractNode
from ..exceptions import GraphTypeException

edge = namedtuple("edge", "src,dst,weight,name")


class AbstractGraph(metaclass=ABCMeta):
    def __init__(self, directed: bool, weighted: bool):
        self.vertexes = set()
        self.directed = directed
        self.weighted = weighted
        self.edge_name_gen = edge_name_generator()

    @abstractmethod
    def add_node(self, node) -> None:
        pass

    @abstractmethod
    def add_edge(self, src, dst, weight: int = 1, name: str = None) -> None:
        pass

    @abstractmethod
    def remove_edge_by_name(self, name: str) -> None:
        pass

    @abstractmethod
    def remove_edge_by_vertexes(self, src, dst, name: str = None) -> None:
        pass

    def check_node(self, node: AbstractNode) -> bool:
        """Check if node exists"""
        for n in self.vertexes:
            if n.name == node.name:
                return False
        return True

    @abstractmethod
    def get_adj_edges(self, node_name: Union[str, id]) -> edge:
        pass

    @abstractmethod
    def get_edges(self) -> edge:
        pass

    def __getitem__(self, item: Union[str, int]):
        for v in self.vertexes:
            if v.name == item:
                return v
        return None

    def __delitem__(self, key):
        v = self[key]
        self.vertexes.remove(v)

    @abstractmethod
    def deg(self) -> Dict:
        """
        Returns degrees of vertexes
        """
        pass

    @abstractmethod
    def is_simple(self) -> bool:
        """
        Check if graph is simple
        """
        pass

    @property
    def n_vertex(self) -> int:
        """
        Get vertex number
        """
        return len(self.vertexes)

    @property
    def is_directed(self) -> bool:
        return self.directed

    def connected_components(
        self,
    ) -> Generator[Set[Union[str, int]], None, None]:
        """
        Return set of connected components
        """

        def _dfs(
            graph: AbstractGraph,
            origin: Union[str, int],
            target: Union[str, int] = None,
        ):
            if (target is not None) and (not graph[target]):
                raise Exception("There no target node in graph")
            if origin == target:
                return {origin}
            stack = deque()
            stack.append(edge(origin, origin, 0, None))
            visited_ = set()
            while stack:
                curr_edge = stack.pop()
                if curr_edge.dst not in visited_:
                    visited_.add(curr_edge.dst)
                    edges = [e for e in graph.get_adj_edges(curr_edge.dst)]
                    for e in reversed(edges):
                        if e.dst not in visited_:
                            stack.append(e)
                            if target is not None:
                                return visited_
                    edges.clear()
            return visited_

        visited = set()
        for v in self.vertexes:
            if v.name not in visited:
                connected = _dfs(self, v.name)
                for vertex in connected:
                    visited.add(vertex)
                yield connected

    def is_connected(self) -> bool:
        """
        True if graph is connected
        """
        # TODO: check graph is simple
        components = []
        for cc in self.connected_components():
            components.append(cc)
        if len(components) == 1:
            if len(components[0]) == self.n_vertex:
                return True
        return False

    def is_eulerian(self) -> bool:
        if self.is_directed:
            raise Exception("Not implemented for directed graph")
        else:
            if self.is_connected():
                for d in self.deg().values():
                    if d // 2 != 0:
                        return False
                return True
            else:
                return False

    def diameter(self) -> int:
        """
        Returns the diameter of connceted graph
        """
        if self.is_directed:
            raise Exception("Not implemented for directed graph")
        if self.is_connected():

            def _bfs(
                graph: AbstractGraph,
                origin: Union[str, int],
            ):
                edge_counter = 0
                visited_ = set()
                visited_.add(origin)
                queue = deque()
                e = edge(origin, origin, 0, None)
                signal_edge = edge(-1, -1, 0, None)
                queue.append(e)
                queue.appendleft(signal_edge)
                while len(queue) != 1:
                    curr_edge = queue.pop()
                    if curr_edge == signal_edge:
                        edge_counter += 1
                        queue.appendleft(signal_edge)
                        continue
                    for e in graph.get_adj_edges(curr_edge.dst):
                        if e.dst not in visited_:
                            queue.appendleft(e)
                            visited_.add(e.dst)
                return edge_counter

            diameter = 0
            for v in self.vertexes:
                d = _bfs(self, v.name)
                if d > diameter:
                    diameter = d
            return diameter
        else:
            raise GraphTypeException(
                "Cannot calculate diameter for not connected graph"
            )
