from typing import Union, Dict

from core.algorithms.utils import has_multiple_paths
from core.graphs.graph import AbstractGraph, adj
from core.graphs.node import AbstractNode


class AdjListGraph(AbstractGraph):
    """
    Graph implementation as adjacency list
    """

    def __init__(self, oriented=False):
        super().__init__(oriented)
        self.adj_list = {}

    def __delitem__(self, key):
        super().__delitem__(key)
        del self.adj_list[key]
        for childs in self.adj_list.values():
            for node in childs:
                if node.name == key:
                    childs.remove(node)
        # [childs.remove(node) for childs in self.adj_list.values() for node in childs if node.name == key]

    def remove_edge(self, src, dst) -> bool:
        """
       :param src: name or id of source node
       :param dst: name or id of dst node
       :return: true if edge removed sucessfully, false otherwise
       """
        if self[src] and self[dst]:
            childs = self.adj_list[src]
            for node in childs:
                if node.name == dst:
                    childs.remove(node)
                    break
            if not self.oriented:
                childs = self.adj_list[dst]
                for node in childs:
                    if node.name == src:
                        childs.remove(node)
                        break
            return True
        return False

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

    def get_adj_nodes(self, node_name: Union[str, id]) -> adj:
        for item in self.adj_list[node_name]:
            yield item

    def _get_paths(self, child, node, paths) -> Dict:
        """
        :param child: child node name
        :param node: current node name
        :param paths: dict of paths
        :return: paths
        """
        if child.name not in paths:
            if has_multiple_paths(paths[node]):
                # If there are multiple ways to node
                paths[child.name] = paths[node][0] + [child.name]
                for i in range(1, len(paths[node])):
                    paths[child.name] = [paths[child.name], paths[node][i] + [child.name]]
            else:
                paths[child.name] = paths[node] + [child.name]
        else:
            m_node_paths, m_child_paths = has_multiple_paths(paths[node]), has_multiple_paths(
                paths[child.name])
            if not (m_node_paths + m_child_paths):
                # There are only one way to child and one way to node
                paths[child.name] = [paths[child.name], paths[node] + [child.name]]
            elif m_node_paths and (not m_child_paths):
                # Multiple ways to node and only one to child
                for i in range(len(paths[child.name])):
                    paths[child.name][i] = paths[child.name][i] + paths[node]
            elif m_child_paths and (not m_node_paths):
                # Multiple ways to child and only one to node
                paths[child.name].append(paths[node] + [child.name])
            else:
                # Multiple ways for child and node
                for i in range(len(paths[node])):
                    path = paths[node][i] + [child.name]
                    if path not in paths[child.name]:
                        paths[child.name].append(path)
        return paths
