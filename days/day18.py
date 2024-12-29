from util.datastructures import Grid
from util.solution import SolutionBase


class GOL(Grid):

    def __init__(self, rows, broken_cells=[]):
        super().__init__(rows)
        self.broken_cells = broken_cells

    def next_evolution(self):
        next_evolution = []

        for y in range(self.height):
            next_evolution.append([])
            for x in range(self.width):
                is_active = self.get_val_at(x, y) == '#'
                neighbours = self.get_neighbours(x, y) + self.get_diagnoal_neighbours(x, y)
                count_active = 0
                for n in neighbours:
                    if self.get_val_at(*n) == '#':
                        count_active += 1

                if is_active and count_active in [2, 3]:
                    next_evolution[y].append('#')
                elif not is_active and count_active == 3:
                    next_evolution[y].append('#')
                elif (x, y) in self.broken_cells:
                    next_evolution[y].append('#')
                else:
                    next_evolution[y].append('.')

        self.rows = next_evolution

    def count_active(self):
        count = 0
        for y in range(self.height):
            for x in range(self.width):
                if self.get_val_at(x, y) == '#':
                    count += 1
        return count


class Solution(SolutionBase):
    def __init__(self):
        super().__init__(2015, 18)

    def level1(self, example_input=False):
        with self.get_input_file(example_input) as f:
            gof = GOL(f.readlines())

            for evolution in range(100):
                gof.next_evolution()

            return gof.count_active()

    def level2(self, example_input=False):
        with self.get_input_file(example_input) as f:
            gof = GOL(f.readlines())

            broken_cells = [
                (0, 0),
                (gof.width - 1, 0),
                (0, gof.height - 1),
                (gof.width - 1, gof.height - 1),
            ]

            gof.broken_cells = broken_cells

            for evolution in range(100):
                gof.next_evolution()

            return gof.count_active()
