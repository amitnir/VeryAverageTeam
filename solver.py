from copy import copy, deepcopy
from typing import List

from utils import Project, Contributor, ProjectSolution


class Solver:
    @classmethod
    def solve_naive(cls, projects: List[Project], contributors: List[Contributor]):
        conts = deepcopy(contributors)
        projs = deepcopy(projects)
        projs = sorted(projs, key=lambda x: x.score, reverse=True)
        solution = []
        for project in projs:
            proj_indices = []
            proj_sol = ProjectSolution(project, [])
            for skill in project.skills:
                lang, level = skill
                for idx, cont in enumerate(conts):
                    if cont.skills[lang] >= level:
                        proj_sol.contributors.append(cont)
                        proj_indices.append(idx)
                        break
            if len(proj_sol.contributors) == len(project.skills):
                solution.append(proj_sol)
        return solution