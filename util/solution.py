from util.submit import submit_answer


class SolutionBase:
    def __init__(self, year, day):
        self.year = year
        self.day = day

    def run(self, level, example_input):
        match level:
            case 1:
                return self.level1(example_input)
            case 2:
                return self.level2(example_input)

    def level1(self, example_input=False):
        raise NotImplementedError()

    def level2(self, example_input=False):
        raise NotImplementedError()

    def submit(self, level):
        result = self.level1() if level == 1 else self.level2()
        submit_answer(result, day=self.day, year=self.year, level=1)

    def get_input_file(self, example_input=False):
        if example_input:
            return open(f'input/day{str(self.day).rjust(2, "0")}d.txt')
        return open(f'input/day{str(self.day).rjust(2, "0")}.txt')
