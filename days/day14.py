import re

from util.solution import SolutionBase


def parse_input(lines):
    deers = []

    for line in [l.strip() for l in lines if l]:
        result = re.search(r'(\w+) .+ (\d+) km/s for (\d+) seconds.* (\d+) seconds', line)
        name, speed, duration, rest_time = result.groups()
        deers.append((name, int(speed), int(duration), int(rest_time)))

    return deers


def calc_distance(deer, time):
    name, speed, duration, rest_time = deer

    total_rounds = time // (duration + rest_time)
    remaining = time % (duration + rest_time)

    return total_rounds * speed * duration + min(remaining, duration) * speed


def calc_max_score(deers, time):
    scores = [0] * len(deers)
    for t in range(1, time + 1):
        traveled_distances = [calc_distance(deer, t) for deer in deers]
        lead = max(traveled_distances)

        for idx in range(len(deers)):
            if traveled_distances[idx] == lead:
                scores[idx] += 1

    return max(scores)


class Solution(SolutionBase):
    def __init__(self):
        super().__init__(2015, 14)

    def level1(self, example_input=False):
        time = 2503
        with self.get_input_file(example_input) as f:
            traveled_distances = [calc_distance(deer, time) for deer in parse_input(f.readlines())]

        return max(traveled_distances)

    def level2(self, example_input=False):
        with self.get_input_file(example_input) as f:
            deers = parse_input(f.readlines())

        return calc_max_score(deers, 2503)
