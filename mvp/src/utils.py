def load_text(path):
    with open(path, "r") as fp:
        return fp.read()

def load_prompt(prompt):
    return load_text(f"../prompts/{prompt}.txt")
