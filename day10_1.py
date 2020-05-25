def get_num_times(s):
    digit_of_interest = s[0]
    num_times = 1

    for c in s[1:]:
        if c == digit_of_interest:
            num_times += 1
        else:
            break

    return digit_of_interest, num_times


def look_and_say(s):
    answer = ''
    i = 0
    while i < len(s):
        digit, num_times = get_num_times(s[i:])
        answer += f'{num_times}{digit}'
        i += num_times

    return answer


def main(s, num_applications=40):
    answer = s
    for i in range(num_applications):
        answer = look_and_say(answer)
        print(f'{i=}, {len(answer)=}')

    return answer


if __name__ == '__main__':
    print(len(main('1113222113', 40)))
