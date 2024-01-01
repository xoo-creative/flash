
from dataclasses import dataclass


@dataclass
class LearningMaterial:
    technology: str
    onboarding: str = None
    with_and_without: str = None
    core_concepts: str = None
    core_apis: str = None
    small_runnable_example: str = None
    real_life_examples: str = None