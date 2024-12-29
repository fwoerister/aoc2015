from heapq import heappush, heappop

from util.solution import SolutionBase


def count_possible_arrangements(amount, containers, c_count=None):
    if c_count is None:
        c_count = len(containers)

    if amount < 0:
        return 0

    if amount == 0:
        return 1

    if c_count == 0:
        return 0

    if not containers or sum(containers) < amount:
        return 0

    c = containers[0]
    containers = containers[1:]

    count = count_possible_arrangements(amount, containers, c_count)
    count += count_possible_arrangements(amount - c, containers, c_count - 1)
    return count


def find_min_arrangement(amount, containers):
    open_solutions = [(0, 0, list(containers), [])]

    while open_solutions:
        num_containers, capacity, remaining_containers, picked = heappop(open_solutions)

        if capacity == amount:
            return num_containers

        if remaining_containers:
            c = remaining_containers[0]
            r = remaining_containers[1:]

            heappush(open_solutions, (num_containers + 1, capacity + c, r, picked + [c]))
            heappush(open_solutions, (num_containers, capacity, r, picked))


def parse_input(lines):
    containers = []
    for line in [l.strip() for l in lines]:
        containers.append(int(line))
    return containers


class Solution(SolutionBase):
    def __init__(self):
        super().__init__(2015, 17)

    def level1(self, example_input=False):
        with self.get_input_file(example_input) as f:
            containers = parse_input(f.readlines())
            return count_possible_arrangements(150, containers)

    def level2(self, example_input=False):
        with self.get_input_file(example_input) as f:
            containers = parse_input(f.readlines())
            min_containers = find_min_arrangement(150, containers)
            return count_possible_arrangements(150, containers, 4)
