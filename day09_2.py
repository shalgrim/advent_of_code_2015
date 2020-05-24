from itertools import permutations

from day09_1 import get_routes


def get_route_length(path, routes):
    distance = 0
    for i, city in enumerate(path[:-1]):
        distance += routes[city][path[i+1]]

    return distance


def get_longest_path(lines):
    routes = get_routes(lines)
    cities = set(routes.keys())
    distances = []
    for p in permutations(cities):
        distances.append(get_route_length(p, routes))

    return max(distances)


if __name__ == '__main__':
    with open('./data/input09.txt') as f:
        lines = [line.strip() for line in f.readlines()]
    print(get_longest_path(lines))  # 391 is too low
