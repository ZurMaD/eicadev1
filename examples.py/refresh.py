from kivy.app import runTouchApp
from kivy.factory import Factory

root = Factory.GridLayout(rows=4)
for i in range(4):
    root.add_widget(Factory.Label(text=str(i)))
runTouchApp(root)