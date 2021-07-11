from collections import defaultdict
from typing import List

message = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1,
}


def parse_sues(lines: List[str]):
    sues = defaultdict(dict)
    for line in lines:
        sue_id = int(line.split(':')[0].split()[1])
        stats = line.split(':', 1)[1]

        for stat in stats.split(','):
            stat_name = stat.strip().split(':')[0]
            stat_value = int(stat.strip().split(':')[1])
            sues[sue_id][stat_name] = stat_value

    return sues


def matches(sue, message):
    for k, v in sue.items():
        if message[k] != v:
            return False
    return True


def main(lines):
    sues = parse_sues(lines)
    for sue_id, sue in sues.items():
        if matches(sue, message):
            return sue_id
    return 0


if __name__ == '__main__':
    with open('data/input16.txt') as f:
        lines = [line.strip() for line in f.readlines()]
    print(main(lines))
