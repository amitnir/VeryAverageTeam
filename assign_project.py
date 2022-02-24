from utils import *
import numpy as np


class assignProjects:
    def __init__(self, project: Project, contributors: List[Contributor]):
        self.con_list = contributors
        self.project = project

    def _get_best_contributor(self, skill: Tuple[str, int]):
        is_first = True
        for cont in self.con_list:
            if is_first:
                min_dist = cont.get_role_dist(skill)
                cur_cont = cont
                is_first = False
            else:
                cur_dist = cont.get_role_dist(skill)
                if min_dist > cur_dist:
                    min_dist = cur_dist
                    cur_cont = cont
        if min_dist == math.inf:
            return None
        return cur_cont

    def update_assignees(self, cont: Contributor):
        pass

    def get_sol(self) -> ProjectSolution:
        sol_con_list = list()
        for skill in self.project.skills:
            best_cont = self._get_best_contributor(skill)
            if best_cont is None:
                return None
            sol_con_list.append(best_cont)
        project_sol = ProjectSolution(project=self.project, contributors=sol_con_list)
        return project_sol

