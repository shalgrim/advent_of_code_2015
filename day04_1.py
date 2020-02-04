from hashlib import md5


SECRET_KEY = 'iwrupvqb'


def main(secret_key, num_zeroes=5):
    i = 0
    instring = f'{secret_key}{i}'
    hash = md5(instring.encode())
    while hash.hexdigest()[:num_zeroes] != '0' * num_zeroes:
        i += 1
        instring = f'{secret_key}{i}'
        hash = md5(instring.encode())

    return i


if __name__ == '__main__':
    print(main(SECRET_KEY))
