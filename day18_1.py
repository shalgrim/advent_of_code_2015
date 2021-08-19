class Grid:
    def __init__(self, data):
        self._grid = data

    def __str__(self):
        return '\n'.join(self._grid)

    def get_neighbors(self, x, y):
        height = len(self._grid)
        width = len(self._grid[0])
        neighbors = []

        # previous row
        if y != 0:
            if x != 0:
                neighbors.append((x - 1, y - 1))
            neighbors.append((x, y - 1))
            if x + 1 < width:
                neighbors.append((x + 1, y - 1))

        # current row
        if x != 0:
            neighbors.append((x - 1, y))
        if x + 1 < width:
            neighbors.append((x + 1, y))

        # next row
        if y + 1 < height:
            if x != 0:
                neighbors.append((x - 1, y + 1))
            neighbors.append((x, y + 1))
            if x + 1 < width:
                neighbors.append((x + 1, y + 1))

        return neighbors

    def tick(self):
        new_grid = []
        for y, row in enumerate(self._grid):
            new_row = ''
            for x, cell in enumerate(row):
                neighbor_coords = self.get_neighbors(x, y)
                neighbor_values = [self._grid[y][x] for x, y in neighbor_coords]
                num_on = neighbor_values.count('#')

                if cell == '#':
                    if num_on in [2, 3]:
                        new_row += '#'
                    else:
                        new_row += '.'
                else:
                    if num_on == 3:
                        new_row += '#'
                    else:
                        new_row += '.'

            new_grid.append(new_row)

        self._grid = new_grid

    @property
    def number_on(self):
        return sum(row.count('#') for row in self._grid)


def make_grid(fn):
    with open(fn) as f:
        lines = [line.strip() for line in f.readlines()]

    return Grid(lines)


if __name__ == '__main__':
    grid = make_grid('data/input18.txt')
    for _ in range(100):
        grid.tick()
    print(grid.number_on)
