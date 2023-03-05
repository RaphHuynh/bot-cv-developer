from project.choices import Language, Framework, Tools, System
from dataclasses import dataclass


@dataclass
class Skill:
    language: Language
    framework: Framework
    tools: Tools
    system: System
