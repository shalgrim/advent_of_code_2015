from day03_1 import visit_houses


def count_houses_with_robo(steps):
    santa = ''
    robo = ''
    for i, step in enumerate(steps):
        if i % 2 == 0:
            santa += step
        else:
            robo += step

    santa_visited = visit_houses(santa)
    robo_visited = visit_houses(robo)
    all_visited = santa_visited.union(robo_visited)
    return len(all_visited)


if __name__ == '__main__':
    with open('data/input03.txt') as f:
        steps = f.read()

    print(count_houses_with_robo(steps))
