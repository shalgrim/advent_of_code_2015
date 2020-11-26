import json


def compute_value(item):
    if isinstance(item, dict):
        if 'red' in item.values():
            return 0
        else:
            return sum(compute_value(v) for v in item.values())
    elif isinstance(item, list):
        return sum(compute_value(l) for l in item)
    elif isinstance(item, str):
        try:
            return int(item)
        except ValueError:
            return 0
    elif isinstance(item, int):
        return item
    else:
        return 0


if __name__ == '__main__':
    with open('data/input12.txt') as f:
        txt = f.read()

    j = json.loads(txt)
    print(compute_value(j))
