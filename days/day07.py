from util.solution import SolutionBase


class ConnectionGate:
    def __init__(self, input_wire, output_wire):
        self.input_wire = input_wire
        self.output_wire = output_wire

    def is_processable(self, wires):
        return self.input_wire.isdigit() or self.input_wire in wires

    def process(self, wires):
        if self.input_wire.isdigit():
            wires[self.output_wire] = format(int(self.input_wire), 'b').rjust(16, '0')
        elif self.input_wire in wires:
            wires[self.output_wire] = wires[self.input_wire]


class AndGate:
    def __init__(self, op1, op2, out):
        self.op1 = op1
        self.op2 = op2
        self.out = out

    def is_processable(self, wires):
        return (self.op1.isdigit() or self.op1 in wires) and (self.op2.isdigit() or self.op2 in wires)

    def process(self, wires):

        if self.op1.isdigit():
            op1 = format(int(self.op1), 'b').rjust(16, '0')
        else:
            op1 = wires[self.op1]

        if self.op2.isdigit():
            op2 = format(sint(elf.op2), 'b').rjust(16, '0')
        else:
            op2 = wires[self.op2]

        result = format(int(op1, 2) & int(op2, 2), 'b').rjust(16, '0')
        wires[self.out] = result


class OrGate:
    def __init__(self, op1, op2, out):
        self.op1 = op1
        self.op2 = op2
        self.out = out

    def is_processable(self, wires):
        return (self.op1.isdigit() or self.op1 in wires) and (self.op2.isdigit() or self.op2 in wires)

    def process(self, wires):
        if self.op1.isdigit():
            op1 = format(int(self.op1), 'b').rjust(16, '0')
        else:
            op1 = wires[self.op1]

        if self.op2.isdigit():
            op2 = format(int(self.op2), 'b').rjust(16, '0')
        else:
            op2 = wires[self.op2]

        result = format(int(op1, 2) | int(op2, 2), 'b').rjust(16, '0')
        wires[self.out] = result


class NotGate:
    def __init__(self, op, out):
        self.op = op
        self.out = out

    def is_processable(self, wires):
        return self.op in wires

    def process(self, wires):
        op = wires[self.op]

        result = ''

        for bit in op:
            result += '0' if bit == '1' else '1'

        wires[self.out] = result


class LShiftGate:
    def __init__(self, op, distance, out):
        self.op = op
        self.distance = distance
        self.out = out

    def is_processable(self, wires):
        return self.op in wires

    def process(self, wires):
        op = wires[self.op]
        result = format(int(op, 2) << self.distance, 'b')

        if len(result) > 16:
            result = result[-16:]
        result = result.rjust(16, '0')

        wires[self.out] = result


class RShiftGate:
    def __init__(self, op, distance, out):
        self.op = op
        self.distance = distance
        self.out = out

    def is_processable(self, wires):
        return self.op in wires

    def process(self, wires):
        op = wires[self.op]
        result = format(int(op, 2) >> self.distance, 'b')
        result = result.rjust(16, '0')

        wires[self.out] = result


def str_to_gate(line):
    if "AND" in line:
        operation, output = line.split(" -> ")
        op1, operation, op2 = operation.split(" ")
        return AndGate(op1, op2, output)
    elif "OR" in line:
        operation, output = line.split(" -> ")
        op1, operation, op2 = operation.split(" ")
        return OrGate(op1, op2, output)
    elif "NOT" in line:
        operation, output = line.split(" -> ")
        operation, op = operation.split(" ")
        return NotGate(op, output)
    elif "LSHIFT" in line:
        operation, output = line.split(" -> ")
        op1, operation, op2 = operation.split(" ")
        return LShiftGate(op1, int(op2), output)
    elif "RSHIFT" in line:
        operation, output = line.split(" -> ")
        op1, operation, op2 = operation.split(" ")
        return RShiftGate(op1, int(op2), output)
    else:
        operation, output = line.split(" -> ")
        return ConnectionGate(operation.strip(), output)


def parse_input(puzzle_input):
    gates = []

    for line in [l.strip() for l in puzzle_input if l]:
        gates.append(str_to_gate(line))

    return gates


def process_gates(gates):
    gates = list(gates)
    wires = {}
    while gates and 'a' not in wires:
        if gates[0].is_processable(wires):
            gates[0].process(wires)
            gates = gates[1:]
        else:
            gates = gates[1:] + [gates[0]]

    return wires


class Solution(SolutionBase):
    def __init__(self):
        super().__init__(2015, 7)

    def level1(self, example_input=False):
        with self.get_input_file(example_input) as f:
            gates = parse_input(f.readlines())

        wires = process_gates(gates)

        for key in wires:
            wires[key] = int(wires[key], 2)

        if 'a' in wires:
            return wires['a']
        return None

    def level2(self, example_input=False):
        with self.get_input_file(example_input) as f:
            gates = parse_input(f.readlines())

        wires = process_gates(gates)
        a = int(wires['a'], 2)

        for g in gates:
            if type(g) is ConnectionGate and g.output_wire == 'b':
                g.input_wire = str(a)

        wires = process_gates(gates)

        if 'a' in wires:
            return int(wires['a'], 2)
        return None
