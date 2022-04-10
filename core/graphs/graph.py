from abc import ABCMeta, abstractmethod
from collections import namedtuple
from typing import Dict, Union

from .node import AbstractNode

edge = namedtuple("edge", "src,dst,weight")


class AbstractGraph(metaclass=ABCMeta):
    def __init__(self, directed: bool, weighted: bool):
        self.vertexes = set()
        self.directed = directed
        self.weighted = weighted

    @abstractmethod
    def add_node(self, node) -> bool:
        pass

    @abstractmethod
    def add_edge(self, src, dst, weight=1) -> bool:
        pass

    @abstractmethod
    def _get_paths(self, child, node, paths):
        """
        :param child: child node name
        :param node: current node name
        :param paths: dict of paths
        :return: paths
        """
        pass

    @abstractmethod
    def remove_edge(self, src, dst) -> bool:
        pass

    def check_node(self, node: AbstractNode) -> bool:
        """Check if node exists"""
        for n in self.vertexes:
            if n.name == node.name:
                return False
        return True

    @abstractmethod
    def get_adj_nodes(self, node_name: Union[str, id]) -> edge:
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
