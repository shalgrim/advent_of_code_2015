from day18_1 import Grid


class StuckGrid(Grid):
    def __init__(self, data):
        super().__init__(data)
        self._set_corners()

    def _set_corners(self):
        top_row = self._grid[0]
        self._grid[0] = f'#{top_row[1:-1]}#'
        bottom_row = self._grid[-1]
        self._grid[-1] = f'#{bottom_row[1:-1]}#'

    def tick(self):
        super().tick()
        self._set_corners()


def make_stuck_grid(fn):
    with open(fn) as f:
        lines = [line.strip() for line in f.readlines()]

    return StuckGrid(lines)


if __name__ == '__main__':
    grid = make_stuck_grid('data/input18.txt')
    for _ in range(100):
        grid.tick()
    print(grid.number_on)
