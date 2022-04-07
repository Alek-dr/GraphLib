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
