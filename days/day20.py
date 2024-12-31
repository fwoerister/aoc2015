from sympy import divisors

from util.solution import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__(2015, 20)

    def level1(self, example_input=False):
        with self.get_input_file(example_input) as f:
            house = 1
            limit = int(f.readline())
            while sum(divisors(house)) * 10 < limit:
                house += 1
            return house

    def level2(self, example_input=False):
        with self.get_input_file(example_input) as f:
            house = 1
            limit = int(f.readline())
            while sum([d for d in divisors(house) if d * 50 >= house]) * 11 < limit:
                house += 1
            return house
