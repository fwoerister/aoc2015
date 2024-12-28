from util.solution import SolutionBase

offset = {
    '<': (-1, 0),
    '>': (1, 0),
    '^': (0, -1),
    'v': (0, 1),
}


class Solution(SolutionBase):
    def __init__(self):
        super().__init__(2015, 3)

    def level1(self, example_input=False):
        visited = {(0, 0)}

        with self.get_input_file(example_input) as f:
            current = (0, 0)
            for direction in f.readline():
                current_x, current_y = current
                offset_x, offset_y = offset[direction]

                current = (current_x + offset_x, current_y + offset_y)
                visited.add(current)

        return len(visited)

    def level2(self, example_input=False):
        visited = {(0, 0)}

        with self.get_input_file(example_input) as f:
            instructions = f.readline()

            current = (0, 0)
            for direction in [instructions[idx] for idx in range(0, len(instructions), 2)]:
                current_x, current_y = current
                offset_x, offset_y = offset[direction]

                current = (current_x + offset_x, current_y + offset_y)
                visited.add(current)

            current = (0, 0)
            for direction in [instructions[idx] for idx in range(1, len(instructions), 2)]:
                current_x, current_y = current
                offset_x, offset_y = offset[direction]

                current = (current_x + offset_x, current_y + offset_y)
                visited.add(current)

        return len(visited)
