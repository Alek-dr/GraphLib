from typing import Dict, Union

from core.algorithms.utils import has_multiple_paths
from core.exceptions import EdgeAddError, EdgeRemoveError
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

    def remove_edge_by_name(self, name: str) -> None:
        found = False
        for vertex_edges in self.adj_list.values():
            if found:
                break
            for edge_ in vertex_edges:
                if edge_.name == name:
                    self.adj_list[edge_.src].remove(edge_)
                    if not self.directed:
                        self.adj_list[edge_.dst].remove(edge(edge_.dst, edge_.src, edge_.weight, edge_.name))
                    found = True
                    break
        if not found:
            raise EdgeRemoveError(f"Cannot find edge with name: {name}")
        return

    def remove_edge_by_vertexes(self, src, dst, name: str = None) -> None:
        """
        :param name: edge name
        :param src: name or id of source node
        :param dst: name or id of dst node
        """
        if self[src] and self[dst]:
            childs = self.adj_list[src]
            if name is not None:
                for edge_ in childs:
                    if edge_.name == name:
                        self.adj_list[src].remove(edge_)
                        if not self.directed:
                            self.adj_list[dst].remove(edge(dst, src, edge_.weight, name))
                        break
            else:
                candidates = [node for node in childs if node.dst == dst]
                if len(candidates) > 1:
                    raise EdgeRemoveError(f"Found more then 1 edge: {candidates}")
                elif len(candidates) == 0:
                    raise EdgeRemoveError(f"Cannot find edge with src = {src}, dst = {dst}")
                else:
                    edge_ = candidates[0]
                    self.adj_list[src].remove(edge_)
                    if not self.directed:
                        self.adj_list[dst].remove(edge(dst, src, edge_.weight, edge_.name))

    def add_node(self, node: AbstractNode) -> None:
        """
        :param node: AbstractNode implementation
        :return: true if node added sucessfully, false otherwise
        """
        if self.check_node(node):
            self.vertexes.add(node)
            self.adj_list[node.name] = []
        return

    def add_edge(self, src, dst, weight: int = 1, name: str = None) -> None:
        """
        :param name: edge name
        :param src: name or id of source node
        :param dst: name or id of dst node
        :param weight: weight of edge
        """
        if self[src] and self[dst]:
            if not self._edge_exists(src, dst, weight, name):
                if name is None:
                    name = next(self.edge_name_gen)
                self.adj_list[src].append(edge(src, dst, weight, name))
                if not self.directed:
                    self.adj_list[dst].append(edge(dst, src, weight, name))
            else:
                raise EdgeAddError(f"{edge(src, dst, weight, name)} already exists")
        return

    def get_adj_nodes(self, node_name: Union[str, id]) -> edge:
        for item in self.adj_list[node_name]:
            yield item

    def get_edges(self) -> edge:
        if not self.directed:
            same_edges = set()
            for vertex_edges in self.adj_list.values():
                for edge_ in vertex_edges:
                    if edge_.name not in same_edges:
                        yield edge_
                    same_edges.add(edge_.name)
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

    def _edge_exists(self, src, dst, weight: int, name: str = None) -> bool:
        for edge in self.adj_list[src]:
            if (edge.src == src) and (edge.dst == dst) and (edge.weight == weight) and (edge.name == name):
                return True
        return False
