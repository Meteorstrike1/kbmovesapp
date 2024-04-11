from kivymd.uix.dialog.dialog import MDDialog
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.list import OneLineListItem, ThreeLineListItem
from kivy.uix.label import Label


class MoveDialogContent(MDBoxLayout):
    pass


class MoveThreeLineList(ThreeLineListItem):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


        self.longlabel = Label(text=self.text, size_hint_y=None,
                              size = self.size, text_size=(None,None))
        # self.add_widget(self.longlabel)
        self.text = self.longlabel

# class MoveThreeLineList(ThreeLineListItem):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#
#         self.longlabel = Label(text=self.text, size_hint_y=None,
#                               size = self.size,
#                               height=self.texture_size[1],)
#         self.add_widget(self.longlabel)


class WrappingLabel(Label):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        text_size = (None, None),
        size_hint_y = None,
        size = self.size,
        height = self.texture_size[1],
        halign = "center",
        valign = "middle"
