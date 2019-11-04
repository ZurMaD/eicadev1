
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
    
    
from kivy.clock import Clock



import multiprocessing

kv = '''
<InterfaceView>:
    Button:
        text: 'teste'
        on_press: root.do_process()
    TextInput:
        text:'gaaa'
    TextInput:
        text:'1'        
'''

Builder.load_string(kv)


class InterfaceView(BoxLayout):
    
    def __init__(self, **kwargs):        
        super().__init__(**kwargs)

    def do_process(self):
        
        Clock.schedule_once(self.do_something, 2)
        
    def do_something(self):
        print("gaaaaaaaaaa")
        return True
        

class SimpleApp(App):
    def build(self):
        return InterfaceView()


if __name__ == '__main__':
    SimpleApp().run()