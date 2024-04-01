from kivy.properties import ObjectProperty
from data.freeform1 import string
from kivymd.uix.screen import MDScreen


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

