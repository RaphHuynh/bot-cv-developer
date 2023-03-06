import json
from json import JSONEncoder
from dataclasses import dataclass, field
from project.models import Skill, Education, Project, DeveloperExperience


@dataclass
class User(JSONEncoder):
    id_user: int = field(default=None)
    lastname: str = field(default=None)
    firstname: str = field(default=None)
    portfolio: str = field(default=None)
    github: str = field(default=None)
    description: str = field(default=None)
    education: Education = field(default=None)
    skill: Skill = field(default=None)
    education: Education = field(default=None)
    project: Project = field(default=None)
    developerExperience: DeveloperExperience = field(default=None)


