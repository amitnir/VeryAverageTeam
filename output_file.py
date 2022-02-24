from typing import List
from utils import ProjectSolution


def generate_output_file(project_solutions: List[ProjectSolution]):
    output_lines = []
    output_lines.append(str(len(project_solutions)))
    for project_solution in project_solutions:
        output_lines.append(project_solution.project.name)
        output_lines.append(' '.join(c.name for c in project_solution.contributors))
    return '\n'.join(output_lines)
