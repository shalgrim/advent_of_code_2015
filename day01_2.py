def main(paren_line):
    floor = 0
    for i, c in enumerate(paren_line):
        if c == '(':
            floor += 1
        else:
            floor -=1
        if floor == -1:
            break
    return i + 1


if __name__ == '__main__':
    with open('data/input01.txt') as f:
        content = f.read().strip()
    print(main(content))
