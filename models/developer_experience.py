from dataclasses import dataclass
from project.models.skill import Skill


@dataclass
class DeveloperExperience:
    job: str
    date: str
    employer: str
    description: str
    skill: Skill
