import pkg_resources
from flash.commons.prompt import Prompt

import logging


def load_text(path: str) -> str:
    """
    Load the text content from a file.

    Args:
        path (str): The path to the file.

    Returns:
        str: The content of the file.
    """
    logging.info(f"Reading from path {path}")
    with open(path, "r") as fp:
        return fp.read()
    
def load_prompt(prompt: Prompt) -> str:

    prompt_path = pkg_resources.resource_filename(package_or_requirement="flash", 
                                                  resource_name=f"prompts/{prompt.value}.txt")

    return load_text(prompt_path)