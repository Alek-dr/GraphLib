from abc import ABC, ABCMeta, abstractmethod, abstractproperty


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


class Node(AbstractNode):

    def __init__(self, name):
        super().__init__(name)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, val):
        self._name = val


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


class AdjListGraph(AbstractGraph):

    def __init__(self, oriented=False):
        super().__init__(oriented)
        self.adj_list = {}

    def add_node(self, node: AbstractNode) -> bool:
        """
        :param node: AbstractNode implementation
        :return: true if node added sucessfully, false otherwise
        """
        if self.check_node(node):
            self.vertexes.add(node)
            self.adj_list[node.name] = []
            return True
        else:
            return False

    def add_edge(self, src, dst, weight=1) -> bool:
        if self[src] and self[dst]:
            self.adj_list[src].append((dst, weight))
            if not self.oriented:
                self.adj_list[dst].append((src, weight))
            return True
        return False


class Graph(object):

    def create_graph(self, type: str, oriented=False) -> AbstractGraph:
        if type == 'adjList':
            return AdjListGraph(oriented)
        else:
            raise Exception("Unknown type")
