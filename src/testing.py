from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen

# Builder.load_file("testing.kv")
#
# class MyLayout(Widget):
#     pass

class ButtonScreenOneScreen(MDScreen):
    pass


class AwesomeApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        # self.theme_cls.material_style = "M3"
        self.theme_cls.primary_palette = "DeepPurple"
        self.theme_cls.accent_palette = "Red"
        return Builder.load_file("testing.kv")

# `'Red'`, `'Pink'`, `'Purple'`, `'DeepPurple'`,
#     `'Indigo'`, `'Blue'`, `'LightBlue'`, `'Cyan'`, `'Teal'`, `'Green'`,
#     `'LightGreen'`, `'Lime'`, `'Yellow'`, `'Amber'`, `'Orange'`, `'DeepOrange'`,
#     `'Brown'`, `'Gray'`, `'BlueGray'

if __name__ == '__main__':
    AwesomeApp().run()
