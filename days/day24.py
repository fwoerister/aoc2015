from heapq import heappop, heappush

from util.solution import SolutionBase


def find_balanced_load_l2(packages):
    open_solutions = [(0, [], [], packages)]
    load_weight = sum(packages) // 4

    while open_solutions:
        load_size, load, withdrawn, remaining = heappop(open_solutions)

        if sum(load) == load_weight:
            if find_balanced_load(packages, load_weight):
                qe = 1
                for p in load:
                    qe *= p
                return qe

        if not remaining:
            continue

        heappush(open_solutions, (load_size + 1, load + [remaining[0]], withdrawn, remaining[1:]))
        heappush(open_solutions, (load_size, load, withdrawn + [remaining[0]], remaining[1:]))


def find_balanced_load(packages, weight):
    open_solutions = [(0, [], [], packages)]
    load_weight = weight

    while open_solutions:
        load_size, load, withdrawn, remaining = heappop(open_solutions)

        if sum(load) == load_weight:
            if find_groups([], load_weight, remaining + withdrawn):
                qe = 1
                for p in load:
                    qe *= p
                return qe

        if not remaining:
            continue

        heappush(open_solutions, (load_size + 1, load + [remaining[0]], withdrawn, remaining[1:]))
        heappush(open_solutions, (load_size, load, withdrawn + [remaining[0]], remaining[1:]))


def find_groups(picked, size, packages):
    if not packages:
        return False

    if sum(picked) == size:
        return True

    if sum(picked) > size:
        return False

    return find_groups(picked, size, packages[1:]) or find_groups(picked + [packages[0]], size, packages[1:])


class Solution(SolutionBase):
    def __init__(self):
        super().__init__(2015, 24)

    def level1(self, example_input=False):
        with self.get_input_file(example_input) as f:
            packages = [int(v) for v in f.readlines() if v]
            return find_balanced_load(packages, sum(packages) // 3)

    def level2(self, example_input=False):
        with self.get_input_file(example_input) as f:
            packages = [int(v) for v in f.readlines() if v]
            return find_balanced_load_l2(packages)
