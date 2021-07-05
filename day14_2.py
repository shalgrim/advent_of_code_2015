from day14_1 import get_reindeer_from_file


def conduct_race(reindeer, seconds):
    for _ in range(seconds):
        for r in reindeer:
            r.advance()

        max_distance = max(r.distance for r in reindeer)
        for r in reindeer:
            if r.distance == max_distance:
                r.score += 1


if __name__ == '__main__':
    reindeer = get_reindeer_from_file('data/input14.txt')
    conduct_race(reindeer, 2503)
    print(max([r.score for r in reindeer]))
