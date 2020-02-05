import re

PATT1 = re.compile(r'(..).*\1')
PATT2 = re.compile(r'(.).\1')


def is_nice(s):
    if not PATT1.search(s) or not PATT2.search(s):
        return False

    return True


if __name__ == '__main__':
    with open('./data/input05.txt') as f:
        strings = [line.strip() for line in f.readlines()]

    print(len([s for s in strings if is_nice(s)]))
