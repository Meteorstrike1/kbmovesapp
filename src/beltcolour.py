from kivy.network.urlrequest import UrlRequest
from screens.moveresult import MoveResult, no_results
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivymd.uix.screen import MDScreen
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivymd.uix.list import OneLineListItem
from kivymd.uix.list import MDList
from screens.listclass import MyOneLineListItem, MyMDList, MyTwoLineListItem

# Make a drop down menu but use normal search for now
# Testing list generation for now


class GeneratedList(MDList):
    def __init__(self, text, **kwargs):
        super().__init__(**kwargs)
        self.text = text
        new_list = OneLineListItem(text=text)
        self.add_widget(new_list)

    # def build(self):
    #     self.height

    # def update_list(self, name):
    #     self.result_name.text = f"Move name: {name}"



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
    # notes = ObjectProperty(None)  # Add this later, need to format properly
    user_search = ObjectProperty(None)
    toggle = ObjectProperty(None)
    search = ObjectProperty(None)
    my_list = ObjectProperty(None)
    notes = ObjectProperty(None)

    def __init__(self, **kw):
        self.count = 0
        self.results_list = []
        super().__init__(**kw)

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

    def search_for_id(self):
        belt = "orange white"
        colour = belt.replace(" ", "%20")
        req = UrlRequest(f"http://127.0.0.1:5000/moves/belt/{colour.lower()}", on_success=self.update_result,
                         on_error=no_results, on_failure=no_results)

    def update_result(self, req, result):
        """Working code"""
        self.my_list.clear_widgets()
        if len(result) == 0:
            no_results(req, error="Not found")
            return "no results"
        self.results_list = result

        # new_md_list = MyMDList
        # self.my_list.add_widget(new_md_list)

        for item in range(len(self.results_list)):
            id = result[item]["id"]
            name = result[item]["name"].capitalize()
            code = result[item]["code"]
            belt = result[item]["belt_colour"].capitalize().replace(" ", "/")
            plan = result[item]["lesson_plan"]
            module = result[item]["module_combo"]
            related = result[item]["related_moves"]
            notes = result[item]["notes"]
            # self.move_name.text = f"Name: {name}"
            # self.code.text = f"Move ID: {code}"
            # self.belt_colour.text = f"Belt: {belt}"
            # self.lesson_plan.text = f"Lesson plan: {plan}"
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
            # text2 = f"Name: {name} | ID: {code} | Belt: {belt} | Lesson plan: {plan}{module_text}{related_text}"
            details = f"Move ID: {code}\nBelt: {belt}\nLesson plan: {plan}\n{module_text}\n{related_text}\n{notes_text}"
            new_list = MyOneLineListItem(text=text, details=details, title=name)
            self.my_list.add_widget(new_list)

    # def update_result(self, req, result):
    #     """Two line list result but don't need"""
    #     self.my_list.clear_widgets()
    #     if len(result) == 0:
    #         no_results(req, error="Not found")
    #         return "no results"
    #     self.results_list = result
    #
    #     # new_md_list = MyMDList
    #     # self.my_list.add_widget(new_md_list)
    #
    #     for item in range(len(self.results_list)):
    #         id = result[item]["id"]
    #         name = result[item]["name"].capitalize()
    #         code = result[item]["code"]
    #         belt = result[item]["belt_colour"].capitalize()
    #         plan = result[item]["lesson_plan"]
    #         module = result[item]["module_combo"]
    #         related = result[item]["related_moves"]
    #         # self.move_name.text = f"Name: {name}"
    #         # self.code.text = f"Move ID: {code}"
    #         # self.belt_colour.text = f"Belt: {belt}"
    #         # self.lesson_plan.text = f"Lesson plan: {plan}"
    #         if module is not None:
    #             if id < 88:
    #                 module_text = f" | Module 1 combinations: {module.replace('M1_', '')}"
    #             else:
    #                 module_text = f" | Module 2 combinations: {module.replace('M2_', '')}"
    #         else:
    #             module_text = ""
    #         if related is not None:
    #             related_text = f" | Related moves: {related}"
    #         else:
    #             related_text = ""
    #         main_text = f"{name}"
    #         subtitle = f"ID: {code} | Belt: {belt} | Lesson plan: {plan}"
    #         details = f"More details e.g. Lesson plan: {plan}{module_text}{related_text}"
    #         new_list = MyTwoLineListItem(text=main_text, details=details, secondary_text=subtitle)
    #         self.my_list.add_widget(new_list)

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

def no_results(req, error):
    print(error)
    pop = Popup(title="Not found", content=Label(text="No results found"), size_hint=(None, None), size=(300, 200))
    pop.open()


def presser():
    print("Something")