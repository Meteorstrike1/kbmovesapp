from kivymd.uix.list import OneLineListItem, ThreeLineListItem, MDList
from kivymd.uix.dialog.dialog import MDDialog
from .combomovedialog import MoveDialogContent
from kivymd.uix.card import MDCard
from kivymd.uix.button import MDFlatButton, MDRaisedButton, MDIconButton
from kivymd.app import MDApp
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.network.urlrequest import UrlRequest
from kivy.properties import ObjectProperty


class ModuleOneLineListItem(OneLineListItem):
    """
    One line list item class for displaying module combination objects.

    Attributes
    ----------
    self.dialog: None
        used with on_release method to create an MDDialog object (pop up for the move details)
    self.details: str
        string of details about the move, passed in from the results of search for moves when this object is created
    self.title: str
        title of the move, passed in from the results of search for moves when this object is created
    self.position: int
        position of the object in the list of results, to be used when navigating through dialogs

    Methods
    -------
    __init__(details, title, position):
        Constructor for move one item list object
    on_release():
        Creates an MDDialog object using the title and details passed into combination list object, this object has
        buttons to use the helper functions close_dialog, search_moves_in_combo, prev_item, and next_item
    close_dialog(instance):
        Close the dialog popup
    search_moves_in_combo(instance):
        Makes a request to search for the moves in the combo, on success calls show_moves method, on failure no_results
    next_item(instance):
        Closes current dialog, uses the MDApp attribute object list (which each of these created objects were saved to
        from the results of move search) to proceed to next item in the list, and use on_release method to call the
        dialog pop up, only IF the self.position is less than the length of the list - 1
    prev_item(instance):
        Closes current dialog, uses the MDApp attribute object list (which each of these created objects were saved to
        from the results of move search) to proceed to previous item in the list, and use on_release method to call the
        dialog pop up, only IF the self.position is greater than 0
    show_moves(req, result):
        Takes results from url request, adds moves to a custom box widget in a loop, adds an MDDialog & opens
    """

    move_details = ObjectProperty(None)
    move_popup = ObjectProperty(None)

    def __init__(self, details, title, position, module, id, *args, **kwargs):
        """Constructs all necessary attributes for the combination list object."""
        self.dialog = None
        self.details = details
        self.title = title
        self.position = position
        self.module = module
        self.id = id
        self.results_list = []
        super().__init__(*args, **kwargs)

    def on_release(self):
        """Creates MDDialog object with combination details and buttons for navigating."""
        self.dialog = MDDialog(title=self.title, text=self.details, buttons=[
            MDIconButton(icon="arrow-left-bold-outline", pos_hint={"x": -2, "y": 0.1}, on_release=self.prev_item),
            MDIconButton(icon="arrow-right-bold-outline", pos_hint={"x": -1.8, "y": 0.1}, on_release=self.next_item),
            MDRaisedButton(text="Move details", on_release=self.search_moves_in_combo),
            MDIconButton(icon="close", on_release=self.close_dialog, pos_hint={"x": 1, "y": 4.5})])
        self.dialog.open()

    def close_dialog(self, instance):
        """Closes dialog pop up."""
        if self.dialog:
            self.dialog.dismiss()

    def search_moves_in_combo(self, instance):
        """Makes a request to search moves in combo, on success calls show_moves method, on failure no_results."""
        req = UrlRequest(f"http://127.0.0.1:5000/{self.module}/combo_moves/{self.id}", on_success=self.show_moves,
                         on_error=no_results, on_failure=no_results)

    def next_item(self, instance):
        """Proceeds to open dialog of next item in list of combinations if it exists."""
        if self.position < len(MDApp.get_running_app().module_list) - 1:
            self.dialog.dismiss()
            MDApp.get_running_app().module_list[self.position + 1].on_release()

    def prev_item(self, instance):
        """Proceeds to open dialog of previous item in list of combinations if it exists."""
        if self.position > 0:
            self.dialog.dismiss()
            MDApp.get_running_app().module_list[self.position - 1].on_release()

    def show_moves(self, req, result):
        """Takes results from url request, adds moves to a custom box widget in a loop, adds to an MDDialog & opens"""
        if len(result) == 0:
            no_results(req, error="Not found")
            return "no results"
        self.results_list = result
        self.move_details = MoveDialogContent(md_bg_color="#c20404")

        for item in range(len(self.results_list)):
            name = result[item]["name"].capitalize()
            code = result[item]["code"]
            belt = result[item]["belt_colour"].capitalize()
            plan = result[item]["lesson_plan"]
            notes = result[item]["notes"]

            if notes is not None:
                notes_text = f"Notes: {notes}"
            else:
                notes_text = ""
            details = f"Move ID: {code} | Belt: {belt} | Lesson plan: {plan}"
            new_list = ThreeLineListItem(text=name, secondary_text=details, tertiary_text=notes_text)
            self.move_details.moves_popup.add_widget(new_list)

        self.move_popup = MDDialog()
        self.move_popup.add_widget(self.move_details)
        self.move_popup.open()


def no_results(req, error):
    """Opens pop up window if no results found."""
    pop = Popup(title="Not found", content=Label(text="No results found"), size_hint=(None, None), size=(300, 200))
    pop.open()
