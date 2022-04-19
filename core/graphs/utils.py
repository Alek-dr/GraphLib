import string


def edge_name_generator():
    i = 0
    while True:
        for char in string.ascii_lowercase:
            yield char if i == 0 else f"{char}{i}"
        i += 1
