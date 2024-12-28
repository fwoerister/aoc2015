from hashlib import md5

from util.solution import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__(2015, 4)

    def level1(self, example_input=False):
        with self.get_input_file(example_input) as f:
            secret_key = f.readline().strip()
            num = 0
            while not md5((secret_key + str(num)).encode()).hexdigest().startswith('00000'):
                num += 1

            return num

    def level2(self, example_input=False):
        with self.get_input_file(example_input) as f:
            secret_key = f.readline().strip()
            num = 0
            while not md5((secret_key + str(num)).encode()).hexdigest().startswith('000000'):
                num += 1

            return num
