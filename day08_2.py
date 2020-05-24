def get_encoded(s):
    encoded = s.replace('\\', r'\\')
    encoded = encoded.replace('"', r'\"')
    return encoded


def get_encoded_len(s):
    return len(get_encoded(s)) + 2


def get_encoded_file_diff(fn):
    with open(fn) as f:
        lines = [line.strip() for line in f.readlines()]
    raw_lens = sum(len(line) for line in lines)
    encoded_lens = sum(get_encoded_len(line) for line in lines)
    return encoded_lens - raw_lens


if __name__ == '__main__':
    print(get_encoded_file_diff('./data/input08.txt'))
