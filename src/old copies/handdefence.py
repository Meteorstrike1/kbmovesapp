from kivy.network.urlrequest import UrlRequest
from kivy.properties import ObjectProperty
from kivymd.uix.screen import MDScreen
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from screens.listclass import MoveOneLineListItem
from kivymd.app import MDApp


class HandDefence(MDScreen):
    """
    Hand defence search class, inherits from MDScreen.
    (Will change to a universal move class for all to inherit from but using this for now)

    Attributes
    ----------
    self.results_list: list
        list for storing results

    Methods
    -------
    __init__:
        Constructor for HandDefence object
    search_hand_defence():
        Makes a request to search by belt colour, on success calls update_result method, on failure no_results
    update_result(req, result):
        Takes results from url request, clears widget if already exists, makes new widgets and adds to a list
    update_label():
        Changes the button label and colour if switch between graded and all.
    clear_results():
        Reset the button and title text and clears all the list widgets
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
    toggle = ObjectProperty(None)
    subtitle = ObjectProperty(None)
    move_list = ObjectProperty(None)
    notes = ObjectProperty(None)

    def __init__(self, **kw):
        self.results_list = []
        super().__init__(**kw)

    def search_hand_defence(self):
        """Makes a request to search by toggle, on success calls update_result method, on failure no_results."""
        search = self.toggle.text
        req = UrlRequest(f"http://127.0.0.1:5000/moves/hand_defences/{search.lower()}", on_success=self.update_result,
                         on_error=no_results, on_failure=no_results)

    def update_result(self, req, result):
        """Takes results from url request, clears widget if already exists, makes new widgets and adds to a list."""
        self.move_list.clear_widgets()
        MDApp.get_running_app().clear_object_list()
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
            new_list = MoveOneLineListItem(text=text, details=details, title=name, position=item)
            self.move_list.add_widget(new_list)
            MDApp.get_running_app().object_list.append(new_list)

    def update_label(self):
        """Changes the button label and colour if switch between graded and all."""
        if self.toggle.text == "Graded":
            self.toggle.text = "All"
            self.toggle.md_bg_color = "green"
            self.subtitle.text = "All hand defences up to blackbelt"
        elif self.toggle.text == "All":
            self.toggle.text = "Graded"
            self.toggle.md_bg_color = "#1f6dff"
            self.subtitle.text = "21 for slide back (purple) and step back (brown white)"
        self.search_hand_defence()

    def clear_results(self):
        """Reset the button text and clears all the list widgets."""
        self.toggle.text = "Graded"
        self.move_list.clear_widgets()


def no_results(req, error):
    """Opens pop up window if no results found."""
    pop = Popup(title="Not found", content=Label(text="No results found"), size_hint=(None, None), size=(300, 200))
    pop.open()
