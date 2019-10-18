from abc import ABC, ABCMeta, abstractmethod
from collections import namedtuple

adj = namedtuple("adj", "name weight")


class AbstractNode(ABC):

    def __init__(self, name):
        self._name = name

    @property
    @abstractmethod
    def name(self):
        """
        :return: unique name or id of node
        """

    @name.setter
    @abstractmethod
    def name(self, val):
        """
        :param val: str or int
        """


class AbstractGraph(metaclass=ABCMeta):

    def __init__(self, oriented):
        self.vertexes = set()
        self.oriented = oriented

    @abstractmethod
    def add_node(self, node):
        pass

    @abstractmethod
    def add_edge(self, src, dst, weight=1):
        pass

    @abstractmethod
    def dijkstra(self, name):
        pass

    def check_node(self, node: AbstractNode) -> bool:
        for n in self.vertexes:
            if n.name == node.name:
                return False
        return True

    def __getitem__(self, item):
        for v in self.vertexes:
            if v.name == item:
                return v
        return None
