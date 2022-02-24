import math
from copy import deepcopy
from dataclasses import dataclass
from typing import List, Dict, Tuple


@dataclass
class Contributor:
    name: str
    skills: Dict[str, int]
    next_available_day: int = 0

    def get_role_dist(self, skill):
        lang, level = skill
        if self.skills[lang] >= level:
            return self.skills[lang] - level
        return math.inf


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
    start_day: int = 0
    score: int = 0

    def __post_init__(self):
        self.start_day = max((c.next_available_day for c in self.contributors))
        self.score = self.project.get_final_score(self.start_day)

    def get_updated_contributors_state(self, contributors: List[Contributor]) -> List[Contributor]:
        """Update state of all contributors based on this solution"""
        contributors = deepcopy(contributors)
        next_available_day = self.start_day + self.project.duration
        for c in contributors:
            c.next_available_day = next_available_day
        return contributors
