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
