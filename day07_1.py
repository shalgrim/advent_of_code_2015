from collections import defaultdict


def intize(param):
    try:
        return int(param)
    except ValueError:
        return param


def process_instructions(instructions):
    wires = defaultdict(lambda: 0)
    for lhs, rhs in instructions:
        if 'AND' in lhs:
            in1, in2 = [intize(param.strip()) for param in lhs.split(' AND ')]
            raw_answer = (in1 if isinstance(in1, int) else wires[in1]) & (in2 if isinstance(in2, int) else wires[in2])
        elif 'OR' in lhs:
            in1, in2 = [intize(param.strip()) for param in lhs.split(' OR ')]
            raw_answer = (in1 if isinstance(in1, int) else wires[in1]) | (in2 if isinstance(in2, int) else wires[in2])
        elif 'LSHIFT' in lhs:
            in1, in2 = [intize(param.strip()) for param in lhs.split(' LSHIFT ')]
            if isinstance(in1, int):
                raw_answer = in1 << in2
            else:
                raw_answer = wires[in1] << in2
        elif 'RSHIFT' in lhs:
            in1, in2 = [intize(param.strip()) for param in lhs.split(' RSHIFT ')]
            if isinstance(in1, int):
                raw_answer = in1 >> in2
            else:
                raw_answer = wires[in1] >> in2
        elif 'NOT' in lhs:
            param = intize(lhs.split()[1])
            if isinstance(param, int):
                raw_answer = 65536 + ~param
            else:
                raw_answer = 65536 + ~wires[param]
        else:
            try:
                raw_answer = int(lhs.strip())
            except ValueError:
                raw_answer = wires[lhs.strip()]
        # wires[rhs.strip()] = raw_answer if raw_answer >= 0 else 65536 + raw_answer
        wires[rhs.strip()] = raw_answer

        if raw_answer != 0:
            print(f'{raw_answer=}')

    return wires


def main(lines):
    wires = process_instructions([line.split(' -> ') for line in lines])
    return wires


if __name__ == '__main__':
    with open('data/input07.txt') as f:
        lines = [line.strip() for line in f.readlines()]
    wires = main(lines)
    print(wires['a'])
