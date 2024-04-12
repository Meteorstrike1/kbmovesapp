from kivymd.uix.list import OneLineListItem, ThreeLineListItem
from kivymd.uix.dialog.dialog import MDDialog
from .combomovedialog import MoveDialogContent, MoveThreeLineList
from kivymd.uix.button import MDFlatButton, MDRaisedButton, MDIconButton
from kivymd.app import MDApp
from kivy.metrics import dp, sp
from kivy.network.urlrequest import UrlRequest
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label


class MoveOneLineListItem(OneLineListItem):
    """
    One line list item class for displaying move objects.

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
        Creates an MDDialog object using the title and details passed into move list object, this object has buttons to
        use the helper functions close_dialog, prev_item, and next_item
    close_dialog(instance):
        Close the dialog popup
    next_item(instance):
        Closes current dialog, uses the MDApp attribute object list (which each of these created objects were saved to
        from the results of move search) to proceed to next item in the list, and use on_release method to call the
        dialog pop up, only IF the self.position is less than the length of the list - 1
    prev_item(instance):
        Closes current dialog, uses the MDApp attribute object list (which each of these created objects were saved to
        from the results of move search) to proceed to previous item in the list, and use on_release method to call the
        dialog pop up, only IF the self.position is greater than 0
    """

    move_details = ObjectProperty(None)
    move_popup = ObjectProperty(None)

    def __init__(self, details, title, position, id, related, module, *args, **kwargs):
        """Constructs all necessary attributes for the move list object."""
        self.dialog = None
        self.details = details
        self.title = title
        self.position = position
        self.id = id
        self.related = related
        self.module = module
        self.results_list = []
        super().__init__(*args, **kwargs)

    def on_release(self):
        """Creates MDDialog object with all of move details and buttons for navigating."""
        buttons_list = []
        left = MDIconButton(icon="arrow-left-bold-outline", pos_hint={"y": 0.08}, on_release=self.prev_item)
        right = MDIconButton(icon="arrow-right-bold-outline", pos_hint={"y": 0.08}, on_release=self.next_item)
        exit = MDIconButton(icon="close", on_release=self.close_dialog, pos_hint={"x": 1, "y": 5.1})
        buttons_list.append(MDIconButton(icon="close", opacity=0, disabled=True, pos_hint={"y": 0.12}))
        if self.related:
            buttons_list.append(MDRaisedButton(text="Related", md_bg_color="green", pos_hint={"y": 0.12},
                                               on_release=self.search_related_moves))
        else:
            buttons_list.append(MDRaisedButton(text="Related", opacity=0, disabled=True, pos_hint={"y": 0.12}))
        buttons_list.append(MDRaisedButton(text="", opacity=0, disabled=True, pos_hint={"y": 0.12}))
        buttons_list.append(left)
        buttons_list.append(right)
        buttons_list.append(MDIconButton(icon="close", opacity=0, disabled=True, pos_hint={"y": 0.12}))
        if self.module:
            buttons_list.append(MDRaisedButton(text="Combinations", md_bg_color="#1f6dff", pos_hint={"y": 0.12},
                                               on_release=self.search_combos_from_move))
        else:
            buttons_list.append(MDRaisedButton(text="Combinations", opacity=0, disabled=True, pos_hint={"y": 0.12}))
        buttons_list.append(exit)
        self.dialog = MDDialog(title=self.title, text=self.details, buttons=buttons_list)
        self.dialog.open()

    def close_dialog(self, instance):
        """Closes dialog pop up."""
        if self.dialog:
            self.dialog.dismiss()

    def search_related_moves(self, instance):
        """Makes a request to search moves in combo, on success calls show_moves method, on failure no_results."""
        req = UrlRequest(f"http://127.0.0.1:5000/moves/related_moves/{self.id}", on_success=self.show_moves,
                         on_error=no_results, on_failure=no_results)

    def search_combos_from_move(self, instance):
        """Makes a request to search moves in combo, on success calls show_moves method, on failure no_results."""
        req = UrlRequest(f"http://127.0.0.1:5000/moves/module_combos/{self.id}", on_success=self.show_combos,
                         on_error=no_results, on_failure=no_results)

    def next_item(self, instance):
        """Proceeds to open dialog of next item in list of objects if it exists."""
        if self.position < len(MDApp.get_running_app().object_list) - 1:
            self.dialog.dismiss()
            MDApp.get_running_app().object_list[self.position + 1].on_release()

    def prev_item(self, instance):
        """Proceeds to open dialog of previous item in list of objects if it exists."""
        if self.position > 0:
            self.dialog.dismiss()
            MDApp.get_running_app().object_list[self.position - 1].on_release()

    def show_moves(self, req, result):
        """Takes results from url request, adds moves to a custom box widget in a loop, adds to an MDDialog & opens"""
        if len(result) == 0:
            no_results(req, error="Not found")
            return "no results"
        self.results_list = result
        self.move_details = MoveDialogContent(md_bg_color="#0c6e01")

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

    def show_combos(self, req, result):
        """Takes results from url request, adds moves to a custom box widget in a loop, adds to an MDDialog & opens"""
        if len(result) == 0:
            no_results(req, error="Not found")
            return "no results"
        self.results_list = result
        self.move_details = MoveDialogContent(md_bg_color="#0228e3")

        for item in range(len(self.results_list)):
            id = result[item]["id"]
            name = result[item]["name"]
            code = result[item]["code"][0:2]
            kick = result[item]["is_kick"]
            jump = result[item]["is_jump"]
            notes = result[item]["notes"]

            if notes is not None:
                notes_text = f"Notes: {notes}"
            else:
                notes_text = ""
            if code == "M1":
                module = "Module 1"
            else:
                module = "Module 2"
            details = f"{module} | {id} | Kick: {kick} | Jump: {jump}"
            new_list = ThreeLineListItem(text=name, secondary_text=details, tertiary_text=notes_text)
            self.move_details.moves_popup.add_widget(new_list)

        self.move_popup = MDDialog()
        self.move_popup.add_widget(self.move_details)
        self.move_popup.open()


def no_results(req, error):
    """Opens pop up window if no results found."""
    pop = Popup(title="Not found", content=Label(text="No results found"), size_hint=(None, None), size=(300, 200))
    pop.open()
