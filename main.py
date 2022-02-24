from argparse import ArgumentParser

from input_file import InputFile
from solver import Solver

if __name__ == '__main__':
    # arg_parser = ArgumentParser(description='Amazing parser of google hash code')
    # arg_parser.add_argument('input_path', help='Path to an input file')
    # arg_parser.parse_args()
    input_file = InputFile(r'./input_data/b_better_start_small.in.txt')
    print(input_file.contributors)
    print(input_file.projects)