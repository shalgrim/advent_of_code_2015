def get_string_length(s):
    evald = eval(s)
    answer = len(evald)
    return answer


def get_file_diffs(fn):
    with open(fn) as f:
        lines = [line.strip() for line in f.readlines()]
    raw_lens = sum(len(line) for line in lines)
    fancy_lens = sum(get_string_length(line) for line in lines)
    return raw_lens - fancy_lens


if __name__ == '__main__':
    print(get_file_diffs('./data/input08.txt'))
