from abc import ABC, abstractmethod


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
