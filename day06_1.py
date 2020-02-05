import re


def parse_instructions(lines):
    PATT = re.compile(r'(?P<instruction_type>^\D+)(?P<x1>\d+),(?P<y1>\d+)\D+(?P<x2>\d+),(?P<y2>\d+)')
    pass


def run_instructions(instructions):
    pass


def calc_num_lit_lights(lines):
    instructions = parse_instructions(lines)
    grid = run_instructions(instructions)
    return sum([sum(row) for row in grid])
    pass


if __name__ == '__main__':
    with open('./data/input06.txt') as f:
        lines = [line.strip() for line in f.readlines()]

    calc_num_lit_lights(lines)
