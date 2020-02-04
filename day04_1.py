from hashlib import md5


SECRET_KEY = 'iwrupvqb'


def main(secret_key):
    i = 0
    instring = f'{secret_key}{i}'
    hash = md5(instring.encode())
    while hash.hexdigest()[:5] != '00000':
        i += 1
        instring = f'{secret_key}{i}'
        hash = md5(instring.encode())

    return i


if __name__ == '__main__':
    print(main(SECRET_KEY))
