def load_text(path):
    """
    Load the text content from a file.

    Args:
        path (str): The path to the file.

    Returns:
        str: The content of the file.
    """
    with open(path, "r") as fp:
        return fp.read()

def load_prompt(prompt):
    return load_text(f"prompts/{prompt}.txt")
