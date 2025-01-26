from kivy.network.urlrequest import UrlRequest
from kivy.properties import ObjectProperty
# from components.movesearch import MoveSearch, no_results
from kivymd.uix.screen import MDScreen
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from components.sparringcombolist import SparringComboOneLineListItem
from kivymd.app import MDApp


class SparringCombo(MDScreen):
    """
    Sparring combo search class, inherits from MDScreen.

    Attributes
    ----------
    self.results_list: list
        list for storing results
    self.module_name: None
        to be used for grabbing module namespace

    Methods
    -------
    __init__:
        Constructor for SparringCombo object
    search_all_combos():
        Makes a request to search for all combinations, on success calls update_result method, on failure no_results
    update_result(req, result):
        Takes results from url request, clears widget if already exists, makes new widgets and adds to a list
    """

    combo_list = ObjectProperty(None)

    def __init__(self, **kw):
        self.results_list = []
        super().__init__(**kw)

    def search_all_combos(self):
        """Makes a request to search moves in combo, on success calls update_result method, on failure no_results."""
        req = UrlRequest(f"http://127.0.0.1:5000/sparring/all", on_success=self.update_result,
                         on_error=no_results, on_failure=no_results)

    def update_result(self, req, result):
        """Takes results from url request, clears widget if already exists, makes new widgets and adds to a list."""
        self.combo_list.clear_widgets()
        MDApp.get_running_app().clear_spar_combo_list()
        if len(result) == 0:
            no_results(req, error="Not found")
            return "no results"
        self.results_list = result

        for item in range(len(self.results_list)):
            id = result[item]["id"]
            attack = result[item]["attack"]
            defence = result[item]["defence"]
            code = result[item]["code"]
            belt = result[item]["belt_colour"].capitalize()
            moves = f"{result[item]["attack_id"]}, {result[item]["defence_id"]})"
            notes = result[item]["notes"]

            if notes is not None:
                notes_text = f"Notes: {notes}"
            else:
                notes_text = ""
            text = f"{belt}: {defence}"
            details = f"ID: {code}\nAttack: {attack}\nDefence: {defence}\nBelt: {belt}\nMoves: {moves}\n{notes_text}"
            new_list = SparringComboOneLineListItem(text=text, details=details, title=text, position=item, id=str(id))
            self.combo_list.add_widget(new_list)
            MDApp.get_running_app().spar_combo_list.append(new_list)


def no_results(req, error):
    """Opens pop up window if no results found."""
    pop = Popup(title="Not found", content=Label(text="No results found"), size_hint=(None, None), size=(300, 200))
    pop.open()
