
from dataclasses import dataclass


@dataclass
class LearningMaterial:
    technology: str
    onboarding: str
    with_and_without: str
    core_concepts: str
    core_apis: str
    small_runnable_example: str
    real_life_examples: str = None