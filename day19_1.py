def make_replacements(starter, rule):
    answer = set()
    lindex = starter.find(rule[0])
    while lindex >= 0:
        replacement = starter[:lindex] + rule[1] + starter[lindex + len(rule[0]) :]
        answer.add(replacement)
        lindex = starter.find(rule[0], lindex + 1)

    return answer


def main(fn):
    with open(fn) as f:
        lines = [line.strip() for line in f.readlines()]

    rules = [line.split(' => ') for line in lines[:-2]]
    starter = lines[-1]
    molecules = set()
    for rule in rules:
        molecules.update(make_replacements(starter, rule))

    return len(molecules)


if __name__ == '__main__':
    print(main('data/input19.txt'))
