import json
from json import JSONEncoder
from dataclasses import dataclass, field
from project.models.skill import Skill


@dataclass
class Project(JSONEncoder):
    title: str = field(default=None)
    description: str = field(default=None)
    date: str = field(default=None)
    skill: str = field(default=None)
