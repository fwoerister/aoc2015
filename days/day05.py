from util.solution import SolutionBase


class StringVerifier:
    def __init__(self, payload):
        self.payload = payload

    def count_vowels(self):
        count = 0
        for vowel in ['a', 'e', 'i', 'o', 'u']:
            count += self.payload.count(vowel)
        return count

    def get_pair_locations(self):
        pair_locations = []
        for idx in range(1, len(self.payload)):
            if self.payload[idx] == self.payload[idx - 1]:
                pair_locations.append(idx - 1)
        return pair_locations

    def does_contain(self, snippets):
        for snippet in snippets:
            if self.payload.find(snippet) >= 0:
                return True
        return False

    def contains_non_overlapping_pair(self):
        for idx in range(len(self.payload) - 1):
            for pair_idx in range(idx + 2, len(self.payload) - 1):
                if self.payload[idx:idx + 2] == self.payload[pair_idx:pair_idx + 2]:
                    return True

        return False

    def contains_repeating_letter(self):
        count = 0
        for idx in range(len(self.payload) - 2):
            if self.payload[idx] == self.payload[idx + 2]:
                return True
        return False


class Solution(SolutionBase):
    def __init__(self):
        super().__init__(2015, 5)

    def level1(self, example_input=False):
        with self.get_input_file(example_input) as f:
            count = 0
            for line in [l.strip() for l in f.readlines()]:
                v = StringVerifier(line)
                if v.count_vowels() >= 3 and v.get_pair_locations() and not v.does_contain(["ab", "cd", "pq", "xy"]):
                    count += 1
        return count

    def level2(self, example_input=False):
        with self.get_input_file(example_input) as f:
            count = 0
            for line in [l.strip() for l in f.readlines()]:
                v = StringVerifier(line)
                if v.contains_non_overlapping_pair() and v.contains_repeating_letter():
                    count += 1
        return count
