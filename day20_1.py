from functools import lru_cache
from typing import Set


@lru_cache(maxsize=None)
def factors(num: int) -> Set[int]:
    # TODO: There must be a way to break this into a cached recursive function
    if num == 1:
        return {1}
    divisor = 1
    answer = set()
    while divisor <= num // 2:
        if num % divisor == 0:
            answer.update({divisor, num // divisor})
        divisor += 1
    return answer


def calc_num_presents(house_num: int) -> int:
    # TODO: There's probably a way to break this down and cache stuff
    # TODO: The other idea I have is to do some kind of bisecting search
    # TODO: but honestly there's some number theory approach that is the right way to solve this
    answer = 0
    visiting_elves = factors(house_num)
    for elf in visiting_elves:
        answer += elf * 10
    return answer


def main(peak: int) -> int:
    house_num = 1
    max_num_presents = 0
    while True:
        if house_num % 10_000 == 0:
            print(f"{house_num=}, max num presents: {max_num_presents:_}")
        max_num_presents = max(calc_num_presents(house_num), max_num_presents)
        if max_num_presents >= peak:
            return house_num
        house_num += 1


if __name__ == "__main__":
    # NOTE: If you can't figure out the number theory, then probably the next best approach is a different search that pokes and proods
    # I'm at 310,000 and the max is 12 million so barely a third of the way there
    # Note: Another potential source of insight is documenting when the max goes up
    # Note: Clearly you could do better on caching, breaking things down, etc.
    print(main(33_100_000))
