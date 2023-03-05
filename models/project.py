from dataclasses import dataclass
from project.models.skill import Skill


@dataclass
class Project:
    title: str
    description: str
    date: str
    skill: Skill
