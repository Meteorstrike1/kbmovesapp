from kivy.network.urlrequest import UrlRequest
from screens.moveresult import MoveResult, no_results

# Make a drop down menu but use normal search for now


class BeltColour(MoveResult):

    def search_by_belt(self):
        """Search by belt"""
        if self.user_search.text == "":
            return
        print(self.user_search.text)
        user_input = self.user_search.text
        colour = user_input.replace(" ", "%20")
        req = UrlRequest(f"http://127.0.0.1:5000/moves/belt/{colour.lower()}", on_success=self.got_list_json,
                         on_error=no_results, on_failure=no_results)
        self.clear_result()
        self.count = 0

