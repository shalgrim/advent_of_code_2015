from collections import defaultdict
from itertools import combinations


def main(containers):
    solutions = defaultdict(list)
    for r in range(1, len(containers) + 1):
        for combo in combinations(containers, r):
            if sum(combo) == 150:
                solutions[len(combo)].append(combo)

    fewest_containers = min(solutions)
    return len(solutions[fewest_containers])


if __name__ == '__main__':
    with open('data/input17.txt') as f:
        containers = [int(line.strip()) for line in f.readlines()]

    print(main(containers))
