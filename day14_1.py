from dataclasses import dataclass


@dataclass
class Reindeer:
    speed: int
    fly_time: int
    rest_time: int
    flying: bool = True

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


if __name__ == '__main__':
    with open('data/input14.txt') as f:
        lines = f.readlines()

    reindeer = [Reindeer(*parse_line(line)) for line in lines]
    distances = [r.calc_distance(2503) for r in reindeer]
    print(max(distances))
