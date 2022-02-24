from utils import Contributor, Project


class InputFile:
    def __init__(self, file_path):
        self.file_path = file_path
        self.projects, self.contributors = self.parse_problem_info()
        self.all_skills = set([skill for contributor in self.contributors for skill in contributor.skills.keys()])
        self._fix_contributors()

    def _fix_contributors(self):
        for contributor in self.contributors:
            contributor_skills = set(contributor.skills.keys())
            for skill_lang in self.all_skills:
                if skill_lang not in contributor_skills:
                    contributor.skills[skill_lang] = 0

    def parse_problem_info(self):
        with open(self.file_path, 'r') as f:
            file_lines = f.readlines()

        num_contributors, num_projects = file_lines[0].split()
        num_contributors, num_projects = int(num_contributors), int(num_projects)
        file_lines = file_lines[1:]
        contributors, projects = [], []

        for idx in range(num_contributors):
            skills = {}
            name, num_skills = file_lines[0].split()
            num_skills = int(num_skills)
            file_lines = file_lines[1:]
            if num_skills == 0:
                contributors.append(Contributor(name, {}, 0))
                continue
            skill_lines = file_lines[:num_skills]
            for skill in skill_lines:
                lang, level = skill.split()
                level = int(level)
                skills[lang] = level
            file_lines = file_lines[num_skills:]
            contributors.append(Contributor(name, skills, 0))

        for idx in range(num_projects):
            skills = []
            project_name, duration, score, best_before, num_skills = file_lines[0].split()
            duration, score, best_before, num_skills = int(duration), int(score), int(best_before), int(num_skills)
            file_lines = file_lines[1:]
            if num_skills == 0:
                projects.append(Project(project_name, duration, score, best_before, []))
                continue
            skill_lines = file_lines[:num_skills]
            for skill in skill_lines:
                lang, level = skill.split()
                level = int(level)
                skills.append((lang, level))
            file_lines = file_lines[num_skills:]
            projects.append(Project(project_name, duration, score, best_before, skills))

        return projects, contributors
