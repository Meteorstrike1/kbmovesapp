from kivy.network.urlrequest import UrlRequest
from kivy.properties import ObjectProperty
from screens.movesearch import MoveSearch, no_results


class MoveByName(MoveSearch):
    """
    Move search class, search by name or id, inheriting from MoveResult.
    Will probably retire this class and replace with BeltColour list generation method, this was just first step for me
    displaying results.

    Methods
    -------
    search_by_name():
        Makes a request to search by belt colour, on success calls update_result method, on failure no_results
    clear_results():
        Clears list widgets and resets user_search text
    """

    user_search = ObjectProperty(None)

    def search_by_name(self):
        """Makes a request to search by name, on success calls update_result method, on failure no_results"""
        if self.user_search.text == "":
            return
        user_input = self.user_search.text
        name = user_input.replace(" ", "%20")
        req = UrlRequest(f"http://127.0.0.1:5000/moves/name/{name}", on_success=self.update_result,
                         on_error=no_results, on_failure=no_results)

    def clear_and_reset(self):
        """Clears list widgets and resets user_search text."""
        self.move_list.clear_widgets()
        self.user_search.text = ""
