from heapq import heappop, heappush

from util.solution import SolutionBase


def find_shortest_path(cities):
    return min([find_shortest_path_from(cities, city) for city in cities])


def find_longest_path(cities):
    return abs(min([find_shortest_path_from(cities, city, negate_weights=True) for city in cities]))


def find_shortest_path_from(cities, start, negate_weights=False):
    open_nodes = [(0, start, {start})]

    while open_nodes:
        cur_weight, cur_city, cur_visited = heappop(open_nodes)

        if len(cur_visited) == len(cities.values()):
            return cur_weight

        for neighbor in [n for n in cities[cur_city] if n[1] not in cur_visited]:
            weight, city_name = neighbor

            if negate_weights:
                heappush(open_nodes, (cur_weight - weight, city_name, cur_visited.union({city_name})))
            else:
                heappush(open_nodes, (cur_weight + weight, city_name, cur_visited.union({city_name})))


def parse_input(data):
    cities = {}
    for line in [l.strip() for l in data if l]:
        from_to, weight = line.split(' = ')
        source, target = from_to.split(' to ')

        if source not in cities:
            cities[source] = [(int(weight), target)]
        else:
            cities[source].append((int(weight), target))

        if target not in cities:
            cities[target] = [(int(weight), source)]
        else:
            cities[target].append((int(weight), source))

    return cities


class Solution(SolutionBase):
    def __init__(self):
        super().__init__(2015, 9)

    def level1(self, example_input=False):
        with self.get_input_file(example_input) as f:
            cities = parse_input(f.readlines())
            return find_shortest_path(cities)

    def level2(self, example_input=False):
        with self.get_input_file(example_input) as f:
            cities = parse_input(f.readlines())
            return find_longest_path(cities)
