from enum import Enum, auto

class Prompt(Enum):
    CORE_APIS = "core-apis"
    CORE_CONCEPTS = "core-concepts"
    ONBOARDING = "onboarding"
    WITH_AND_WITHOUT = "with-and-without"
    SMALL_RUNNABLE_EXAMPLE = "small-runnable-example"
    REAL_LIFE_EXAMPLES = "real-life-examples"