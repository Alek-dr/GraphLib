from core.graphs.graph import edge


class Path:
    def __init__(self, dst_vertex):
        self.dst_vertex = dst_vertex
        self.vertexes = []
        self.edges = []
        self.path_weight = 0

    def __add__(self, path):
        path.vertexes = self.vertexes.copy() + [path.dst_vertex]
        path.edges = self.edges + path.edges
        path.path_weight += self.path_weight
        return path

    def __str__(self):
        s = ""
        n = len(self.vertexes) - 1
        for i, v in enumerate(self.vertexes, 0):
            if i == n:
                s += f"{v}"
            else:
                edge = self.edges[i] if len(self.edges) else "()"
                s += f"{v} -> ({edge}) -> "
        return s

    def add_step(self, edg: edge):
        if edg is not None:
            self.vertexes.append(edg.dst)
            self.path_weight += edg.weight
            if edg.name is not None:
                self.edges.append(edg.name)
        return
