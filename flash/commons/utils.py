import pkg_resources
from flash.commons.page import Page
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


def escape_markdown(content: str) -> str:
    """
    Returns format-safe markdown str that can be passed into the taipy.Gui.Markdown function.
    """
    to_replace = {
        ">" : "\>",
        # "}" : "\}"
    }

    for old, new in to_replace.items():
        content = content.replace(old, new)
    
    return content


def _write_flash(content: str, path: str) -> str:

    """
    Writes `content` to a file in subfolder `/<project_root>/flash/{path}` 
    """

    flash_folder_path = pkg_resources.resource_filename("flash", "")

    file_path = f"{flash_folder_path}/{path}"

    logging.info(f"Writing content to {file_path}")

    with open(file_path, "w") as fp:
        fp.write(content)

def capitalize_each_word(words: str) -> str:
    return " ".join([word.capitalize() for word in words.split(" ")])

def technology_page_exists(technology: str, lop: list[Page]) -> bool:
    for page in lop:
        if page.is_for_technology(technology):
            return True
    return False

    
TEST_MD_CONTENT = """# Test Technology

## Onboarding

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

### What problem does this aim to solve?

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Cras semper auctor neque vitae tempus. At augue eget arcu dictum varius duis at. Tellus id interdum velit laoreet. Felis donec et odio pellentesque diam volutpat commodo. At imperdiet dui accumsan sit amet. In hac habitasse platea dictumst vestibulum. Iaculis at erat pellentesque adipiscing commodo elit at imperdiet. Fringilla phasellus faucibus scelerisque eleifend donec pretium. Curabitur gravida arcu ac tortor dignissim convallis. Aliquam sem et tortor consequat id porta nibh. Ac auctor augue mauris augue neque gravida.

### What sub-category of technologies is this?

Euismod elementum nisi quis eleifend quam adipiscing vitae proin. Mauris nunc congue nisi vitae suscipit tellus mauris a. Eget gravida cum sociis natoque penatibus et magnis dis parturient. Nunc mi ipsum faucibus vitae aliquet. Vulputate dignissim suspendisse in est ante in nibh. Duis ut diam quam nulla porttitor massa id neque. Donec ac odio tempor orci dapibus ultrices in iaculis nunc. Cras adipiscing enim eu turpis egestas. Etiam dignissim diam quis enim. Lacus viverra vitae congue eu consequat ac. Faucibus vitae aliquet nec ullamcorper sit amet risus. Eget nunc scelerisque viverra mauris in aliquam sem fringilla ut. Mattis ullamcorper velit sed ullamcorper morbi tincidunt ornare massa eget. Praesent tristique magna sit amet purus. Habitant morbi tristique senectus et. Condimentum id venenatis a condimentum vitae sapien. In fermentum et sollicitudin ac orci phasellus. Nisl tincidunt eget nullam non.
"""