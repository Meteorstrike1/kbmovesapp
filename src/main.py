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
from kivy.properties import ListProperty


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


class MoveMenu(MDScreen):
    pass


class ComboMenu(MDScreen):
    pass


class PracticeWindow(MDScreen):
    pass


class WindowManager(MDScreenManager):
    pass


kv = Builder.load_file("main.kv")


class KickboxingApp(MDApp):
    """
    App class, inherits from MDApp.

    Attributes
    ----------
    object_list: ListProperty
        variable for storing list of objects globally so can be accessed across different widgets
    self.sm: WindowManager
        WindowManger instance

    Methods
    -------
    __init__:
        Constructor for App class
    build:
        Build method, add screens to window manager, set theme colours
    clear_object_list:
        Method to reset the object list to an empty list
    """

    object_list = ListProperty()

    def __init__(self, **kwargs):
        """Constructor for App class."""
        self.sm = WindowManager()
        super().__init__(**kwargs)

    def build(self):
        """Build method, add screens to window manager, set theme colours."""
        self.sm.add_widget(HomeWindow(name="home"))
        self.sm.add_widget(StartWindow(name="startpage"))
        self.sm.add_widget(RefWindow(name="reference"))
        self.sm.add_widget(MoveMenu(name="movemenu"))
        self.sm.add_widget(ComboMenu(name="combomenu"))
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

    def clear_object_list(self):
        """Method to reset the object list to an empty list."""
        self.object_list = []


if __name__ == "__main__":
    KickboxingApp().run()


# TODO: - About, - Disclaimer
