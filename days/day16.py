from util.solution import SolutionBase


def parse_input(lines):
    aunts = []
    for line in [l.strip() for l in lines if l]:
        first_colone = line.index(':')
        tag = line[:first_colone]
        attributes = line[first_colone + 2:]
        aunt_id = int(tag.split(' ')[1])

        attributes = attributes.split(', ')

        aunt = {'id': aunt_id}
        for attribute in attributes:
            key, val = attribute.split(": ")
            val = int(val)
            aunt[key] = val
        aunts.append(aunt)

    return aunts


def does_match_l1(aunt, filter):
    for key in filter:
        if key in aunt and aunt[key] != filter[key]:
            return False
    return True


def does_match_l2(aunt, filter):
    for key in filter:
        if key in ['cats', 'trees']:
            if key in aunt and aunt[key] <= filter[key]:
                return False
        elif key in ['pomeranians', 'goldfish']:
            if key in aunt and aunt[key] >= filter[key]:
                return False
        else:
            if key in aunt and aunt[key] != filter[key]:
                return False

    return True


class Solution(SolutionBase):
    def __init__(self):
        super().__init__(2015, 16)

    def level1(self, example_input=False):
        with self.get_input_file(example_input) as f:
            aunts = parse_input(f.readlines())
            aunt_filter = {"children": 3,
                           "cats": 7,
                           "samoyeds": 2,
                           "pomeranians": 3,
                           "akitas": 0,
                           "vizslas": 0,
                           "goldfish": 5,
                           "trees": 3,
                           "cars": 2,
                           "perfumes": 1,
                           }
            return [a for a in aunts if does_match_l1(a, aunt_filter)][0]['id']

    def level2(self, example_input=False):
        with self.get_input_file(example_input) as f:
            aunts = parse_input(f.readlines())
            aunt_filter = {"children": 3,
                           "cats": 7,
                           "samoyeds": 2,
                           "pomeranians": 3,
                           "akitas": 0,
                           "vizslas": 0,
                           "goldfish": 5,
                           "trees": 3,
                           "cars": 2,
                           "perfumes": 1,
                           }
            return [a for a in aunts if does_match_l2(a, aunt_filter)][0]['id']
