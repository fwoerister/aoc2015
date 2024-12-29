import json

from util.solution import SolutionBase


def dict_to_num(data, ignore_red=False):
    result = 0

    if type(data) is list:
        for val in data:
            result += dict_to_num(val, ignore_red)
        return result
    elif type(data) is dict:
        if ignore_red and "red" in data.values():
            return 0
        for val in data:
            result += dict_to_num(data[val], ignore_red)
        return result
    elif type(data) is int:
        return data
    else:
        return 0


class Solution(SolutionBase):
    def __init__(self):
        super().__init__(2015, 12)

    def level1(self, example_input=False):
        with self.get_input_file(example_input) as f:
            data = json.loads(f.readline())
            return dict_to_num(data)

    def level2(self, example_input=False):
        with self.get_input_file(example_input) as f:
            data = json.loads(f.readline())
            return dict_to_num(data, ignore_red=True)
