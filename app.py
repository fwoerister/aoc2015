import argparse
import importlib

if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='Advent of Code 2015')
    parser.add_argument('day', type=int)
    parser.add_argument('--part', type=int, default=1)
    parser.add_argument('--example-input', type=bool)
    args = parser.parse_args()

    solution = importlib.import_module(f'days.day{str(args.day).rjust(2, "0")}').Solution()

    result = solution.run(args.part, args.example_input)
    print(result)
