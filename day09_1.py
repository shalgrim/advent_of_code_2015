import math
from collections import defaultdict
from copy import copy


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


def get_shortest_path_dfs(routes, path, distance=0):
    remaining_cities = {k for k in routes if k not in path}
    if not remaining_cities:  # base case
        return path, distance

    these_paths = []
    for rc in remaining_cities:
        incremental_distance = routes[path[-1]][rc]
        new_path = copy(path)
        new_path.append(rc)
        shortest_from_here_tuple = get_shortest_path_dfs(routes, new_path, distance+incremental_distance)
        these_paths.append(shortest_from_here_tuple)

    sorted_paths = sorted(these_paths, key=lambda x: x[1])
    return sorted_paths[0]


def get_shortest_path(lines):
    routes = get_routes(lines)
    shortest_path = math.inf

    shortest_path_tuples_by_origin = [
        get_shortest_path_dfs(routes, [start_city]) for start_city in routes
    ]
    return min(tpl[1] for tpl in shortest_path_tuples_by_origin)


if __name__ == '__main__':
    with open('./data/input09.txt') as f:
        lines = [line.strip() for line in f.readlines()]
    print(get_shortest_path(lines))
