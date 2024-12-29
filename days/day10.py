from util.solution import SolutionBase


def look_and_say(data, level):
    if level == 0:
        return len(data)

    result = ''

    idx = 0
    while idx < len(data):
        char = data[idx]
        char_idx = idx
        idx += 1
        while idx < len(data) and data[idx] == char:
            idx += 1

        result += str(idx - char_idx) + char

    return look_and_say(result, level - 1)


class Solution(SolutionBase):
    def __init__(self):
        super().__init__(2015, 10)

    def level1(self, example_input=False):
        with self.get_input_file(example_input) as f:
            initial_val = f.readline().strip()
            return look_and_say(initial_val, 40)

    def level2(self, example_input=False):
        with self.get_input_file(example_input) as f:
            initial_val = f.readline().strip()
            return look_and_say(initial_val, 50)
