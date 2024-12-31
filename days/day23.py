from util.solution import SolutionBase


def parse_input(lines):
    instructions = []
    for line in [l.strip() for l in lines if l]:
        mnemonic = line[:3]
        args = line[4:].split(', ')
        match mnemonic:
            case 'hlf':
                instructions.append(HlfInstruction(args))
            case 'tpl':
                instructions.append(TplInstruction(args))
            case 'inc':
                instructions.append(IncInstruction(args))
            case 'jmp':
                instructions.append(JmpInstruction(args))
            case 'jie':
                instructions.append(JieInstruction(args))
            case 'jio':
                instructions.append(JioInstruction(args))

    return instructions


class Machine:
    def __init__(self, prog):
        self.reg = {
            'p': 0,
            'a': 0,
            'b': 0,
        }

        self.prog = prog

    def execute_next(self):
        inst = self.prog[self.reg['p']]
        inst.execute_on(self)

    def terminated(self):
        return self.reg['p'] >= len(self.prog)


class Instruction:
    def __init__(self, args):
        self.args = args


class HlfInstruction(Instruction):
    def execute_on(self, machine):
        machine.reg[self.args[0]] //= 2
        machine.reg['p'] += 1


class TplInstruction(Instruction):
    def execute_on(self, machine):
        machine.reg[self.args[0]] *= 3
        machine.reg['p'] += 1


class IncInstruction(Instruction):
    def execute_on(self, machine):
        machine.reg[self.args[0]] += 1
        machine.reg['p'] += 1


class JmpInstruction(Instruction):
    def execute_on(self, machine):
        machine.reg['p'] += int(self.args[0])


class JieInstruction(Instruction):
    def execute_on(self, machine):
        if machine.reg[self.args[0]] % 2 == 0:
            machine.reg['p'] += int(self.args[1])
        else:
            machine.reg['p'] += 1


class JioInstruction(Instruction):
    def execute_on(self, machine):
        if machine.reg[self.args[0]] == 1:
            machine.reg['p'] += int(self.args[1])
        else:
            machine.reg['p'] += 1


class Solution(SolutionBase):
    def __init__(self):
        super().__init__(2015, 23)

    def level1(self, example_input=False):
        with self.get_input_file(example_input) as f:
            prog = parse_input(f.readlines())
            m = Machine(prog)

            while not m.terminated():
                m.execute_next()

            return int(m.reg['b'])

    def level2(self, example_input=False):
        with self.get_input_file(example_input) as f:
            prog = parse_input(f.readlines())
            m = Machine(prog)

            m.reg['a'] = 1

            while not m.terminated():
                m.execute_next()

            return int(m.reg['b'])
