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
from kivy.uix.scrollview import ScrollView
from kivy.properties import StringProperty

# Make a drop down menu but use normal search for now


class BeltColour(Screen):
    code = ObjectProperty(None)
    move_name = ObjectProperty(None)
    belt_colour = ObjectProperty(None)
    lesson_plan = ObjectProperty(None)
    related_moves = ObjectProperty(None)
    in_module = ObjectProperty(None)
    defence = ObjectProperty(None)
    kick = ObjectProperty(None)
    jump = ObjectProperty(None)
    notes = ObjectProperty(None)
    user_search = ObjectProperty(None)
    # scroll_list = ObjectProperty(None)

    def search_by_belt(self):
        """Search by belt"""
        if self.user_search.text == "":
            return
        print(self.user_search.text)
        user_input = self.user_search.text
        colour = user_input.replace(" ", "%20")
        req = UrlRequest(f"http://127.0.0.1:5000/moves/belt/{colour}", on_success=self.get_list_by_belt,
                         on_error=no_results, on_failure=no_results)
        # self.clear_result()


    def get_list_by_belt(self, req, result):
        if len(result) == 0:
            return "no results"
        move_list = []
        print(result)
        for i in range(len(result)):
            name = result[i]["name"]
            move_list.append(name)
            print(move_list)
        # for i in result:
        #     name = result["name"]
        #     print(name)
        #     move_list.append(name)
        string = ", ".join(move_list)
        ScrollableView.update_text(ScrollableView(), string)
        # return move_list


    # def got_list_json(self, req, result):
    #     """Temporary method for getting first from list"""
    #     print(result)
    #     if len(result) == 0:
    #         return "no results"
    #     id = result[0]["id"]
    #     name = result[0]["name"].capitalize()
    #     code = result[0]["code"]
    #     belt = result[0]["belt_colour"].capitalize()
    #     module = result[0]["module_combo"]
    #     related = result[0]["related_moves"]
    #     self.move_name.text = f"Name: {name}"
    #     self.code.text = f"Move ID: {code}"
    #     self.belt_colour.text = f"Belt: {belt}"
    #     if module is not None:
    #         if id < 88:
    #             self.in_module.text = f"Module 1 combinations : {module}"
    #         else:
    #             self.in_module.text = f"Module 2 combinations : {module}"
    #     else:
    #         self.in_module.text = ""
    #     if related is not None:
    #         self.related_moves.text = f"Related moves: {related}"
    #     else:
    #         self.related_moves.text = ""
    #     print("it worked?")
    # def got_move_json(self, req, result):
    #     print(result)
    #     id = result["id"]
    #     name = result["name"].capitalize()
    #     code = result["code"]
    #     belt = result["belt_colour"].capitalize()
    #     module = result["module_combo"]
    #     related = result["related_moves"]
    #     self.move_name.text = f"Name: {name}"
    #     self.code.text = f"Move ID: {code}"
    #     self.belt_colour.text = f"Belt: {belt}"
    #     if module is not None:
    #         if id < 88:
    #             self.in_module.text = f"Module 1 combinations : {module}"
    #         else:
    #             self.in_module.text = f"Module 2 combinations : {module}"
    #     if related is not None:
    #         self.related_moves.text = f"Related moves: {related}"
    #     print("it worked?")



    # def clear_result(self):
    #     self.move_name.text = "Name: "
    #     self.code.text = "Move ID: "
    #     self.belt_colour.text = "Belt: "
    #     self.in_module.text = "Module: "
    #     self.related_moves.text = "Related: "



class ScrollableView(ScrollView):
    # user_search = ObjectProperty(None)
    scroll_list = ObjectProperty(None)
    text = StringProperty('')
    # def search_by_belt(self):
    #     """Search by belt"""
    #     if BeltColour.user_search.text == "":
    #         return
    #     print(BeltColour.user_search.text)
    #     user_input = BeltColour.user_search.text
    #     colour = user_input.replace(" ", "%20")
    #     req = UrlRequest(f"http://127.0.0.1:5000/moves/belt/{colour}", on_success=self.get_list_by_belt,
    #                      on_error=no_results, on_failure=no_results)

    # def get_list_by_belt(self, req, result):
    #     if len(result) == 0:
    #         return "no results"
    #     move_list = []
    #     print(result)
    #     for i in range(len(result)):
    #         name = result[i]["name"]
    #         move_list.append(name)
    #         print(move_list)
    #     # for i in result:
    #     #     name = result["name"]
    #     #     print(name)
    #     #     move_list.append(name)
    #     string = ", ".join(move_list)
    #     self.scroll_list.text = string

    def update_text(self, string):
        self.scroll_list.text = string
        print(string)




def no_results(req, error):
    print(error)
    pop = Popup(title="Not found", content=Label(text="No results found"), size_hint=(None, None), size=(300, 200))
    pop.open()


def invalid_search(error):
    print(error)
    pop = Popup(title="Invalid input", content=Label(text="Please search for a number"), size_hint=(None, None),
                size=(300, 200))
    pop.open()