from kivy.network.urlrequest import UrlRequest
from screens.movesearch import MoveSearch, no_results


class BeltColour(MoveSearch):
    """
    Belt colour search class, inherits from MoveSearch.

    Methods
    -------
    spinner_clicked(value):
        Sets the spinner value to the search text
    search_by_belt():
        Makes a request to search by belt colour, on success calls update_result method, on failure no_results
    clear_results():
        Reset the spinner and title text and clears all the list widgets
    """

    def spinner_clicked(self, value):
        """Sets the spinner value to the search text."""
        self.ids.user_search.text = value

    def search_by_belt(self):
        """Makes a request to search by belt colour, on success calls update_result method, on failure no_results."""
        if self.user_search.text == "":
            return
        user_input = self.user_search.text
        colour = user_input.replace(" ", "%20")
        req = UrlRequest(f"http://127.0.0.1:5000/moves/belt/{colour.lower()}", on_success=self.update_result,
                         on_error=no_results, on_failure=no_results)

    def clear_results(self):
        """Reset the spinner and title text and clears all the list widgets."""
        self.ids.spinner_id.text = "Belt colour"
        self.spinner_clicked("Choose a belt")
        self.move_list.clear_widgets()

