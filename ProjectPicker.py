from typing import List

from utils import Contributor, Project


class ProjectPicker:
    def __init__(self, projects: List[Project], contributers: List[Contributor]):
        self.projects = projects
        self.contributes = contributers

    def pick_project(self):
        max_p = max(self.projects, key=lambda x: x.score)
        self.projects.remove(max_p)
        return max_p

class ProjectPickerOrderByDate(ProjectPicker):
    def pick_project(self):
        min_p = min(self.projects, key=lambda x: x.best_before)
        self.projects.remove(min_p)
        return min_p