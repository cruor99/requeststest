from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
import requests

class ReqRoot(BoxLayout):
    print requests.get("http://vg.no").headers


class ReqApp(App):
    def on_pause(self):
        return True


if __name__ == '__main__':
    ReqApp().run()
