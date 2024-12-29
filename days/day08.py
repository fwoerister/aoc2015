from util.solution import SolutionBase


def get_str_length(data):
    data = data[1:-1]
    idx = 0
    data_len = 0
    while idx < len(data):
        data_len += 1
        if data[idx:idx + 2] == r'\"':
            idx += 2
        elif data[idx:idx + 2] == r'\\':
            idx += 2
        elif data[idx:idx + 2] == r'\x':
            idx += 4
        else:
            idx += 1
    return data_len


class Solution(SolutionBase):
    def __init__(self):
        super().__init__(2015, 8)

    def level1(self, example_input=False):
        result = 0
        with self.get_input_file(example_input) as f:
            for line in [l.strip() for l in f.readlines()]:
                result += len(line) - get_str_length(line)

        return result

    def level2(self, example_input=False):
        result = 0
        with self.get_input_file(example_input) as f:
            for line in [l.strip() for l in f.readlines()]:
                new_line = line.replace('"', '\\"')
                new_line = new_line.replace("\\", "\\\\")
                result += len(new_line) - get_str_length(new_line)

        return result
