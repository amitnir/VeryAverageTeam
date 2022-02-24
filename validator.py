from typing import List, Tuple

from utils import Project, Contributor, ProjectSolution


def validate_solution(solution: List[ProjectSolution]):
    for project_solution in solution:
        project = project_solution.project
        print(f'Parsing project {project.name}')
        contributors = project_solution.contributors
        assert len(project.skills) == len(contributors), 'Num of skills must match num of contributors'
        for skill, contributor in zip(project.skills, contributors):
            validate_contributor_skill_fit(skill, contributor, contributors)


def validate_contributor_skill_fit(skill: Tuple[str, int], main_contributor: Contributor, all_contributors: List[Contributor]):
    lang, level = skill
    if main_contributor.skills[lang] >= level:
        return
    if main_contributor.skills[lang] < level - 1:
        raise Exception(f'{main_contributor.name} level {main_contributor.skills[lang]} is less than required for the skill {skill}')
    for contributor in all_contributors:
        if contributor.skills[lang] >= level:
            return

    raise Exception(f'None of the contributors {[cont.name for cont in all_contributors]} has level required {skill}')