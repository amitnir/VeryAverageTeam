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

    def get_final_score(self, start_day):
        """returns score of the project"""
        return self.score - max(0, start_day + self.duration - self.best_before)


@dataclass
class ProjectSolution:
    project: Project
    contributors: List[Contributor]

    @property
    def start_day(self):
        return max(c.next_available_day for c in self.contributors)

    @property
    def score(self):
        return self.project.get_final_score(self.start_day)
