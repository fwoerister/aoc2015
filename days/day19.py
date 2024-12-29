from heapq import heappop, heappush

from util.solution import SolutionBase

# greedy approach, does not guarantee optimal solution!
#
# checkout this solution:
# https://en.wikipedia.org/wiki/CYK_algorithm

def gen_distinct_molecules(molecule, rules, prefix=""):
    applicable_rule_keys = [key for key in rules if molecule.startswith(key)]

    if molecule == '':
        return {prefix}

    if len(applicable_rule_keys) == 0:
        return gen_distinct_molecules(molecule[1:], rules, prefix + molecule[0])

    new_molecules = set()
    for key in applicable_rule_keys:
        for to_m in rules[key]:
            new_molecules.add(prefix + to_m + molecule[len(key):])
        new_molecules = new_molecules.union(gen_distinct_molecules(molecule[len(key):], rules, prefix + key))
    return new_molecules


def parse_input(lines):
    idx = 0
    rules = {}
    while lines[idx] != '\n':
        from_m, to_m = lines[idx].strip().split(' => ')
        if from_m in rules:
            rules[from_m].append(to_m)
        else:
            rules[from_m] = [to_m]
        idx += 1

    idx += 1
    molecule = lines[idx].strip()

    return rules, molecule


def get_minimal_steps_to_medicine(rules, molecule):
    open_solutions = [(len(molecule), 0, molecule)]

    while open_solutions:
        len_m, current_steps, current_molecule = heappop(open_solutions)
        if current_molecule == 'e':
            return current_steps

        for idx in range(len(current_molecule)):
            applicable_rule_keys = []
            for key in rules:
                for to_m in rules[key]:
                    if current_molecule[idx:].startswith(to_m):
                        applicable_rule_keys.append((key, to_m))

            for key, value in applicable_rule_keys:
                new_m = current_molecule[:idx] + key + current_molecule[idx + len(value):]
                heappush(open_solutions, (len(new_m), current_steps + 1, new_m))


class Solution(SolutionBase):
    def __init__(self):
        super().__init__(2015, 19)

    def level1(self, example_input=False):
        with self.get_input_file(example_input) as f:
            rules, molecules = parse_input(f.readlines())

            return len(gen_distinct_molecules(molecules, rules)) - 1

    def level2(self, example_input=False):
        with self.get_input_file(example_input) as f:
            rules, molecules = parse_input(f.readlines())
            return get_minimal_steps_to_medicine(rules, molecules)
