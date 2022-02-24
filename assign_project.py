from utils import *
import numpy as np


class assignProjects:
    def __init__(self, project: Project, contributors: List[Contributor]):
        self.con_list = contributors
        self.project = project

    def _get_best_contributor(self, skill: Tuple[str, int]):
        is_first = True
        for cont in self.con_list:
            if cont in self.sol_con_list:
                continue
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
        self.sol_con_list: List[Contributor] = list()
        for skill in self.project.skills:
            best_cont = self._get_best_contributor(skill)
            if best_cont is None:
                return None
            self.sol_con_list.append(best_cont)
        project_sol = ProjectSolution(self.project, self.sol_con_list)
        self.updated_contributors_state(project_sol, self.con_list)
        return project_sol

    def updated_contributors_state(self, proj_solution:ProjectSolution, contributors: List[Contributor]):
        """Update state of all contributors based on this solution"""
        next_available_day = proj_solution.start_day + proj_solution.project.duration
        for i, c in enumerate(self.sol_con_list):
            c.next_available_day = next_available_day
            skill = proj_solution.project.skills[i]
            if c.skills[skill[0]] <= skill[1]:
                c.skills[skill[0]] += 1
