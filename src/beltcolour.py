from kivy.network.urlrequest import UrlRequest
from screens.moveresult import MoveResult, no_results
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivymd.uix.screen import MDScreen
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivymd.uix.list import OneLineListItem
from kivymd.uix.list import MDList

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

    def __init__(self, **kw):
        super(BeltColour, self).__init__(**kw)

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
        id = 1
        req = UrlRequest(f"http://127.0.0.1:5000/moves/id/{id}", on_success=self.update_result,
                         on_error=no_results, on_failure=no_results)

    def update_result(self, req, result):
        id = result["id"]
        name = result["name"].capitalize()
        code = result["code"]
        belt = result["belt_colour"].capitalize()
        plan = result["lesson_plan"]
        module = result["module_combo"]
        related = result["related_moves"]
        # custom_list = GeneratedList(name)
        # self.add_widget(custom_list)
        # print(custom_list)
        text = f"Name: {name} | ID: {code} | Belt: {belt} | Lesson plan: {plan}"
        new_list = OneLineListItem(text=text)
        self.my_list.add_widget(new_list)
        # new_list = OneLineListItem(text=f"Name: {name} | ID: {code} | Belt: {belt} | Lesson plan: {plan}")
        # self.add_widget(new_list)
        print(result)
        # custom_list.update_list(name)

        # self.move_name.text = f"Name: {name}"
        # self.code.text = f"Move ID: {code}"
        # self.belt_colour.text = f"Belt: {belt}"
        # self.lesson_plan.text = f"Lesson plan: {plan}"
        # if module is not None:
        #     if id < 88:
        #         self.in_module.text = f"Module 1 combinations : {module.replace('M1_', '')}"
        #     else:
        #         self.in_module.text = f"Module 2 combinations : {module.replace('M2_', '')}"
        # else:
        #     self.in_module.text = ""
        # if related is not None:
        #     self.related_moves.text = f"Related moves: {related}"
        # else:
        #     self.related_moves.text = ""

def no_results(req, error):
    print(error)
    pop = Popup(title="Not found", content=Label(text="No results found"), size_hint=(None, None), size=(300, 200))
    pop.open()
