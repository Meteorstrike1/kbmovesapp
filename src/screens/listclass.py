from kivymd.uix.list import OneLineListItem, TwoLineListItem, MDList
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivymd.uix.dialog.dialog import MDDialog
from kivymd.uix.button import MDFlatButton, MDRaisedButton, MDIconButton
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout


class MoveOneLineListItem(OneLineListItem):
    def __init__(self, details, title, *args, **kwargs):
        self.dialog = None
        self.details = details
        self.title = title
        super().__init__(*args, **kwargs)

    def on_release(self):
        self.dialog = MDDialog(title=self.title, text=self.details, buttons=[
                    MDIconButton(icon="arrow-left-bold-outline", pos_hint={"x": -2, "y": 0.1}),
                    MDIconButton(icon="arrow-right-bold-outline", pos_hint={"x": -1.8, "y": 0.1}),
                    MDIconButton(icon="close", on_release=self.close_dialog, pos_hint={"x": 1, "y": 4.5})])
        self.dialog.open()
        # print("Something")

    def close_dialog(self, instance):
        if self.dialog:
            self.dialog.dismiss()


# class MyMDList(MDList):
#     def __init__(self, *args, **kwargs):
#
#         super().__init__(*args, **kwargs)

# class MyTwoLineListItem(TwoLineListItem):
#     def __init__(self, details, *args, **kwargs):
#         self.dialog = None
#         self.details = details
#         super().__init__(*args, **kwargs)
#
#     def on_release(self):
#         self.dialog = MDDialog(title="Title", text=self.details, buttons=[MDIconButton(icon="close",
#                     on_release=self.close_dialog, pos_hint={"x": 1, "y": 2})], height=200)
#
#         self.dialog.open()
#
#         print("Something")
#
#     def close_dialog(self, instance):
#         if self.dialog:
#             self.dialog.dismiss()