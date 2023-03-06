import json
from json import JSONEncoder
from dataclasses import dataclass, field


@dataclass
class Education(JSONEncoder):
    degree: str = field(default=None)
    institution: str = field(default=None)
    date: str = field(default=None)
