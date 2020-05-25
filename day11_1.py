import re


REPEAT = re.compile(r'(.)\1')


def meets_req1(s):
    """one increasing straight of 3"""
    for i in range(ord('a'), ord('y')):
        substr = chr(i) + chr(i+1) + chr(i+2)
        if substr in s:
            return True

    return False


def meets_req2(s):
    return 'i' not in s and 'l' not in s and 'o' not in s


def meets_req3(s):
    repeats = set(REPEAT.findall(s))
    return len(repeats) > 1


def is_valid(pwd):
    return meets_req1(pwd) and meets_req2(pwd) and meets_req3(pwd)


def get_next_pwd(pwd):
    next_pwd = increment(pwd)
    while not is_valid(next_pwd):
        next_pwd = increment(next_pwd)

    return next_pwd


def smart_increment(pwd):
    raise NotImplementedError


def increment(pwd):
    answer = ['.'] * len(pwd)
    for i in range(len(pwd)-1, -1, -1):
        letter = pwd[i]
        if ord(letter) < ord('z'):
            answer[i] = chr(ord(letter) + 1)
            for j in range(i):
                answer[j] = pwd[j]
            break
        else:
            answer[i] = 'a'

    return ''.join(answer)


if __name__ == '__main__':
    print(get_next_pwd('hepxcrrq'))
