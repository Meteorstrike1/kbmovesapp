from kivy.uix.screenmanager import Screen
from kivy.network.urlrequest import UrlRequest
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label


class MoveResult(Screen):
    """
    Displaying single and list results for the moves, inherits from Screen.

    Attributes
    ----------
    self.count
    self.results_list

    Methods
    -------
    got_move_json(req, result)
        For displaying the data of single result move requests

    got_list_json(req, result)
        Sets self.results_list to move request results for list searches and displays the first index

    increase_count()
        For increasing self.count and using it as index for self.results_list to update displayed results

    decrease_count()
        For decreasing self.count and using it as index for self.results_list to update displayed results

    """

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
        else:
            self.in_module.text = ""
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
            no_results(req, error="Not found")
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
