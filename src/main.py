from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.network.urlrequest import UrlRequest
from functools import partial
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget


class HomeWindow(Screen):
    pass


class StartWindow(Screen):
    code = ObjectProperty(None)
    move_name = ObjectProperty(None)
    belt_colour = ObjectProperty(None)
    related_moves = ObjectProperty(None)
    in_module = ObjectProperty(None)
    defence = ObjectProperty(None)
    kick = ObjectProperty(None)
    jump = ObjectProperty(None)
    notes = ObjectProperty(None)
    def get_move(self):
        # data = '{"id": "1"}'
        id = 1
        req = UrlRequest(f"http://127.0.0.1:5000/moves/id/{id}", on_success=self.got_json)
        # request = UrlRequest(f"http://127.0.0.1:5000/moves/id/{id}", on_success=self.got_json)
        # result = UrlRequest(f"localhost:5000/moves/id/{id}", req_body=data, on_success=self.got_json)
        print("it works?")
        # return req

    def update_label(self):
        print("It works?")

    def got_json(self, req, result):
        print(result)
        id = result["id"]
        name = result["name"].capitalize()
        code = result["code"]
        belt = result["belt_colour"].capitalize()
        module = result["module_combo"]
        related = result["related_moves"]
        self.move_name.text = f"Name: {name}"
        self.code.text = f"Move ID: {code}"
        self.belt_colour.text = f"Belt: {belt}"
        if module is not None:
            if id < 88:
                self.in_module.text = f"Module 1 combinations : {module}"
            else:
                self.in_module.text = f"Module 2 combinations : {module}"
        if related is not None:
            self.related_moves.text = f"Related moves: {related}"
        # for key, value in req.resp_headers.items():
        #     print('{}: {}'.format(key, value))
        # json = dict(request["data"])
        # print(json)
        print("it worked?")




class RefWindow(Screen):
    pass


class PracticeWindow(Screen):
    pass


class WindowManager(ScreenManager):
    FadeTransition()


kv = Builder.load_file("my.kv")

sm = WindowManager()

screens = [HomeWindow(name="home"), StartWindow(name="startpage"), RefWindow(name="reference"),
           PracticeWindow(name="practice")]
for screen in screens:
    sm.add_widget(screen)

sm.current = "home"


class MyMainApp(App):  # Inherits from App class
    def build(self):
        return sm


if __name__ == "__main__":
    MyMainApp().run()
