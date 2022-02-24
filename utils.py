from dataclasses import dataclass
from typing import List, Dict


@dataclass
class Project:
    name: str
    duration: int
    score: int
    best_before: int
    skills: Dict[str, int]


@dataclass
class Contributor:
    name: str
    skills: Dict[str, int]
