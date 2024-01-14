
from dataclasses import dataclass


def remove_spaces_and_lower_case(s: str) -> str:
    return s.strip().lower().replace("'", "").replace(" ", "")


@dataclass
class Page:

    """
    Contains information about a taipy page in the taipy app.

    url_path: the url path after '/' that you can find this page.
    page_name: the page name which shows on the menu bar
    technology: Optional. The name of the technology with spaces removed and all lower case. Required if this is a technology page.
    """

    url_path: str
    page_name: str

    def convert_to_taipy_menu_page(self) -> tuple:
        return (self.url_path, self.page_name)
    
    def is_for_technology(self, technology_name: str) -> bool:
        if "_" in self.url_path:
            return remove_spaces_and_lower_case(technology_name) == self.url_path.split("_")[1]
        else:
            ## because only the "learn_{technology_name}" pages are eligible.
            return False

    