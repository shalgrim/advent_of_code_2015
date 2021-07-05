from dataclasses import dataclass


@dataclass
class Reindeer:
    speed: int
    fly_time: int
    rest_time: int
    flying: bool = True
    score: int = 0

    def calc_distance(self, seconds) -> int:
        seconds_left = seconds
        answer = 0

        while seconds_left:
            if self.flying:
                if seconds_left <= self.fly_time:
                    answer += self.speed * seconds_left
                    seconds_left = 0
                else:
                    answer += self.speed * self.fly_time
                    self.flying = False
                    seconds_left -= self.fly_time
            else:
                if seconds_left <= self.rest_time:
                    seconds_left = 0
                else:
                    self.flying = True
                    seconds_left -= self.rest_time

        return answer


def parse_line(line: str):
    tokens = line.split()
    return [int(tokens[3]), int(tokens[6]), int(tokens[13])]


def get_reindeer_from_file(filename):
    with open(filename) as f:
        lines = f.readlines()
    return [Reindeer(*parse_line(line)) for line in lines]


if __name__ == '__main__':
    reindeer = get_reindeer_from_file('data/input14.txt')
    distances = [r.calc_distance(2503) for r in reindeer]
    print(max(distances))
