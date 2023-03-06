from json import JSONEncoder
from dataclasses import dataclass, field


@dataclass
class DeveloperExperience(JSONEncoder):
    job: str = field(default=None)
    date: str = field(default=None)
    employer: str = field(default=None)
    description: str = field(default=None)
    skill: str = field(default=None)
