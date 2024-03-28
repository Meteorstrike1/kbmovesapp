from kivy.app import App
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.network.urlrequest import UrlRequest
from functools import partial
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from movesearch import MoveSearch
from beltcolour import BeltColour
from freeform import Freeform
from data.freeform1 import string
from movebuilder import MoveBuilder
from kivymd.uix.button import MDTextButton
from kivymd.uix.label import MDLabel
from kivymd.uix.dropdownitem import dropdownitem
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import MDScreenManager


class HomeWindow(MDScreen):
    # about = ObjectProperty(None)
    # disclaimer = ObjectProperty(None)
    # def about_screen(self):
    #
    #     return
    pass


class StartWindow(MDScreen):
    pass


class RefWindow(MDScreen):
    pass


class PracticeWindow(MDScreen):
    pass


class WindowManager(MDScreenManager):
    pass


kv = Builder.load_file("main.kv")

# sm = WindowManager()
#
# screens = [HomeWindow(name="home"), StartWindow(name="startpage"), RefWindow(name="reference"),
#            MoveSearch(name="movesearch"), BeltColour(name="beltcolour"), Freeform(name="freeform"),
#            PracticeWindow(name="practice"), MoveBuilder(name="movebuilder")]
# for screen in screens:
#     sm.add_widget(screen)
#
# sm.current = "home"


class KickboxingApp(MDApp):

    def build(self):
        self.sm = WindowManager()

        self.sm.add_widget(HomeWindow(name="home"))
        self.sm.add_widget(StartWindow(name="startpage"))
        self.sm.add_widget(RefWindow(name="reference"))
        self.sm.add_widget(MoveSearch(name="movesearch"))
        self.sm.add_widget(BeltColour(name="beltcolour"))
        self.sm.add_widget(Freeform(name="freeform"))
        self.sm.add_widget(PracticeWindow(name="practice"))
        self.sm.add_widget(MoveBuilder(name="movebuilder"))
        self.sm.current = "home"

        self.theme_cls.theme_style = "Dark"

        self.theme_cls.primary_palette = "Red"
        self.theme_cls.accent_palette = "Blue"
        return self.sm

        # return Builder.load_file("main.kv")


if __name__ == "__main__":
    KickboxingApp().run()


# TODO: - About, - Disclaimer