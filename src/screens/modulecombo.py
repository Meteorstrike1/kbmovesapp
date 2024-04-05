from kivy.network.urlrequest import UrlRequest
from kivy.properties import ObjectProperty, StringProperty
from kivymd.uix.screen import MDScreen
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from .modulelist import ModuleOneLineListItem
from kivymd.app import MDApp


class ModuleCombo(MDScreen):
    """
    Module combo search class, inherits from MDScreen.

    Attributes
    ----------
    self.results_list: list
        list for storing results
    self.module_name: None
        to be used for grabbing module namespace

    Methods
    -------
    __init__:
        Constructor for ModuleCombo object
    search_all_combos(module):
        Makes a request to search for all combinations, on success calls update_result method, on failure no_results
    update_result(req, result):
        Takes results from url request, clears widget if already exists, makes new widgets and adds to a list
    clear_results():
        Reset the spinner and title text and clears all the list widgets
    """

    combo_list = ObjectProperty(None)

    def __init__(self, **kw):
        self.module_name = None
        self.results_list = []
        super().__init__(**kw)

    def search_all_combos(self, module):
        """Makes a request to search moves in combo, on success calls update_result method, on failure no_results."""
        self.module_name = module
        req = UrlRequest(f"http://127.0.0.1:5000/{module}/all", on_success=self.update_result,
                         on_error=no_results, on_failure=no_results)

    def update_result(self, req, result):
        """Takes results from url request, clears widget if already exists, makes new widgets and adds to a list."""
        self.combo_list.clear_widgets()
        MDApp.get_running_app().clear_module_list()
        if len(result) == 0:
            no_results(req, error="Not found")
            return "no results"
        self.results_list = result
        module = self.module_name

        for item in range(len(self.results_list)):
            id = result[item]["id"]
            name = result[item]["name"]
            code = result[item]["code"]
            moves = result[item]["moves"]
            kick = result[item]["is_kick"]
            jump = result[item]["is_jump"]
            notes = result[item]["notes"]

            if notes is not None:
                notes_text = f"Notes: {notes}"
            else:
                notes_text = ""
            text = f"{id}. {name}"
            details = f"Combo ID: {code}\nMoves: {moves}\nKick: {kick}\nJump: {jump}\n{notes_text}"
            new_list = ModuleOneLineListItem(text=text, details=details, title=text, position=item, module=module,
                                             id=str(id))
            self.combo_list.add_widget(new_list)
            MDApp.get_running_app().module_list.append(new_list)


def no_results(req, error):
    """Opens pop up window if no results found."""
    pop = Popup(title="Not found", content=Label(text="No results found"), size_hint=(None, None), size=(300, 200))
    pop.open()
