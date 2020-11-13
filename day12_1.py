import re


if __name__ == '__main__':
    with open('data/input12.txt') as f:
        txt = f.read()

    all_nums = re.findall(r'-?\d+', txt)
    all_nums = [int(i) for i in all_nums]
    print(sum(all_nums))
