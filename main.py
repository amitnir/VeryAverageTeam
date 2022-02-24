from argparse import ArgumentParser

from input_file import InputFile
from output_file import generate_output_file
from solver import Solver
from validator import validate_solution

if __name__ == '__main__':
    # arg_parser = ArgumentParser(description='Amazing parser of google hash code')
    # arg_parser.add_argument('input_path', help='Path to an input file')
    # arg_parser.parse_args()
    input_file = InputFile(r'./input_data/a_an_example.in.txt')
    # print(input_file.contributors)
    # print(input_file.projects)
    solution = Solver.solve_naive(input_file.projects, input_file.contributors)
    validate_solution(solution)
    print(solution)
    generate_output_file(solution)