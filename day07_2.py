from day07_1 import main


if __name__ == '__main__':
    with open('data/input07_2.txt') as f:
        lines = [line.strip() for line in f.readlines()]
    wires = main(lines)
    print(wires['a'])
