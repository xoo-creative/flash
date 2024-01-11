# Import from standard library
import logging
import datetime

# Import from 3rd party libraries
from taipy.gui import Gui, notify, State, Markdown

# Import modules
from flash.agent.lambda_agent import LambdaAgent
from flash.commons.utils import load_text, escape_markdown

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
def generate(state: State) -> None:
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

    agent = LambdaAgent(state.technology)

    state.n_requests += 1
    learning_material = agent.get_learning_material().strip().replace('"', "")
    learning_material = escape_markdown(learning_material)

    # Notify the user in console and in the GUI
    logging.info(
        f"Technology: {agent.technology}\n"
        f"Learning Material: {learning_material}"
    )

    gui = state.get_gui()
    gui.add_page("learn", Markdown(learning_material))

    state.learning_material_ready = True

    notify(state, "success", "Ready to Learn!")


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


# Variables
learning_material = ""
n_requests = 0

technology = "Elm"
level = "Beginner"
learning_material_ready = False
# Markdown for the entire page
## <text|
## |text> 
## "text" here is just a name given to my part/my section
## it has no meaning in the code

root_md = """
<|container|

<|content|>

<br/>

---

<br/>

**Code from [@tommysteryy](https://github.com/tommysteryy)**

Original code can be found [here](https://github.com/xoo-creative/flash)

|>

"""


homepage = """
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

<|part|render={learning_material_ready}|class_name=card|
## **Your Learning Material**{: .color-primary}
You can find your report about <|{technology}|> [here](/learn)
|>
"""

pages = {
    "/": root_md,
    "home": homepage
}

if __name__ == "__main__":
    # a = LambdaAgent("Apache Kafka")
    # result = a.get_learning_material()
    # print(result)
    Gui(pages=pages).run(title='flash', use_reloader=True, debug=True)
