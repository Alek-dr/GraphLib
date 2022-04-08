from typing import List


def has_multiple_paths(item: List) -> bool:
    return (len(item) > 1) and (isinstance(item[1], list))
