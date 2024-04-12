from kivy.network.urlrequest import UrlRequest
from screens.movesearch import MoveSearch, no_results


class LegDefence(MoveSearch):
    """
    Leg defence search class, inherits from MoveSearch.

    Methods
    -------
    search_hand_defence():
        Makes a request to search by belt colour, on success calls update_result method, on failure no_results
    clear_results():
        Reset and clears all the list widgets
    """

    def search_leg_defence(self):
        """Makes a request to search for all, on success calls update_result method, on failure no_results."""
        req = UrlRequest(f"http://127.0.0.1:5000/moves/leg_defences/all", on_success=self.update_result,
                         on_error=no_results, on_failure=no_results)

    def clear_results(self):
        """Reset and clears all the list widgets."""
        self.move_list.clear_widgets()
