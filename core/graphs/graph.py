from abc import ABCMeta, abstractmethod
from collections import namedtuple

from .node import AbstractNode

adj = namedtuple("adj", "name weight")


class AbstractGraph(metaclass=ABCMeta):

    def __init__(self, oriented):
        self.vertexes = set()
        self.oriented = oriented

    @abstractmethod
    def add_node(self, node) -> bool:
        pass

    @abstractmethod
    def add_edge(self, src, dst, weight=1) -> bool:
        pass

    # @abstractmethod
    # def dijkstra(self, name) -> (dict, dict):
    #     pass
    #
    # @abstractmethod
    # def bfs(self, name, target=None) -> dict:
    #     pass
    #
    # @abstractmethod
    # def dfs(self, name, target=None) -> dict:
    #     pass

    @abstractmethod
    def remove_edge(self, src, dst) -> bool:
        pass

    def check_node(self, node: AbstractNode) -> bool:
        """Check if node exists"""
        for n in self.vertexes:
            if n.name == node.name:
                return False
        return True

    def __getitem__(self, item):
        for v in self.vertexes:
            if v.name == item:
                return v
        return None

    def __delitem__(self, key):
        v = self[key]
        self.vertexes.remove(v)
