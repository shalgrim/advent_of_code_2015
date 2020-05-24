import math
from collections import defaultdict


def get_routes(lines):
    routes = defaultdict(dict)
    for line in lines:
        splits = line.split()
        city1 = splits[0]
        city2 = splits[2]
        distance = int(splits[-1])
        routes[city1][city2] = distance
        routes[city2][city1] = distance

    return routes


def get_shortest_path_dfs(start_city, routes, path=None):
    raise NotImplementedError


def get_shortest_path(lines):
    routes = get_routes(lines)
    shortest_path = math.inf

    shortest_paths_by_origin = [get_shortest_path_dfs(start_city, routes) for start_city in routes]
    return min(shortest_paths_by_origin)


if __name__ == '__main__':
    with open('./data/input09.txt') as f:
        lines = [line.strip() for line in f.readlines()]
    print(get_shortest_path(lines))
