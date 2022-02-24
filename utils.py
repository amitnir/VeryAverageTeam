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
class Project:
    name: str
    duration: int
    score: int
    best_before: int
    skills: List[Tuple[str, int]]

    def get_proj_score(self):
        """returns score of the project"""
        pass


@dataclass
class ProjectSolution:
    project: Project
    contributors: List[Contributor]
