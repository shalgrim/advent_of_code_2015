from collections import defaultdict
from itertools import permutations


def build_happiness_values(lines):
    individual_happiness_values = defaultdict(dict)
    for line in lines:
        p1 = line.split()[0]
        p2 = line.split()[-1][:-1]
        value = int(line.split()[3])
        if line.split()[2] == 'lose':
            value = -value

        individual_happiness_values[p1][p2] = value

    return individual_happiness_values


def calculate_happiness(individual_happiness_values, perm):
    answer = 0
    for i, person in enumerate(perm):
        prev_person = perm[i-1]
        answer += individual_happiness_values[person][prev_person]
        answer += individual_happiness_values[prev_person][person]

    return answer


if __name__ == '__main__':
    with open('data/input13.txt') as f:
        lines = f.readlines()

    individual_happiness_values = build_happiness_values(lines)
    attendees = list(individual_happiness_values.keys())
    happiness_values = [calculate_happiness(individual_happiness_values, perm) for perm in permutations(attendees)]
    print(max(happiness_values))
