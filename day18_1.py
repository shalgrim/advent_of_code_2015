class Grid:
    def __init__(self, data):
        pass


def make_grid(fn):
    with open(fn) as f:
        lines = [line.strip() for line in f.readlines()]

    return Grid(lines)
