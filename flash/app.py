# Import from standard library
import logging
from dotenv import load_dotenv

# Import from 3rd party libraries
from taipy.gui import Gui, notify, State, Markdown, navigate

# Import modules
from flash.agent.lambda_agent import LambdaAgent
from flash.commons.models import Model, ModelUsage
from flash.commons.page import Page, remove_spaces_and_lower_case
from flash.commons.utils import capitalize_each_word, escape_markdown

# Configure logger
logging.basicConfig(format="\n%(asctime)s\n%(message)s", level=logging.INFO, force=True)

load_dotenv()

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
    
    # Check if user still has enough requests of this model left
    if state.model.usages_remaining == 0:
        notify(state, "error", "The selected model has run out of free usages. Please choose a different model, or contact the creator.")
        return

    # Check if the user has put a topic
    if state.technology == "":
        notify(state, "error", "Please enter a technology you want to learn.")
        return
    
    if technology_page_exists(state):
        notify(state, "error", "This technology has already been generated for. Please check the left menu bar for the corresponding page!")
        return


    agent = LambdaAgent(state.technology.strip(), model=state.model.model, testing=False)

    state.n_requests += 1
    learning_material = agent.get_learning_material().strip().replace('"', "")
    learning_material = escape_markdown(learning_material)

    # Notify the user in console and in the GUI
    logging.debug(
        f"Technology: {agent.technology}\n"
        f"Learning Material: {learning_material}"
    )

    gui = state.get_gui()

    new_page_url = generate_page_url(agent.technology, state.level, state.model.model)
    new_page_name = generate_page_name(agent.technology, state.level, state.model.model)

    # These need to be changed together because taipy.gui's pages are actually not related to the menu pages.
    gui.add_page(new_page_url, Markdown(learning_material))
    state.list_of_pages.append(Page(new_page_url, new_page_name, remove_spaces_and_lower_case(agent.technology),
                                    state.level, state.model.model))

    # need this refresh to reload the menu
    state.refresh("list_of_pages")

    # update the num of requests left
    update_model_usage(state)
    state.refresh("list_of_model_usages")
    state.model = state.list_of_model_usages[0]   # default to first model, i.e. using GPT-3.5

    notify(state = state, 
           notification_type="success", 
           message=f"Your learning material should be ready to view in the new tab named \"{capitalize_each_word(agent.technology)}\"!",
           duration=5000)
    
def generate_page_name(technology: str, level: str, model: Model) -> str:
    return f"{capitalize_each_word(technology)}_{level.capitalize()}_{model.value}"
    
def generate_page_url(technology: str, level: str, model: Model) -> str:
    return f"learn_{remove_spaces_and_lower_case(technology)}_{level.lower()}_{model.name.lower()}"
    
def technology_page_exists(state: State) -> bool:
    for page in state.list_of_pages:
        logging.debug(f"User requested: {state.technology}, {state.level}, {state.model.model}")
        if page.matches(technology_name=state.technology, difficulty_level=state.level, model=state.model.model):
            return True
    return False
    
def update_model_usage(state: State) -> None:
    # need to update the number of requests left
    _found = False
    for model_usage in state.list_of_model_usages:
        if model_usage.model.value == state.model.model.value:
            _found = True
            model_usage.decrement()
    
    if not _found:
        logging.WARN(f"Could not find the user-selected model in list_of_model_usages {list_of_model_usages} using state {state}. No decrementing was performed.")

    # return list_of_model_usages

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


def make_menu_item(page: Page) -> str:
    return page.convert_to_taipy_menu_page()

def on_menu(state, action, info):
    page = info["args"][0]
    navigate(state, to=page)

# Variables
learning_material = ""
n_requests = 0

technology = "Elm"
level = "Beginner"

NUM_GPT3_5_REQUESTS = 10
NUM_GPT4_REQUESTS = 2

list_of_model_usages = [ModelUsage(Model.GPT_3_5, NUM_GPT3_5_REQUESTS), ModelUsage(Model.GPT_4, NUM_GPT4_REQUESTS)]
model: ModelUsage =list_of_model_usages[0]

list_of_pages = [Page("home", "Home")]



def make_model_usage_item(model_usage: ModelUsage) -> str:
    return model_usage.render()

root_md = """

<|container
<|menu|label=Menu|lov={list_of_pages}|on_action=on_menu|adapter=make_menu_item|>

<|content|>

<br/>

<br/>

**Code by [@tommysteryy](https://github.com/tommysteryy)**

Original code can be found [here](https://github.com/xoo-creative/flash).
|>

"""


homepage = """
# **flash**{: .color-primary} ⚡️

The best way to learn new technologies. For SWEs, by SWEs. Utilizing key teaching techniques from higher education.

<br/>

<|layout|columns=2 2 2 1|gap=30px|

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

<|card align-item-center|
### **Model**{: .color-primary}
<|{model}|selector|lov={list_of_model_usages}|dropdown|adapter=make_model_usage_item|>
|>

<|align-item-center |
<|Teach me!|button|on_action=generate|class_name=fullwidth|>
|>

|>

<br/>


"""

# stylekit = {
#     "color_background_dark": "#001845",
#     "color_paper_dark": "#002855",
#     "color-primary": "#ff462b",
#     "color_background_light": "#ade8f4",
#     "color_paper_light": "#90e0ef",
# }

pages = {
    "/": root_md,
    "home": homepage
}

if __name__ == "__main__":
    Gui(pages=pages).run(title='flash', use_reloader=True, debug=True, dark_mode=True)
