from itertools import combinations


def main(containers):
    answer = 0
    for r in range(1, len(containers) + 1):
        for combo in combinations(containers, r):
            if sum(combo) == 150:
                answer += 1
    return answer


if __name__ == '__main__':
    with open('data/input17.txt') as f:
        containers = [int(line.strip()) for line in f.readlines()]

    print(main(containers))
