from dotenv import load_dotenv
from .utils import load_text
from src.commons.learning_material import LearningMaterial
from src.commons.prompt import Prompt
from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    SystemMessagePromptTemplate,
)

import logging

load_dotenv()


class Agent:

    def __init__(self, technology) -> None:
        
        self.openai_chat = ChatOpenAI(temperature=0)
        self.technology=technology
        self.learning_material = LearningMaterial(technology=technology)

    def write_section(self, section: Prompt, technology_name: str) -> str:
        try:
            requested_prompt = self.load_prompt(section)
        except:
            raise RuntimeError("Section title provided is not one of the valid sections. Please check the `prompts` folder for options.")
        
        if technology_name == "":
            raise RuntimeError("No technology name is provided, but it is required.")

        human_prompt_template = "{technology_name}"

        system_message_prompt = SystemMessagePromptTemplate.from_template(requested_prompt)
        human_message_prompt = HumanMessagePromptTemplate.from_template(human_prompt_template)

        chat_prompt = ChatPromptTemplate.from_messages(
            [system_message_prompt, human_message_prompt]
        )

        chat_response = self.openai_chat(
            chat_prompt.format_prompt(
                technology_name=technology_name
            ).to_messages()
        )

        return chat_response.content
    
    def load_prompt(self, prompt: Prompt) -> str:
        return U.load_text(f"../prompts/{prompt.value}.txt")


    def generate_core_concepts(self) -> str:

        logging.info("Writing'Core Concepts' section")

        self.learning_material.core_concepts = self.write_section(Prompt.CORE_CONCEPTS, self.technology)

        return self.learning_material.core_concepts

        
        
        # core_concepts_prompt = load_prompt("core-concepts")
        # human_prompt_template = "{technology_name}"

        # system_message_prompt = SystemMessagePromptTemplate.from_template(core_concepts_prompt)
        # human_message_prompt = HumanMessagePromptTemplate.from_template(human_prompt_template)

        # chat_prompt = ChatPromptTemplate.from_messages(
        #     [system_message_prompt, human_message_prompt]
        # )

        # self.core_principles = self.openai_chat(chat_prompt.format_prompt(technology_name=self.technology).to_messages())

        # return self.core_principles.content






