from typing import Dict, Union

from core.graphs.graph import edge
from core.graphs.walk import Walk


def update_walks(walks: Dict, e: edge, d: Union[int, str]) -> Dict:
    """
    Update walks dict
    """
    if len(walks[e.dst].edges) == 0:
        walks[e.dst].add_step(e)
        walks[e.dst] = walks[e.src] + walks[e.dst]
    else:
        path = Walk(e.dst)
        path.add_step(e)
        walks[e.dst] = walks[e.src] + path
    walks[e.dst].weight = d
    return walks
