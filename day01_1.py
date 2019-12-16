def main(paren_line):
    return paren_line.count('(') - paren_line.count(')')


if __name__ == '__main__':
    with open('data/input01.txt') as f:
        content = f.read().strip()
    print(main(content))
