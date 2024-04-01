from kivy.network.urlrequest import UrlRequest
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from screens.moveresult import MoveResult, no_results


class MoveSearch(MoveResult):
    """
    Move search class, search by name or id, inheriting from MoveResult.
    Will probably retire this class and replace with BeltColour list generation method, this was just first step for me
    displaying results.
    """

    def call_search_type(self):
        """Switch method being used with the search box depending on the text selection."""
        if self.toggle.text == "By name":
            self.search_by_name()
        if self.toggle.text == "By id":
            self.search_by_id()

    def search_by_name(self):
        """Search by move name, calls got_list_json on success, no_results on failure."""
        if self.user_search.text == "":
            return
        print(self.user_search.text)
        user_input = self.user_search.text
        name = user_input.replace(" ", "%20")
        req = UrlRequest(f"http://127.0.0.1:5000/moves/name/{name}", on_success=self.got_list_json,
                         on_error=no_results, on_failure=no_results)
        self.clear_result()
        self.count = 0

    def search_by_id(self):
        """Search by id, calls got_move_json on success, no_results on failure, invalid_search if not int."""
        if self.user_search.text == "":
            return
        else:
            try:
                id = int(self.user_search.text)
            except ValueError:
                invalid_search(ValueError)
                return "invalid number"
        print(self.user_search.text)
        req = UrlRequest(f"http://127.0.0.1:5000/moves/id/{id}", on_success=self.got_move_json,
                         on_error=no_results, on_failure=no_results)
        self.clear_result()

    def update_label(self):
        """Changes the button label and colour if switch between id and name."""
        if self.toggle.text == "By name":
            self.toggle.text = "By id"
            self.toggle.md_bg_color = "green"
        elif self.toggle.text == "By id":
            self.toggle.text = "By name"
            self.toggle.md_bg_color = 0.3, 0.3, 1, 1
        self.user_search.text = ""
        self.clear_result()

    def clear_and_reset(self):
        """Calls clear_result (inherited method) and resets user_search text."""
        self.clear_result()
        self.user_search.text = ""


def invalid_search(error):
    """Pop up to warn user of invalid input."""
    print(error)
    pop = Popup(title="Invalid input", content=Label(text="Please search for a number"), size_hint=(None, None),
                size=(300, 200))
    pop.open()
