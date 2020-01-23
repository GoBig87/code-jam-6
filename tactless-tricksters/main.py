from kivymd.app import MDApp
from kivy.app import App

from kivy.factory import Factory

from kivy.core.text import LabelBase

from kivymd.uix.list import OneLineAvatarListItem

from kivy.uix.screenmanager import ScreenManager
from kivy.properties import StringProperty

   
LabelBase.register(
	name='font',
	fn_regular='font.otf'
) 


class NavigationItem(OneLineAvatarListItem):
    icon = StringProperty()
    
class AppLayout(ScreenManager):
	
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
			
	def go_to_nav(self):
		self.current = 'nav'
	
	
class MainApp(MDApp):
	
	def __init__(self, **kwargs):
		self.theme_cls.primary_palette = "Teal"
		super().__init__(**kwargs)
		
	def build(self):
		menu = Factory.AppLayout()
		self.root = menu
		
	
		


if __name__ == "__main__":
    MainApp().run()
