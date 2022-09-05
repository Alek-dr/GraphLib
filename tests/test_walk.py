from core.graphs.walk import Walk


def test_is_trail_1():
    w = Walk("d")
    w.vertexes = ["a", "b", "c", "d"]
    w.edges = [1, 2, 3]
    w.weight = 3
    assert w.is_trail()


def test_is_path_1():
    w = Walk("d")
    w.vertexes = ["a", "b", "c", "d"]
    w.edges = [1, 2, 3]
    w.weight = 3
    assert w.is_path()


def test_is_not_path_1():
    w = Walk("d")
    w.vertexes = ["a", "b", "c", "d", "a"]
    w.edges = [1, 2, 3]
    w.weight = 3
    assert not w.is_path()


def test_is_trail_2():
    w = Walk("e")
    w.vertexes = ["a", "b", "c", "d", "e"]
    w.edges = [1, 2, 3, 4]
    w.weight = 3
    assert w.is_trail()


def test_is_path_2():
    w = Walk("e")
    w.vertexes = ["a", "b", "c", "d", "e"]
    w.edges = [1, 2, 3, 4]
    w.weight = 3
    assert w.is_path()


def test_is_not_path_2():
    w = Walk("e")
    w.vertexes = ["a", "b", "c", "d", "e"]
    w.edges = [1, 2, 3, 4, 3]
    w.weight = 3
    assert not w.is_path()


def test_is_not_trail_1():
    w = Walk("d")
    w.vertexes = ["a", "b", "c", "d"]
    w.edges = [1, 2, 3, 1]
    w.weight = 3
    assert not w.is_trail()


def test_is_not_trail_2():
    w = Walk("d")
    w.vertexes = ["a", "b", "c", "d"]
    w.edges = [1, 2, 3, 3]
    w.weight = 3
    assert not w.is_trail()
