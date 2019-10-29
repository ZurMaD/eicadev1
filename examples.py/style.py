from kivy.lang import Builder

Builder.load_string('''
<-Button,-ToggleButton>:
    canvas:
        Color:
            rgba: [1, 0, 0, 1] if self.state == 'normal' else [0, 0, 1, 1]
        Rectangle:
            pos: self.pos
            size: self.size
        Color:
            rgba: 1, 1, 1, 1
        Rectangle:
            texture: self.texture
            size: self.texture_size
            pos: int(self.center_x - self.texture_size[0] / 2.), int(self.center_y - self.texture_size[1] / 2.)
''')

from os.path import abspath, dirname, join

from kivy.app import App
from kivy.resources import resource_add_path, resource_find
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button


class MainLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(MainLayout, self).__init__(**kwargs)
        self.add_widget(Button(text="Button1"))
        self.add_widget(Button(text="Button2"))

class MainApp(App):
    def build(self):
        return MainLayout()

if __name__ == '__main__':
    MainApp().run()