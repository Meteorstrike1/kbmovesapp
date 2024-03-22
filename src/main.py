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
