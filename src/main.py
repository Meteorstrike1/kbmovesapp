from kivy.app import App
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


class HomeWindow(Screen):
    pass


class StartWindow(Screen):
    pass


class RefWindow(Screen):
    pass


# class Freeform(Screen):
#     pass


class PracticeWindow(Screen):
    pass


class WindowManager(ScreenManager):
    FadeTransition()


kv = Builder.load_file("main.kv")

sm = WindowManager()

screens = [HomeWindow(name="home"), StartWindow(name="startpage"), RefWindow(name="reference"),
           MoveSearch(name="movesearch"), BeltColour(name="beltcolour"), Freeform(name="freeform"),
           PracticeWindow(name="practice"), MoveBuilder(name="movebuilder")]
for screen in screens:
    sm.add_widget(screen)

sm.current = "home"


class MyMainApp(App):

    def build(self):
        return sm


if __name__ == "__main__":
    MyMainApp().run()


# TODO: Pop up for errors
