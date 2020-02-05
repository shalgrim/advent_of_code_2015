import re
from collections import Counter

PATT = re.compile(r'(.)\1')


def is_nice(s):
    if any([verboten in s for verboten in ('ab', 'cd', 'pq', 'xy')]):
        return False

    c = Counter(s)
    if sum([c.get(vowel, 0) for vowel in ('a', 'e', 'i', 'o', 'u')]) < 3:
        return False

    if not PATT.search(s):
        return False

    return True


if __name__ == '__main__':
    with open('./data/input05.txt') as f:
        strings = [line.strip() for line in f.readlines()]

    print(len([s for s in strings if is_nice(s)]))
