import json
from json import JSONEncoder
from project.choices import Language, Framework, Tools, System
from dataclasses import dataclass, field


@dataclass
class Skill(JSONEncoder):
    language: str = field(default=None)
    framework: str = field(default=None)
    tools: str = field(default=None)
    system: str = field(default=None)
