from kivymd.app import MDApp
from kivy.lang import Builder
from movesearch import MoveSearch
from beltcolour import BeltColour
from movebuilder import MoveBuilder
from handdefence import HandDefence
from legdefence import LegDefence
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import MDScreenManager
from kivy.properties import ListProperty
from screens.modulecombo import ModuleCombo
from kivy.properties import ObjectProperty
from data.freeform1 import string


class HomeWindow(MDScreen):
    # about = ObjectProperty(None)
    # disclaimer = ObjectProperty(None)
    pass


class StartWindow(MDScreen):
    pass


class RefWindow(MDScreen):
    pass


class MoveMenu(MDScreen):
    pass


class ComboMenu(MDScreen):
    pass


class ModuleOne(ModuleCombo):
    pass


class ModuleTwo(ModuleCombo):
    pass


class Freeform(MDScreen):
    """
    Freeform 1 inherits from MDScreen.

    Methods
    ----------
    make_appear:
        Sets freeform_text.text property to imported freeform 1 string, executes on screen load
    """

    freeform_text = ObjectProperty(None)

    def make_appear(self):
        """Sets freeform_text.text property to imported freeform 1 string, executes on screen load."""
        self.freeform_text.text = string


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
    module_list = ListProperty()

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
        self.sm.add_widget(HandDefence(name="handdefence"))
        self.sm.add_widget(LegDefence(name="legdefence"))
        self.sm.add_widget(Freeform(name="freeform"))
        self.sm.add_widget(ModuleOne(name="moduleone"))
        self.sm.add_widget(ModuleTwo(name="moduletwo"))
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

    def clear_module_list(self):
        """Method to reset the object list to an empty list."""
        self.module_list = []


if __name__ == "__main__":
    KickboxingApp().run()


# TODO: - About, - Disclaimer
