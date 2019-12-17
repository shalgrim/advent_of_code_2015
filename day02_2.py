from day02_1 import dimensions_from_lines


def calc_ribbon_needed(dimension):
    l, w, h = dimension
    p1 = 2*(l+w)
    p2 = 2*(l+h)
    p3 = 2*(w+h)

    wrap_ribbon = min([p1, p2, p3])
    bow_ribbon = l * w * h
    return wrap_ribbon + bow_ribbon


def main(dimension_lines):
    dimensions = dimensions_from_lines(dimension_lines)
    ribbon_needed = [calc_ribbon_needed(d) for d in dimensions]
    return sum(ribbon_needed)


if __name__ == '__main__':
    with open('data/input02.txt') as f:
        lines = [line.strip() for line in f.readlines()]
    print(main(lines))
