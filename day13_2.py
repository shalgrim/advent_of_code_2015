from itertools import permutations

from day13_1 import build_happiness_values, calculate_happiness

if __name__ == '__main__':
    with open('data/input13.txt') as f:
        lines = f.readlines()

    individual_happiness_values = build_happiness_values(lines)
    attendees = list(individual_happiness_values.keys())
    attendees.append('me')

    for attendee in attendees:
        individual_happiness_values['me'][attendee] = 0
        individual_happiness_values[attendee]['me'] = 0

    happiness_values = [calculate_happiness(individual_happiness_values, perm) for perm in permutations(attendees)]
    print(max(happiness_values))
