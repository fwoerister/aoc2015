import re

from util.solution import SolutionBase


def parse_input(lines):
    happiness = {}
    guests = set()
    for line in [l.strip() for l in lines]:
        result = re.search(r'(\w+) would (lose|gain) (\d+) happiness units by sitting next to (\w+)', line)
        n1, sign, value, n2 = result.groups()
        sign = -1 if sign == 'lose' else 1
        value = int(value)

        happiness[(n1, n2)] = sign * value
        guests.add(n1)
        guests.add(n2)

    return happiness, guests


def find_best_seating_score(guests, happiness, seating):
    max_score = None

    if not guests:
        score = 0
        for idx in range(len(seating)):
            score += happiness[(seating[idx - 1], seating[idx])]
            score += happiness[(seating[idx], seating[idx - 1])]
        return score

    for g in guests:
        new_seating = seating + [g]
        score = find_best_seating_score(guests.difference({g}), happiness, new_seating)
        if not max_score or score > max_score:
            max_score = score
    return max_score


class Solution(SolutionBase):
    def __init__(self):
        super().__init__(2015, 13)

    def level1(self, example_input=False):
        with self.get_input_file(example_input) as f:
            happiness, guests = parse_input(f.readlines())

        return find_best_seating_score(guests, happiness, [])

    def level2(self, example_input=False):
        with self.get_input_file(example_input) as f:
            happiness, guests = parse_input(f.readlines())

        for g in guests:
            happiness[(g, 'me')] = 0
            happiness[('me', g)] = 0

        guests.add('me')

        return find_best_seating_score(guests, happiness, [])
