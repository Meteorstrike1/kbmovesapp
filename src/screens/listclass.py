from kivymd.uix.list import OneLineListItem
from kivymd.uix.list import MDList
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivymd.uix.dialog.dialog import MDDialog
from kivymd.uix.button import MDFlatButton, MDRaisedButton, MDIconButton
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout


# class DialogContent(MDDialog):
#     pass


class MyOneLineListItem(OneLineListItem):
    def __init__(self, details, *args, **kwargs):
        self.dialog = None
        self.details = details
        super().__init__(*args, **kwargs)

    # def on_release(self):
    #     pop = Popup(title="Title", content=Label(text=self.details))
    #     pop.open()
    #     print("Something")

    # def on_release(self):
    #     dialog = MyDialog(title="Title", text=self.details)
    #     dialog.open()
    #
    #     print("Something")

    def on_release(self):
        self.dialog = MDDialog(title="Title", text=self.details, buttons=[MDIconButton(icon="close",
                    on_release=self.close_dialog, pos_hint={"x": 1, "y": 2})], height=200)

        # self.dialog = MDDialog(title="Title", text=self.details, buttons=[MDIconButton(icon="close",
        #             on_release=self.close_dialog, pos_hint={"x": 1, "y": 2})], height=200, size_hint=[0.8, 0.8], type="custom", content_cls=DialogContent())

        # self.dialog = MDDialog(title="Title", text=self.details, buttons=[MDIconButton(icon="close",
        #             on_release=self.close_dialog, pos_hint={"x": 1, "y": 2})], size_hint=(0.8, 0.8))

        # self.dialog.buttons = [MDFlatButton(text="CANCEL"), MDRaisedButton(text="DISCARD")]
        self.dialog.open()

        print("Something")

    # def on_release(self):
    #     self.dialog = MDDialog(title="Title", text=self.details, buttons=[MDIconButton(icon="close",
    #                 on_release=self.close_dialog, pos_hint={"x": 0, "y": 0}), MDRaisedButton(text="DISCARD")])
    #
    #     # self.dialog.buttons = [MDFlatButton(text="CANCEL"), MDRaisedButton(text="DISCARD")]
    #     self.dialog.open()
    #
    #     print("Something")

    # def on_release(self):
    #     self.dialog = MDDialog(title="Title", text=self.details)
    #
    #     self.dialog.buttons = [MDFlatButton(text="CANCEL"), MDRaisedButton(text="DISCARD")]
    #     self.dialog.open()
    #
    #     print("Something")

    # def on_release(self):
    #     self.dialog = MDDialog(title="Title", text=self.details)
    #
    #     self.dialog.buttons = [MDFlatButton(text="CANCEL", on_release=self.close_dialog), MDRaisedButton(text="DISCARD")]
    #     self.dialog.open()
    #
    #     print("Something")

    def close_dialog(self, instance):
        if self.dialog:
            self.dialog.dismiss()

    # def on_release(self):
    #     dialog = MDDialog(title="Title", text=self.details, buttons=[
    #                 MDFlatButton(text="CANCEL"), MDRaisedButton(text="DISCARD"),
    #             ])
    #     dialog.open()
    #
    #     print("Something")


# class MyDialog(MDDialog):
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#
#     def build(self):
#         self.buttons = [
#                     MDFlatButton(text="CANCEL"), MDRaisedButton(text="DISCARD"),
#                 ]


# def presser(self, pressed, details):
    #     pop = Popup(title="Title", content=Label(text=details))
    #     pop.open()
    #     print("Something")


class MyMDList(MDList):
    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

