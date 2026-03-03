from dataclasses import dataclass
from dataclasses import field
from typing import List


@dataclass
class Rule:
    id: str
    category: str
    tags: List[str]
    name: str
    description: str
    wrong_example: str
    correct_example: str
