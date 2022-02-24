from typing import List
from utils import ProjectSolution


def get_score(project_solutions: List[ProjectSolution]):
    return sum(s.score for s in project_solutions)


