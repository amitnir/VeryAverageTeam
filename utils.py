from copy import deepcopy
from dataclasses import dataclass
from typing import List, Dict, Tuple


@dataclass
class Contributor:
    name: str
    skills: Dict[str, int]

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
    contributors: List[Dict[Contributor, int]]  # Contributor -> next available day
    start_day: int = 0
    score: int = 0

    def __init__(self):
        self.start_day = max(self.contributors.values())
        self.score = self.project.get_final_score(self.start_day)

    def get_updated_contributors_state(self, contributors: Dict[Contributor, int]) -> Dict[Contributor, int]:
        """Update state of all contributors based on this solution"""
        contributors = deepcopy(contributors)
        next_available_day = self.start_day + self.project.duration
        for c in self.contributors:
            contributors[c] = next_available_day
        return contributors
