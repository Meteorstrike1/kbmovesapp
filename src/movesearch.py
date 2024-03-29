from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.network.urlrequest import UrlRequest
from functools import partial
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.button import Button
from screens.moveresult import MoveResult, no_results


class MoveSearch(MoveResult):

    def call_search_type(self):
        if self.toggle.text == "By name":
            self.search_by_name()
        if self.toggle.text == "By id":
            self.search_by_id()

    def search_by_name(self):
        """Search by move name"""
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
        if self.toggle.text == "By name":
            self.toggle.text = "By id"
            self.toggle.md_bg_color = "green"
        elif self.toggle.text == "By id":
            self.toggle.text = "By name"
            self.toggle.md_bg_color = 0.3, 0.3, 1, 1
        self.user_search.text = ""
        self.clear_result()


def invalid_search(error):
    print(error)
    pop = Popup(title="Invalid input", content=Label(text="Please search for a number"), size_hint=(None, None),
                size=(300, 200))
    pop.open()
