def dimensions_from_lines(lines):
    dimensions = []

    for line in lines:
        dimensions.append([int(d) for d in line.split('x')])

    return dimensions


def calc_paper_needed(dimensions):
    l, w, h = dimensions
    p1 = l*w
    p2 = l*h
    p3 = w*h

    smallest = min([p1, p2, p3])

    return p1*2 + p2*2 + p3*2 + smallest


def main(dimension_lines):
    dimensions = dimensions_from_lines(dimension_lines)
    paper_needed = [calc_paper_needed(d) for d in dimensions]
    return sum(paper_needed)

if __name__ == '__main__':
    with open('data/input02.txt') as f:
        lines = [line.strip() for line in f.readlines()]
    print(main(lines))
