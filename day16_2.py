from day16_1 import message, parse_sues


def matches(sue, message):
    for k, v in sue.items():
        if k in ['cats', 'trees']:
            if message[k] >= v:
                return False
        elif k in ('pomeranians', 'goldfish'):
            if message[k] <= v:
                return False
        elif message[k] != v:
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
