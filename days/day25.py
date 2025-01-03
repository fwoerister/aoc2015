import re

from util.solution import SolutionBase


def parse_input(line):
    row = int(re.search(r'row (\d*)', line).groups()[0])
    column = int(re.search(r'column (\d*)', line).groups()[0])
    return row, column


class CodeGenerator:
    def __init__(self, initial_code):
        self.initial_code = initial_code

    @staticmethod
    def get_idx(row, column):
        idx = column + row - 1
        idx = idx * (idx + 1) // 2
        idx -= (row - 1)
        return idx

    def get_code(self, row, column):
        code = self.initial_code
        idx = self.get_idx(row, column)
        while idx > 1:
            code = (code * 252533) % 33554393
            idx -= 1
        return code


class Solution(SolutionBase):
    def __init__(self):
        super().__init__(2015, 25)

    def level1(self, example_input=False):
        with self.get_input_file(example_input) as f:
            row, column = parse_input(f.readline())

            gen = CodeGenerator(20151125)
            return gen.get_code(row, column)
