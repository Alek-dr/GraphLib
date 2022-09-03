from typing import Dict, Union

from core.graphs.gpath import GPath
from core.graphs.graph import edge


def update_path(paths: Dict, e: edge, d: Union[int, str]) -> Dict:
    """
    Update path dict
    """
    if len(paths[e.dst].edges) == 0:
        paths[e.dst].add_step(e)
        paths[e.dst] = paths[e.src] + paths[e.dst]
    else:
        path = GPath(e.dst)
        path.add_step(e)
        paths[e.dst] = paths[e.src] + path
    paths[e.dst].path_weight = d
    return paths
