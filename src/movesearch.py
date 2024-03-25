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


class MoveSearch(Screen):
    code = ObjectProperty(None)
    move_name = ObjectProperty(None)
    belt_colour = ObjectProperty(None)
    lesson_plan = ObjectProperty(None)
    related_moves = ObjectProperty(None)
    in_module = ObjectProperty(None)
    defence = ObjectProperty(None)
    kick = ObjectProperty(None)
    jump = ObjectProperty(None)
    # notes = ObjectProperty(None)  # Add this later, need to format properly
    user_search = ObjectProperty(None)
    toggle = ObjectProperty(None)
    search = ObjectProperty(None)

    def __init__(self, **kw):
        self.count = 0
        self.results_list = []
        super().__init__(**kw)

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
        elif self.toggle.text == "By id":
            self.toggle.text = "By name"

    def got_move_json(self, req, result):
        print(result)
        id = result["id"]
        name = result["name"].capitalize()
        code = result["code"]
        belt = result["belt_colour"].capitalize()
        plan = result["lesson_plan"]
        module = result["module_combo"]
        related = result["related_moves"]
        # note = result["notes"]
        self.move_name.text = f"Name: {name}"
        self.code.text = f"Move ID: {code}"
        self.belt_colour.text = f"Belt: {belt}"
        self.lesson_plan.text = f"Lesson plan: {plan}"
        if module is not None:
            if id < 88:
                self.in_module.text = f"Module 1 combinations : {module.replace('M1_', '')}"
            else:
                self.in_module.text = f"Module 2 combinations : {module.replace('M2_', '')}"
        if related is not None:
            self.related_moves.text = f"Related moves: {related}"
        else:
            self.related_moves.text = ""
        # if note is not None:
        #     self.notes.text = f"Notes: {note}"

    def got_list_json(self, req, result):
        """Initialises variables as first item of the list"""
        print(result)
        if len(result) == 0:
            return "no results"
        self.results_list = result
        id = result[0]["id"]
        name = result[0]["name"].capitalize()
        code = result[0]["code"]
        belt = result[0]["belt_colour"].capitalize()
        module = result[0]["module_combo"]
        related = result[0]["related_moves"]
        plan = result[0]["lesson_plan"]
        self.move_name.text = f"Name: {name}"
        self.code.text = f"Move ID: {code}"
        self.belt_colour.text = f"Belt: {belt}"
        self.lesson_plan.text = f"Lesson plan: {plan}"
        if module is not None:
            if id < 88:
                self.in_module.text = f"Module 1 combinations : {module.replace('M1_', '')}"
            else:
                self.in_module.text = f"Module 2 combinations : {module.replace('M2_', '')}"
        else:
            self.in_module.text = ""
        if related is not None:
            self.related_moves.text = f"Related moves: {related}"
        else:
            self.related_moves.text = ""
        print(self.count)
        print(self.results_list[self.count])

    def clear_result(self):
        self.move_name.text = "Name: "
        self.code.text = "Move ID: "
        self.belt_colour.text = "Belt: "
        self.lesson_plan.text = "Lesson plan: "
        self.in_module.text = "Module: "
        self.related_moves.text = "Related: "
        self.results_list = []

    def increase_count(self):
        if len(self.results_list) <= 1:
            return
        self.count += 1
        if self.count > len(self.results_list) - 1:
            self.count = 0
        id = self.results_list[self.count]["id"]
        name = self.results_list[self.count]["name"].capitalize()
        code = self.results_list[self.count]["code"]
        belt = self.results_list[self.count]["belt_colour"].capitalize()
        plan = self.results_list[self.count]["lesson_plan"]
        module = self.results_list[self.count]["module_combo"]
        related = self.results_list[self.count]["related_moves"]
        self.move_name.text = f"Name: {name}"
        self.code.text = f"Move ID: {code}"
        self.belt_colour.text = f"Belt: {belt}"
        self.lesson_plan.text = f"Lesson plan: {plan}"
        if module is not None:
            if id < 88:
                self.in_module.text = f"Module 1 combinations : {module.replace('M1_', '')}"
            else:
                self.in_module.text = f"Module 2 combinations : {module.replace('M2_', '')}"
        else:
            self.in_module.text = ""
        if related is not None:
            self.related_moves.text = f"Related moves: {related}"
        else:
            self.related_moves.text = ""

        print(self.count)
        print(self.results_list[self.count])

    def decrease_count(self):
        if len(self.results_list) <= 1:
            return
        self.count -= 1
        if self.count < 1:
            self.count = 0
        id = self.results_list[self.count]["id"]
        name = self.results_list[self.count]["name"].capitalize()
        code = self.results_list[self.count]["code"]
        belt = self.results_list[self.count]["belt_colour"].capitalize()
        plan = self.results_list[self.count]["lesson_plan"]
        module = self.results_list[self.count]["module_combo"]
        related = self.results_list[self.count]["related_moves"]
        self.move_name.text = f"Name: {name}"
        self.code.text = f"Move ID: {code}"
        self.belt_colour.text = f"Belt: {belt}"
        self.lesson_plan.text = f"Lesson plan: {plan}"
        if module is not None:
            if id < 88:
                self.in_module.text = f"Module 1 combinations : {module.replace('M1_', '')}"
            else:
                self.in_module.text = f"Module 2 combinations : {module.replace('M2_', '')}"
        else:
            self.in_module.text = ""
        if related is not None:
            self.related_moves.text = f"Related moves: {related}"
        else:
            self.related_moves.text = ""

        print(self.count)
        print(self.results_list[self.count])

def no_results(req, error):
    print(error)
    pop = Popup(title="Not found", content=Label(text="No results found"), size_hint=(None, None), size=(300, 200))
    pop.open()


def invalid_search(error):
    print(error)
    pop = Popup(title="Invalid input", content=Label(text="Please search for a number"), size_hint=(None, None),
                size=(300, 200))
    pop.open()
