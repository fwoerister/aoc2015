from util.solution import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__(2015, 2)

    def level1(self, example_input=False):
        result = 0
        with self.get_input_file(example_input) as f:
            for dimensions in [line.strip() for line in f]:
                l, w, h = [int(val) for val in dimensions.split('x')]
                result += 2 * l * w + 2 * w * h + 2 * l * h
                result += min(l * w, w * h, l * h)
        return result

    def level2(self, example_input=False):
        result = 0
        with self.get_input_file(example_input) as f:
            for dimensions in [line.strip() for line in f]:
                l, w, h = [int(val) for val in dimensions.split('x')]
                result += min(2 * l + 2 * w, 2 * w + 2 * h, 2 * l + 2 * h)
                result += l * w * h
        return result
