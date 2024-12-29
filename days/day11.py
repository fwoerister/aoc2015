from util.solution import SolutionBase


def increment_password(pwd):
    pwd = [ord(digit) for digit in pwd]
    pwd.reverse()

    pwd[0] += 1

    while any([val > ord('z') for val in pwd]):
        idx = pwd.index(ord('z') + 1)
        pwd[idx] = ord('a')
        if idx != len(pwd) - 1:
            pwd[idx + 1] += 1

    pwd.reverse()
    return ''.join([chr(val) for val in pwd])


def check_password(pwd):
    return (contains_inc_straight(pwd)
            and not contains_letters(pwd, ['i', 'o', 'l'])
            and count_non_overlapping_pairs(pwd) >= 2)


def contains_inc_straight(pwd):
    pwd = [ord(digit) for digit in pwd]

    for idx in range(len(pwd) - 2):
        if pwd[idx + 1] == pwd[idx] + 1 and pwd[idx + 2] == pwd[idx] + 2:
            return True
    return False


def contains_letters(pwd, letters):
    for l in letters:
        if l in pwd:
            return True
    return False


def count_non_overlapping_pairs(pwd):
    count = 0
    idx = 0

    while idx < len(pwd) - 1:
        if pwd[idx] == pwd[idx + 1]:
            count += 1
            idx += 2
        else:
            idx += 1

    return count


class Solution(SolutionBase):
    def __init__(self):
        super().__init__(2015, 11)

    def level1(self, example_input=False):
        with self.get_input_file(example_input) as f:
            pwd = f.readline().strip()

            while not check_password(pwd):
                pwd = increment_password(pwd)

            return pwd

    def level2(self, example_input=False):
        with self.get_input_file(example_input) as f:
            pwd = f.readline().strip()

            while not check_password(pwd):
                pwd = increment_password(pwd)

            pwd = increment_password(pwd)

            while not check_password(pwd):
                pwd = increment_password(pwd)

            return pwd
