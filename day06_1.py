import re
from copy import copy

PATT = re.compile(
    r'(?P<instruction_type>^\D+)(?P<x1>\d+),(?P<y1>\d+)\D+(?P<x2>\d+),(?P<y2>\d+)'
)


def parse_instructions(lines):
    instructions = []

    for line in lines:
        match = PATT.search(line)
        it = match.group('instruction_type').strip()
        upper_left = (int(match.group('x1')), int(match.group('y1')))
        lower_right = (int(match.group('x2')), int(match.group('y2')))
        instructions.append((it, upper_left, lower_right))

    return instructions


def run_instructions(instructions):
    row = [0] * 1000
    grid = []
    for i in range(1000):
        grid.append(copy(row))

    for inst, upper_left, lower_right in instructions:
        if 'toggle' in inst:
            for x in range(upper_left[0], lower_right[0] + 1):
                for y in range(upper_left[1], lower_right[1] + 1):
                    grid[x][y] = 0 if grid[x][y] else 1
        else:
            val = 0 if 'off' in inst else 1

            for x in range(upper_left[0], lower_right[0] + 1):
                for y in range(upper_left[1], lower_right[1] + 1):
                    grid[x][y] = val

    return grid


def sum_lit_lights(grid):
    return sum([sum(row) for row in grid])


def calc_num_lit_lights(lines, run_algo=run_instructions):
    instructions = parse_instructions(lines)
    grid = run_algo(instructions)
    return sum_lit_lights(grid)


if __name__ == '__main__':
    with open('./data/input06.txt') as f:
        lines = [line.strip() for line in f.readlines()]

    print(calc_num_lit_lights(lines))
