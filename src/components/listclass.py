from kivymd.uix.list import OneLineListItem
from kivymd.uix.dialog.dialog import MDDialog
from kivymd.uix.button import MDFlatButton, MDRaisedButton, MDIconButton
from kivymd.app import MDApp


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

    def __init__(self, details, title, position, *args, **kwargs):
        """Constructs all necessary attributes for the move list object."""
        self.dialog = None
        self.details = details
        self.title = title
        self.position = position
        super().__init__(*args, **kwargs)

    def on_release(self):
        """Creates MDDialog object with all of move details and buttons for navigating."""
        self.dialog = MDDialog(title=self.title, text=self.details, buttons=[
            MDIconButton(icon="arrow-left-bold-outline", pos_hint={"x": -2, "y": 0.1}, on_release=self.prev_item),
            MDIconButton(icon="arrow-right-bold-outline", pos_hint={"x": -1.8, "y": 0.1}, on_release=self.next_item),
            MDIconButton(icon="close", on_release=self.close_dialog, pos_hint={"x": 1, "y": 4.5})])
        self.dialog.open()
        # print(MDApp.get_running_app().object_list[self.position])
        # print("Something")

    def close_dialog(self, instance):
        """Closes dialog pop up."""
        if self.dialog:
            self.dialog.dismiss()

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
