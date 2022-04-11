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

    def add_step(self, v, edge, w) -> None:
        self.vertexes.append(v)
        if edge is not None:
            self.edges.append(edge)
        self.path_weight += w
        return
