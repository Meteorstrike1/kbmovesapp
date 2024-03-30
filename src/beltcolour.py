from kivy.network.urlrequest import UrlRequest
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivymd.uix.screen import MDScreen
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivymd.uix.list import OneLineListItem
from kivymd.uix.list import MDList
from screens.listclass import MoveOneLineListItem


# class GeneratedList(MDList):
#     def __init__(self, text, **kwargs):
#         super().__init__(**kwargs)
#         self.text = text
#         new_list = OneLineListItem(text=text)
#         self.add_widget(new_list)


class BeltColour(MDScreen):
    code = ObjectProperty(None)
    move_name = ObjectProperty(None)
    belt_colour = ObjectProperty(None)
    lesson_plan = ObjectProperty(None)
    related_moves = ObjectProperty(None)
    in_module = ObjectProperty(None)
    defence = ObjectProperty(None)
    kick = ObjectProperty(None)
    jump = ObjectProperty(None)
    user_search = ObjectProperty(None)
    toggle = ObjectProperty(None)
    search = ObjectProperty(None)
    move_list = ObjectProperty(None)
    notes = ObjectProperty(None)

    def __init__(self, **kw):
        self.count = 0
        self.results_list = []
        super().__init__(**kw)

    def spinner_clicked(self, value):
        self.ids.user_search.text = value

    def search_by_belt(self):
        if self.user_search.text == "":
            return
        print(self.user_search.text)
        user_input = self.user_search.text
        colour = user_input.replace(" ", "%20")
        req = UrlRequest(f"http://127.0.0.1:5000/moves/belt/{colour.lower()}", on_success=self.update_result,
                         on_error=no_results, on_failure=no_results)

    def update_result(self, req, result):
        """Working code"""
        self.move_list.clear_widgets()
        if len(result) == 0:
            no_results(req, error="Not found")
            return "no results"
        self.results_list = result

        for item in range(len(self.results_list)):
            id = result[item]["id"]
            name = result[item]["name"].capitalize()
            code = result[item]["code"]
            belt = result[item]["belt_colour"].capitalize()
            plan = result[item]["lesson_plan"]
            module = result[item]["module_combo"]
            related = result[item]["related_moves"]
            notes = result[item]["notes"]

            if module is not None:
                if id < 88:
                    module_text = f"Module 1 combinations: {module.replace('M1_', '')}"
                else:
                    module_text = f"Module 2 combinations: {module.replace('M2_', '')}"
            else:
                module_text = ""
            if related is not None:
                related_text = f"Related moves: {related}"
            else:
                related_text = ""
            if notes is not None:
                notes_text = f"Notes: {notes}"
            else:
                notes_text = ""
            text = f"{name}"
            details = f"Move ID: {code}\nBelt: {belt}\nLesson plan: {plan}\n{module_text}\n{related_text}\n{notes_text}"
            new_list = MoveOneLineListItem(text=text, details=details, title=name)
            self.move_list.add_widget(new_list)

    def clear_results(self):
        self.ids.spinner_id.text = "Belt colour"
        self.spinner_clicked("Choose a belt")
        self.move_list.clear_widgets()


def no_results(req, error):
    print(error)
    pop = Popup(title="Not found", content=Label(text="No results found"), size_hint=(None, None), size=(300, 200))
    pop.open()

