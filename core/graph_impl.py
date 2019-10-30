from .abc_structures import *
from collections import deque


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

    def bfs(self, origin, target=None) -> dict:
        """
        :param origin: name or id of origin node
        :param target: node to find path. If target is None all paths will be returned
        :return: shortest path to target or all possible paths to all nodes if target is not specified
        """

        def multiple_paths(item):
            if (len(item) > 1) and (isinstance(item[1], list)):
                return True
            return False

        if (target is not None) and (not self[target]):
            raise Exception("There no target node in graph")
        visited = set()
        visited.add(origin)
        queue = deque()
        queue.append(origin)
        paths = {origin: [origin]}
        while queue:
            node = queue.pop()
            for child in self.adj_list[node]:
                if child.name not in paths:
                    if multiple_paths(paths[node]):
                        # If there are multiple ways to node
                        paths[child.name] = paths[node][0] + [child.name]
                        for i in range(1, len(paths[node])):
                            paths[child.name] = [paths[child.name], paths[node][i] + [child.name]]
                    else:
                        paths[child.name] = paths[node] + [child.name]
                else:
                    m_node_paths, m_child_paths = multiple_paths(paths[node]), multiple_paths(paths[child.name])
                    if (m_node_paths + m_child_paths) == False:
                        # There are only one way to child and one way to node
                        paths[child.name] = [paths[child.name], paths[node] + [child.name]]
                    elif m_node_paths and (not m_child_paths):
                        # Multiple ways to node and only one to child
                        for i in range(len(paths[child.name])):
                            paths[child.name][i] = paths[child.name][i] + paths[node]
                    elif m_child_paths and (not m_node_paths):
                        # Multiple ways to chile and only one to node
                        paths[child.name].append(paths[node] + [child.name])
                    else:
                        # Multiple ways for child and node
                        for i in range(len(paths[node])):
                            path = paths[node][i] + [child.name]
                            if path not in paths[child.name]:
                                paths[child.name].append(path)
                if (target is not None) and (child.name == target):
                    if multiple_paths(paths[target]):
                        return {target: min(paths[target], key=lambda x: len(x))}
                    else:
                        return {target: paths[target]}
                visited.add(child.name)
                queue.appendleft(child.name)
        return paths

    def dijkstra(self, origin) -> (dict, dict):
        """
        :param origin: name or id of origin node
        :return: dict of shortest paths weights, dict of paths
        """
        if not self[origin]:
            raise Exception("There no such node")
        unvisited = [v.name for v in self.vertexes if v.name != origin]
        costs = {v.name: float("inf") for v in self.vertexes}
        costs[origin] = 0
        paths = {}
        paths[origin] = [origin]
        current_node = origin
        while unvisited:
            for node in self.adj_list[current_node]:
                if node.name in unvisited:
                    d = node.weight + costs[current_node]
                    if costs[node.name] > d:
                        costs[node.name] = d
                        paths[node.name] = paths[current_node] + [node.name]
            nearest = unvisited[0]
            min_w = costs[nearest]
            for node in unvisited:
                if costs[node] < min_w:
                    min_w = costs[node]
                    nearest = node
            unvisited.remove(nearest)
            current_node = nearest
        return costs, paths
