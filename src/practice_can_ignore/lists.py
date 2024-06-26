from kivy.lang import Builder
from kivymd.app import MDApp


class MainApp(MDApp):
    title = "Simple List"

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"

        return Builder.load_file("lists.kv")

    def presser(self, pressed, list_id):
        pressed.text = f"You pressed {list_id}"



MainApp().run()

# One line list item, two line list item, three line list item
