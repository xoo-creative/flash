from dotenv import load_dotenv
from utils import load_prompt
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
        
        self.client = ChatOpenAI(temperature=0)
        self.technology=technology

    def generate_core_principles(self) -> str:

        logging.info("Started the request to OpenAI")
        
        core_concepts_prompt = load_prompt("core-concepts")
        human_prompt_template = "{technology_name}"

        system_message_prompt = SystemMessagePromptTemplate.from_template(core_concepts_prompt)
        human_message_prompt = HumanMessagePromptTemplate.from_template(human_prompt_template)

        chat_prompt = ChatPromptTemplate.from_messages(
            [system_message_prompt, human_message_prompt]
        )

        self.core_principles = self.client(chat_prompt.format_prompt(technology_name=self.technology).to_messages())

        return self.core_principles.content






