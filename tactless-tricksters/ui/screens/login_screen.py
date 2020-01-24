from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen


class LoginPair(BoxLayout):
    field = StringProperty()


class LoginScreen(Screen):

    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(name=kwargs.get('name'))
        self.util = kwargs.get('util')
