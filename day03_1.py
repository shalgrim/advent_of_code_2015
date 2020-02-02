def visit_houses(steps):
    x = 0
    y = 0
    visited = set([(x, y)])

    for step in steps:
        if step == '^':
            y -= 1
        elif step == 'v':
            y += 1
        elif step == '>':
            x += 1
        elif step == '<':
            x -= 1
        else:
            continue

        visited.add((x, y))

    return visited


def count_houses_visited(steps):
    return len(visit_houses(steps))


if __name__ == '__main__':
    with open('data/input03.txt') as f:
        steps = f.read()

    print(count_houses_visited(steps))

