from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
import requests


class ReqRoot(BoxLayout):
    print requests.get("http://vg.no").headers


class TestA(BoxLayout):

    def __init__(self, **kwargs):
        super(TestA, self).__init__(**kwargs)
        print "it works"


class TestB(BoxLayout):
    pass


class ReqApp(App):

    def on_pause(self):
        return True


if __name__ == '__main__':
    ReqApp().run()
