
from dataclasses import dataclass
import dataclasses
from enum import Enum


class Model(Enum):
    GPT_3_5 = "GPT-3.5"
    GPT_4 = "GPT-4"



@dataclass
class ModelUsage:
    model: Model
    usages_remaining: int

    def render(self) -> str:
        return f"{self.model.value} ({self.usages_remaining} free uses left)"
    
    def decrement(self, n: int = 1) -> None:
        self.usages_remaining -= n
        
