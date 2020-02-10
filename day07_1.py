from collections import defaultdict
from copy import copy


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


def get_relied_on(lhs):
    items = lhs.split()
    relied_on = []

    for item in items:
        if isinstance(intize(item.strip()), int) or item.strip() in (['AND', 'OR', 'NOT', 'RSHIFT', 'LSHIFT']):
            pass
        else:
            relied_on.append(item.strip())

    return relied_on


def order_instructions(raw_instructions):
    relies_on = defaultdict(set)
    all_rhs = set()

    for lhs, rhs in raw_instructions:
        relier = rhs.strip()
        all_rhs.add(relier)
        relied_on = get_relied_on(lhs)
        relies_on[relier].update(set(relied_on))

    remaining_instructions = copy(raw_instructions)
    ordered_instructions = []
    while remaining_instructions:
        for rhs in all_rhs:
            if not relies_on[rhs]:
                for ri in remaining_instructions:
                    if ri[1].strip() == rhs:
                        ordered_instructions.append(ri)
                        remaining_instructions.remove(ri)
                        for v in relies_on.values():
                            v.discard(rhs)

    return ordered_instructions


def main(lines):
    instructions = order_instructions([line.split(' -> ') for line in lines])
    wires = process_instructions([instructions])
    return wires


if __name__ == '__main__':
    with open('data/input07.txt') as f:
        lines = [line.strip() for line in f.readlines()]
    wires = main(lines)
    print(wires['a'])
