from kivy.network.urlrequest import UrlRequest
from kivy.properties import ObjectProperty
from screens.movesearch import MoveSearch, no_results


class HandDefence(MoveSearch):
    """
    Hand defence search class, inherits from MoveSearch.

    Methods
    -------
    search_hand_defence():
        Makes a request to search by belt colour, on success calls update_result method, on failure no_results
    update_label():
        Changes the button label and colour if switch between graded and all.
    clear_results():
        Reset the button and title text and clears all the list widgets
    """

    toggle = ObjectProperty(None)
    subtitle = ObjectProperty(None)

    def search_hand_defence(self):
        """Makes a request to search by toggle, on success calls update_result method, on failure no_results."""
        search = self.toggle.text
        req = UrlRequest(f"http://127.0.0.1:5000/moves/hand_defences/{search.lower()}", on_success=self.update_result,
                         on_error=no_results, on_failure=no_results)

    def update_label(self):
        """Changes the button label and colour if switch between graded and all."""
        if self.toggle.text == "Graded":
            self.toggle.text = "All"
            self.toggle.md_bg_color = "green"
            self.subtitle.text = "All hand defences up to blackbelt"
        elif self.toggle.text == "All":
            self.toggle.text = "Graded"
            self.toggle.md_bg_color = "#1f6dff"
            self.subtitle.text = "21 for slide back (purple) and step back (brown white)"
        self.search_hand_defence()

    def clear_results(self):
        """Reset the button text and clears all the list widgets."""
        self.toggle.text = "Graded"
        self.move_list.clear_widgets()
