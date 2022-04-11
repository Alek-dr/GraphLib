import string
from typing import List


def has_multiple_paths(item: List) -> bool:
    return (len(item) > 1) and (isinstance(item[1], list))


def edge_name_generator():
    i = 0
    while True:
        for char in string.ascii_lowercase:
            yield char if i == 0 else f"{char}{i}"
        i += 1


if __name__ == '__main__':
    for char in edge_name_generator():
        print(char)
