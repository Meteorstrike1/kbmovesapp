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
from kivy.uix.dropdown import DropDown
from screens.moveresult import MoveResult, no_results

# Try just using the search class for now, grab some moves
# Read into drop down menu


# class CustomDropDown(DropDown):
#
#     def hello(self):
#         print("hello")



class MoveBuilder(MoveResult):
    # def __init__(self, **kw):
    #     super().__init__(**kw)
    #     self.dropdown = DropDown()
    #     self.add_widget(self.dropdown)
    def spinner_clicked(self, value):
        self.ids.user_search.text = value

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

    def hello(self):
        print("hello")


# class MoveBuilder(Screen):
#     def __init__(self, **kw):
#         super().__init__(**kw)
#         self.dropdown = DropDown()
#         self.add_widget(self.dropdown)

# class CustomDropDown(DropDown):
#     pass


# dropdown = CustomDropDown()
# mainbutton = Button(text="Select a belt", size_hint=(None, None))
# mainbutton.bind(on_release=dropdown.open)
# dropdown.bind(on_select=lambda instance, x: setattr(mainbutton, "text", x))
