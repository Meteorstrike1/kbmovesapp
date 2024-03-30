from kivymd.uix.list import OneLineListItem, TwoLineListItem, MDList
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivymd.uix.dialog.dialog import MDDialog
from kivymd.uix.button import MDFlatButton, MDRaisedButton, MDIconButton
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.app import MDApp


class MoveOneLineListItem(OneLineListItem):
    count = 0
    # object_list = MDApp.get_running_app().object_list
    def __init__(self, details, title, position, *args, **kwargs):
        self.dialog = None
        self.details = details
        self.title = title
        self.position = position
        MoveOneLineListItem.count += 1
        super().__init__(*args, **kwargs)

    def on_release(self):
        self.dialog = MDDialog(title=self.title, text=self.details, buttons=[
            MDIconButton(icon="arrow-left-bold-outline", pos_hint={"x": -2, "y": 0.1}, on_release=self.prev_item),
            MDIconButton(icon="arrow-right-bold-outline", pos_hint={"x": -1.8, "y": 0.1}, on_release=self.next_item),
            MDIconButton(icon="close", on_release=self.close_dialog, pos_hint={"x": 1, "y": 4.5})])
        self.dialog.open()
        print(MDApp.get_running_app().object_list[self.position])
        # print("Something")

    def close_dialog(self, instance):
        if self.dialog:
            self.dialog.dismiss()

    def next_item(self, instance):
        if self.position < len(MDApp.get_running_app().object_list) - 1:
            self.dialog.dismiss()
            MDApp.get_running_app().object_list[self.position + 1].on_release()

    def prev_item(self, instance):
        if self.position > 0:
            self.dialog.dismiss()
            MDApp.get_running_app().object_list[self.position - 1].on_release()





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