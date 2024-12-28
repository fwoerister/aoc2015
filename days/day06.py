import re

from util.solution import SolutionBase


class LightPanel:
    def __init__(self):
        self.intensity = 0
        self.active_lights = set()

    def turn_on(self, start, end):
        for x in range(start[0], end[0] + 1):
            for y in range(start[1], end[1] + 1):
                self.active_lights.add((x, y))

    def turn_off(self, start, end):
        for x in range(start[0], end[0] + 1):
            for y in range(start[1], end[1] + 1):
                if (x, y) in self.active_lights:
                    self.active_lights.remove((x, y))

    def toggle(self, start, end):
        for x in range(start[0], end[0] + 1):
            for y in range(start[1], end[1] + 1):
                if (x, y) in self.active_lights:
                    self.active_lights.remove((x, y))
                else:
                    self.active_lights.add((x, y))


class LightPanelL2:
    def __init__(self):
        self.active_lights = dict()

    def turn_on(self, start, end):
        for x in range(start[0], end[0] + 1):
            for y in range(start[1], end[1] + 1):
                if (x, y) in self.active_lights:
                    self.active_lights[(x, y)] += 1
                else:
                    self.active_lights[(x, y)] = 1

    def turn_off(self, start, end):
        for x in range(start[0], end[0] + 1):
            for y in range(start[1], end[1] + 1):
                if (x, y) in self.active_lights and self.active_lights[(x, y)] > 0:
                    self.active_lights[(x, y)] -= 1

    def toggle(self, start, end):
        for x in range(start[0], end[0] + 1):
            for y in range(start[1], end[1] + 1):
                if (x, y) in self.active_lights:
                    self.active_lights[(x, y)] += 2
                else:
                    self.active_lights[(x, y)] = 2


class Solution(SolutionBase):
    def __init__(self):
        super().__init__(2015, 6)

    def level1(self, example_input=False):
        with self.get_input_file(example_input) as f:
            panel = LightPanel()
            for instruction in f.readlines():
                result = re.search(r"(turn on|turn off|toggle) (\d+,\d+) through (\d+,\d+)", instruction)
                command, start, end = result.groups()
                start = [int(val) for val in start.split(',')]
                end = [int(val) for val in end.split(',')]

                match command:
                    case 'turn on':
                        panel.turn_on(start, end)
                    case 'turn off':
                        panel.turn_off(start, end)
                    case 'toggle':
                        panel.toggle(start, end)

        return len(panel.active_lights)

    def level2(self, example_input=False):
        with self.get_input_file(example_input) as f:
            panel = LightPanelL2()
            for instruction in f.readlines():
                result = re.search(r"(turn on|turn off|toggle) (\d+,\d+) through (\d+,\d+)", instruction)
                command, start, end = result.groups()
                start = [int(val) for val in start.split(',')]
                end = [int(val) for val in end.split(',')]

                match command:
                    case 'turn on':
                        panel.turn_on(start, end)
                    case 'turn off':
                        panel.turn_off(start, end)
                    case 'toggle':
                        panel.toggle(start, end)

        return sum(panel.active_lights.values())
