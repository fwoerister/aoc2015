from util.solution import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__(2015, 1)

    def level1(self, example_input=False):
        with self.get_input_file() as f:
            directions = f.readline()

            return directions.count('(') - directions.count(')')

    def level2(self, example_input=False):
        with self.get_input_file() as f:
            directions = f.readline()

            current_floor = 0
            idx = 0
            for d in directions:
                idx += 1
                if d == '(':
                    current_floor += 1
                if d == ')':
                    current_floor -= 1

                if current_floor == -1:
                    return idx