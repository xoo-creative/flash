from taipy import Gui
from taipy.gui import Markdown, State

result_ready = False

def change_content(state: State):
    """
    This function is responsible for changing the content of the GUI page.
    It takes a State object as input and updates the GUI with new content.
    """
    content = """
# Elm

## Onboarding 

Test onboarding section.
"""
    gui = state.get_gui()
    gui.add_page("result", Markdown(content))
    state.result_ready = True

page1_md="""# flash

## Click here to see your results!
<|button|on_action=change_content|>


<|part|render={result_ready}|class_name=card|
Click [**here**](/result) for your result!
|>

This application was created with [Taipy](https://www.taipy.io/).

"""

pages = {
    "page1": page1_md,
}

gui = Gui(pages=pages)





gui.run(debug=True, use_reloader=True)
