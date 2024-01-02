# Import from standard library
import logging
import random
import re

# Import from 3rd party libraries
from taipy.gui import Gui, notify

# Import modules
from agent.agent import Agent
from flash.commons.prompt import Prompt

# Configure logger
logging.basicConfig(format="\n%(asctime)s\n%(message)s", level=logging.INFO, force=True)


def error_prompt_flagged(state, prompt):
    """Notify user that a prompt has been flagged."""
    notify(state, "error", "Prompt flagged as inappropriate.")
    logging.info(f"Prompt flagged as inappropriate: {prompt}")

def error_too_many_requests(state):
    """Notify user that too many requests have been made."""
    notify(state, "error", "Too many requests. Please wait a few seconds before generating another text or image.")
    logging.info(f"Session request limit reached: {state.n_requests}")
    state.n_requests = 1


# Define functions
def generate(state):
    """Generate Learning Materials."""
    state.learning_material = ""

    # Check the number of requests done by the user
    if state.n_requests >= 5:
        error_too_many_requests(state)
        return

    # Check if the user has put a topic
    if state.technology == "":
        notify(state, "error", "Please enter a technology you want to learn.")
        return

    agent = Agent(state.technology)

    state.n_requests += 1
    state.learning_material = agent.generate_full().strip().replace('"', "")
    

    # Notify the user in console and in the GUI
    logging.info(
        f"Technology: {state.technology}\n"
        f"Learning Material: {state.learning_material}"
    )
    notify(state, "success", "Ready to Learn!")



# Variables
learning_material = ""
n_requests = 0

technology = "Elm"
level = "Beginner"

# Called whever there is a problem
def on_exception(state, function_name: str, ex: Exception):
    """
    Logs the exception and the name of the function where the exception occurred.

    Args:
        state: Not used in this function.
        function_name (str): The name of the function where the exception occurred.
        ex (Exception): The exception that occurred.

    Returns:
        None
    """
    logging.error(f"Problem {ex} \nin {function_name}")
    notify(state, 'error', f"Problem {ex} \nin {function_name}")


# Markdown for the entire page
## <text|
## |text> 
## "text" here is just a name given to my part/my section
## it has no meaning in the code
page = """
<|container|
# **flash**{: .color-primary} ⚡️

The best way to learn new technologies. For SWEs, by SWEs. Utilizing key teaching techniques from higher education.

<br/>

<|layout|columns=2 2 1|gap=30px|

<|card align-item-center|

<technology|
### **Technology**{: .color-primary}
<|{technology}|input|label=Technology name|>
|technology>

|>

<|card align-item-center|

<level|
### **Level of Expertise**{: .color-primary}
<|{level}|selector|lov=Beginner;Intermediate;Expert|dropdown|>
|level>

|>

<|align-item-center |
<|I'm ready to learn!|button|on_action=generate|class_name=fullwidth|>
|>

|>

<br/>

---

<br/>

### **Generated Learning Material**{: .color-primary}

<|{learning_material}|input|multiline|label=Your learning material!|class_name=fullwidth rebuild|>

<br/>

**Code from [@tommysteryy](https://github.com/tommysteryy)**

Original code can be found [here](https://github.com/xoo-creative/flash)
|>
"""

if __name__ == "__main__":
    Gui(page).run(title='flash', use_reloader=True, debug=True)
