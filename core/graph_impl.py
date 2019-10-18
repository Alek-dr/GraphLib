from .abc_structures import *


class Node(AbstractNode):

    def __init__(self, name):
        super().__init__(name)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, val):
        self._name = val


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
        return False

    def add_edge(self, src, dst, weight=1) -> bool:
        """
        :param src: name or id of source node
        :param dst: name or id of dst node
        :param weight: weight of edge
        :return: true if edge added sucessfully, false otherwise
        """
        if self[src] and self[dst]:
            self.adj_list[src].append(adj(dst, weight))
            if not self.oriented:
                self.adj_list[dst].append(adj(src, weight))
            return True
        return False

    def dijkstra(self, origin) -> (dict, dict):
        """
        :param origin: name or id of origin node
        :return: dict of shortest paths weights, dict of paths
        """

        def lowest_cost():
            # find any not visited adjacent node
            nearest = None
            for node in self.adj_list[current_node]:
                if node.name in unvisited:
                    nearest = node.name
                    break
            if nearest is None:
                return nearest

            for node in self.adj_list[current_node]:
                if node.name in unvisited:
                    d = node.weight + costs[current_node]
                    if costs[node.name] > d:
                        costs[node.name] = d
                        paths[node.name] = paths[current_node] + [node.name]
                    if d < costs[nearest]:
                        nearest = node.name
            return nearest

        if self[origin]:
            unvisited = [v.name for v in self.vertexes if v.name != origin]
            costs = {v.name: float("inf") for v in self.vertexes}
            costs[origin] = 0
            paths = {}
            paths[origin] = [origin]
            current_node = origin
            while unvisited:
                nearest = lowest_cost()
                if nearest and (nearest in unvisited):
                    unvisited.remove(nearest)
                    current_node = nearest
                else:
                    current_node = origin
                    final = True
                    for node in self.adj_list[origin]:
                        if node.name in unvisited:
                            final = False
                            break
                    if final:
                        break
            return costs, paths
        else:
            raise Exception("There no such node")
