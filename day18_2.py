from day18_1 import Grid


class StuckGrid(Grid):
    def __init__(self, data):
        super().__init__(data)
        top_row = self._grid[0]
        self._grid[0] = f'#{top_row[1:-1]}#'
        bottom_row = self._grid[-1]
        self._grid[0] = f'#{bottom_row[1:-1]}#'


def make_stuck_grid(fn):
    with open(fn) as f:
        lines = [line.strip() for line in f.readlines()]

    return StuckGrid(lines)
