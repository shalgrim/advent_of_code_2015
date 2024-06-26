from day19_1 import make_replacements


def main(lines):
    rules = [line.split(' => ') for line in lines[:-2]]
    final_molecule = lines[-1].strip()
    num_steps = 0

    seen_molecules = set()
    current_molecules = {'e'}

    while final_molecule not in current_molecules:
        print(f"{num_steps=}")
        print(f"{len(current_molecules)=}")
        seen_molecules.update(current_molecules)
        num_steps += 1
        new_molecules = set()
        for molecule in current_molecules:
            for rule in rules:
                new_molecules.update(make_replacements(molecule, rule))
        current_molecules = new_molecules

    return num_steps


if __name__ == '__main__':
    with open('data/input19.txt') as f:
        lines = [line.strip() for line in f.readlines()]
    print(main(lines))
