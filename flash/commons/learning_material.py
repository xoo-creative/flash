
from dataclasses import dataclass

from flash.commons.prompt import Prompt


@dataclass
class LearningMaterial:
    technology: str
    onboarding: str = None
    with_and_without: str = None
    core_concepts: str = None
    core_apis: str = None
    small_runnable_example: str = None
    real_life_examples: str = None

    def get(self, prompt: Prompt) -> str:
        return getattr(self, prompt.value)
    
    def set(self, prompt: Prompt, val: str) -> None:
        return setattr(self, prompt.value, val)
    
    def render(self) -> str:
        return "\n \n".join([self.onboarding, self.with_and_without, self.core_concepts, self.core_apis, self.small_runnable_example])