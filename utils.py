from dataclasses import dataclass
from typing import List, Dict, Tuple


@dataclass
class Project:
    name: str
    duration: int
    score: int
    best_before: int
    skills: List[Tuple[str, int]]


@dataclass
class Contributor:
    name: str
    skills: Dict[str, int]


class ProjectSolution:
    project: Project
    contributors: List[Contributor]