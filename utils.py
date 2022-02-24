from dataclasses import dataclass
from typing import List, Dict, Tuple


@dataclass
class Contributor:
    name: str
    skills: Dict[str, int]
    next_available_day: int

    def get_role_dist(self):
        """ returns distance if not relevant returns -1"""


@dataclass
class Role:
    skills: Dict[str, int]
    best_before: int
    duration: int


@dataclass
class Project:
    name: str
    Roles: List[Role]
    score: int
    duration: int

    def get_proj_score(self):
        """returns score of the project"""
        pass


class ProjectSolution:
    project: Project
    contributors: List[Contributor]
