# Import from standard library
import logging
# from dotenv import load_dotenv

# Import from 3rd party libraries
from taipy.gui import Gui, notify, State, Markdown, navigate

# Import modules
from flash.agent.lambda_agent import LambdaAgent
from flash.commons.page import Page, remove_spaces_and_lower_case
from flash.commons.utils import capitalize_each_word, escape_markdown, technology_page_exists

# Configure logger
logging.basicConfig(format="\n%(asctime)s\n%(message)s", level=logging.INFO, force=True)

# load_dotenv()

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
    state.learning_material_ready = False

    # Check the number of requests done by the user
    if state.n_requests >= 5:
        error_too_many_requests(state)
        return

    # Check if the user has put a topic
    if state.technology == "":
        notify(state, "error", "Please enter a technology you want to learn.")
        return
    
    if technology_page_exists(state.technology, state.list_of_pages):
        notify(state, "error", "This technology has already been generated for. Please check the left menu bar for the corresponding page!")
        return

    agent = LambdaAgent(state.technology.strip(), testing=False)

    state.n_requests += 1
    learning_material = agent.get_learning_material().strip().replace('"', "")
    learning_material = escape_markdown(learning_material)

    # Notify the user in console and in the GUI
    logging.info(
        f"Technology: {agent.technology}\n"
        f"Learning Material: {learning_material}"
    )

    gui = state.get_gui()

    new_page_name = f"learn_{remove_spaces_and_lower_case(agent.technology)}"

    # These need to be changed together because taipy.gui's pages are actually not related to the menu pages.
    gui.add_page(new_page_name, Markdown(learning_material))
    state.list_of_pages.append(Page(new_page_name, capitalize_each_word(agent.technology)))

    # need this refresh to reload the menu
    state.refresh("list_of_pages")

    state.learning_material_ready = True

    notify(state = state, 
           notification_type="success", 
           message=f"Your learning material should be ready to view in the new tab named \"{capitalize_each_word(agent.technology)}\"!",
           duration=5000)

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
    notify(state, 'error', f"An unfortunate back-end error occurred. Please try again or come back later.")


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

def make_menu_item(page: Page) -> str:
    return page.convert_to_taipy_menu_page()

def on_menu(state, action, info):
    page = info["args"][0]
    navigate(state, to=page)

list_of_pages = [Page("home", "Home")]


root_md = """

<|container
<|menu|label=Menu|lov={list_of_pages}|on_action=on_menu|adapter=make_menu_item|>

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


"""

"""
<|part|render={learning_material_ready}|class_name=card|
## **Your Learning Material**{: .color-primary}
You can find your unique notes on a new tab called <|{technology}|> in the nav bar!
|>
"""

pages = {
    "/": root_md,
    "home": homepage
}

if __name__ == "__main__":
    Gui(pages=pages).run(title='flash', use_reloader=True, debug=True)
