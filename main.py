from argparse import ArgumentParser

import output_file
from ProjectPicker import ProjectPicker, ProjectPickerOrderByDate
from assign_project import assignProjects
from input_file import InputFile
from output_file import generate_output_file
from solver import Solver
from validator import validate_solution
import scorer


def solve(input_file_name, proj_picker, assignees_picker):
    print(input_file_name)
    input_file = InputFile(input_file_name)
    contributors = input_file.contributors
    pp = proj_picker(input_file.projects, contributors)
    proj_solutions = []
    while(input_file.projects):
        curr_proj = pp.pick_project()
        ap = assignees_picker(curr_proj, contributors)
        ap_sol = ap.get_sol()
        if ap_sol is None:
            continue
        proj_solutions.append(ap_sol)
        print(scorer.get_score(proj_solutions))
    output_file.generate_output_file(proj_solutions, input_file_name + "_output.txt")



if __name__ == '__main__':
    # arg_parser = ArgumentParser(description='Amazing parser of google hash code')
    # arg_parser.add_argument('input_path', help='Path to an input file')
    # arg_parser.parse_args()
    solve(r'./input_data/a_an_example.in.txt', ProjectPicker, assignProjects)
    solve(r'./input_data/b_better_start_small.in.txt', ProjectPicker, assignProjects)
    solve(r'./input_data/c_collaboration.in.txt', ProjectPicker, assignProjects)
    solve(r'./input_data/d_dense_schedule.in.txt', ProjectPickerOrderByDate, assignProjects)
    solve(r'./input_data/e_exceptional_skills.in.txt', ProjectPicker, assignProjects)
    solve(r'./input_data/f_find_great_mentors.in.txt', ProjectPicker, assignProjects)

