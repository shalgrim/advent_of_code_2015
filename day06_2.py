from copy import copy
from day06_1 import calc_num_lit_lights


def run_brightness(instructions):
    row = [0] * 1000
    grid = []
    for i in range(1000):
        grid.append(copy(row))

    for inst, upper_left, lower_right in instructions:
        if 'toggle' in inst:
            for x in range(upper_left[0], lower_right[0] + 1):
                for y in range(upper_left[1], lower_right[1] + 1):
                    grid[x][y] += 2
        elif 'off' in inst:
            for x in range(upper_left[0], lower_right[0] + 1):
                for y in range(upper_left[1], lower_right[1] + 1):
                    grid[x][y] = max(0, grid[x][y] - 1)
        elif 'on' in inst:
            for x in range(upper_left[0], lower_right[0] + 1):
                for y in range(upper_left[1], lower_right[1] + 1):
                    grid[x][y] += 1

    return grid


if __name__ == '__main__':
    with open('./data/input06.txt') as f:
        lines = [line.strip() for line in f.readlines()]

    print(calc_num_lit_lights(lines, run_brightness))
