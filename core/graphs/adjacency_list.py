from typing import Dict, Union

from core.algorithms.utils import has_multiple_paths
from core.graphs.graph import AbstractGraph, edge
from core.graphs.node import AbstractNode


class AdjListGraph(AbstractGraph):
    """
    Graph implementation as adjacency list
    """

    def __init__(self, directed: bool = False, weighted: bool = False):
        super().__init__(directed, weighted)
        self.adj_list = {}

    def __delitem__(self, key):
        super().__delitem__(key)
        del self.adj_list[key]
        for childs in self.adj_list.values():
            for node in childs:
                if node.name == key:
                    childs.remove(node)

    def deg(self) -> Dict:
        degrees = {}
        if not self.directed:
            degrees = {
                node_name: len(adj_list)
                for node_name, adj_list in self.adj_list.items()
            }
        else:
            for node_name in self.adj_list.keys():
                degrees[node_name] = dict(in_degree=0, out_degree=0)
            for node_name, adj_list in self.adj_list.items():
                degrees[node_name]["out_degree"] = len(adj_list)
                for item in adj_list:
                    degrees[item.dst]["in_degree"] += 1
        return degrees

    def is_simple(self) -> bool:
        if self.directed or self.weighted:
            return False
        for node_name, adj_list in self.adj_list.items():
            names = [item.dst for item in adj_list]
            if len(names) != len(set(names)):
                # multiple edges
                return False
            for name in names:
                if name == node_name:
                    # loop
                    return False
        return True

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
            if not self.directed:
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
            self.adj_list[src].append(edge(src, dst, weight))
            if not self.directed:
                self.adj_list[dst].append(edge(dst, src, weight))
            return True
        return False

    def get_adj_nodes(self, node_name: Union[str, id]) -> edge:
        for item in self.adj_list[node_name]:
            yield item

    def get_edges(self) -> edge:
        if self.directed == False:
            same_edges = set()
            for vertex_edges in self.adj_list.values():
                for item in vertex_edges:
                    if item not in same_edges:
                        yield item
                    same_edges.add(edge(item.dst, item.src, item.weight))
        else:
            for vertex_edges in self.adj_list.values():
                for item in vertex_edges:
                    yield item

    def _get_paths(self, child, node, paths) -> Dict:
        """
        :param child: child node name
        :param node: current node name
        :param paths: dict of paths
        :return: paths
        """
        if child.dst not in paths:
            if has_multiple_paths(paths[node]):
                # If there are multiple ways to node
                paths[child.dst] = paths[node][0] + [child.dst]
                for i in range(1, len(paths[node])):
                    paths[child.dst] = [
                        paths[child.dst],
                        paths[node][i] + [child.dst],
                    ]
            else:
                paths[child.dst] = paths[node] + [child.dst]
        else:
            m_node_paths, m_child_paths = has_multiple_paths(
                paths[node]
            ), has_multiple_paths(paths[child.dst])
            if not (m_node_paths + m_child_paths):
                # There are only one way to child and one way to node
                paths[child.dst] = [paths[child.dst], paths[node] + [child.dst]]
            elif m_node_paths and (not m_child_paths):
                # Multiple ways to node and only one to child
                for i in range(len(paths[child.dst])):
                    paths[child.dst][i] = paths[child.dst][i] + paths[node]
            elif m_child_paths and (not m_node_paths):
                # Multiple ways to child and only one to node
                paths[child.dst].append(paths[node] + [child.dst])
            else:
                # Multiple ways for child and node
                for i in range(len(paths[node])):
                    path = paths[node][i] + [child.dst]
                    if path not in paths[child.dst]:
                        paths[child.dst].append(path)
        return paths
