from typing import Union

from core.graphs.graph import edge


class Walk:
    def __init__(self, dst_vertex: Union[str, int]):
        self.dst_vertex = dst_vertex
        self.vertexes = []
        self.edges = []
        self.weight = 0

    @property
    def initial_vertex(self):
        if len(self.vertexes):
            return self.vertexes[0]
        return None

    @property
    def final_vertex(self):
        if len(self.vertexes):
            return self.vertexes[-1]
        return None

    def __add__(self, walk):
        walk.vertexes = self.vertexes.copy() + [walk.dst_vertex]
        walk.edges = self.edges + walk.edges
        walk.weight += self.weight
        return walk

    def __str__(self):
        s = ""
        n = len(self.vertexes) - 1
        for i, v in enumerate(self.vertexes, 0):
            if i == n:
                s += f"{v}"
            else:
                edge = self.edges[i] if len(self.edges) else "()"
                s += f"{v} -> ({edge}) -> "
        if s == "":
            s += f"-x- {self.dst_vertex}"
        return s

    def add_step(self, edg: edge):
        if edg is not None:
            self.vertexes.append(edg.dst)
            self.weight += edg.weight
            if edg.name is not None:
                self.edges.append(edg.name)
        return

    def length(self) -> int:
        """
        The number of edges in a walk is called its length
        """
        return len(self.edges)

    def is_trail(self) -> bool:
        """
        A walk in which all the edges are distinct is a trail
        """
        return len(self.edges) == len(set(self.edges))

    def is_path(self) -> bool:
        """
        If walk is train and all vertices are distinct then the trail is a path
        """
        return self.is_trail() and (len(self.vertexes) == len(set(self.vertexes)))

    def is_closed(self) -> bool:
        """
        Train is closed if initial vertex = final vertex
        """
        return self.initial_vertex == self.final_vertex
