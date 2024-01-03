from dotenv import load_dotenv
from flash.commons.utils import load_prompt
from flash.commons.learning_material import LearningMaterial
from flash.commons.prompt import Prompt
from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    SystemMessagePromptTemplate,
)

import logging

load_dotenv()


class Agent:

    def __init__(self, technology: str) -> None:
        """
        Initializes an Agent object.

        Parameters:
            technology (str): The name of the technology for the Agent.

        Returns:
            None
        """
        
        self.openai_chat = ChatOpenAI(temperature=0)
        self.technology=technology
        self.learning_material = LearningMaterial(technology=technology)

    def write_section(self, section: Prompt, technology_name: str) -> str:
        """
        Writes a section of the learning material.

        Parameters:
            section (Prompt): The section prompt to guide the content.
            technology_name (str): The name of the technology for the section.

        Returns:
            str: The content of the chat response.
        """
        # logging.info(f"Prompt value is {section.value}.")
        # try:
        requested_prompt = load_prompt(section)
        # except:
        #     raise RuntimeError("Section title provided is not one of the valid sections. Please check the `prompts` folder for options.")
        
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
    
    def generate_section(self, section_title: Prompt) -> str:
        """
        Generates a section of the learning material.

        Parameters:
            section_title (Prompt): The title prompt of the section.

        Returns:
            str: The content of the generated section.
        """
        logging.info(f"Writing {section_title.value} section")

        section_content = self.write_section(section_title, self.technology)
        self.learning_material.set(section_title, section_content)

        return section_content
    
    def generate_full(self) -> str:
        """
        Generates the full learning material and returns it as a string.

        Parameters:
            None

        Returns:
            str: The complete learning material as a string.
        """
        self.generate_section(Prompt.ONBOARDING)
        self.generate_section(Prompt.WITH_AND_WITHOUT)
        self.generate_section(Prompt.CORE_CONCEPTS)
        self.generate_section(Prompt.CORE_APIS)
        self.generate_section(Prompt.SMALL_RUNNABLE_EXAMPLE)
        return self.learning_material.render()

        
    





