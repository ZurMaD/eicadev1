import kivy
from kivy.app import App
from kivy.core.text import Label as CoreLabel
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.graphics import *
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window
kivy.require('1.0.6')  # replace with your current kivy version !

class ConnectApp(App):

    def build(self):
        return kv_file

class Menu(Screen):
    pass

class Setting(Screen):
    pass

class Main(Screen):
    board = [
        [2, 2, 2],
        [0, 0, 0],
        [1, 1, 1]
    ]
    hold_piece: bool = False
    temp = 0
    move_no = 0

    P1win = False
    P2win = False

    def __init__(self, **kwargs):
        super(Main, self).__init__(**kwargs)
        self.bind(pos=self.update_canvas)
        self.bind(size=self.update_canvas)
        self.update_canvas()

    def update_canvas(self, *args):
        self.canvas.clear()
        with self.canvas:
            get_indexes = lambda x, xs: [i for (y, i) in zip(xs, range(len(xs))) if x == y]
            for i in self.board:
                for index in get_indexes(1, i):
                    Color(1, 0, 0, 1)
                    Ellipse(pos=(self.size[0] * index * 0.25, self.size[1] * self.board.index(i) * 0.25 + self.size[1]*0.125),
                            size=(self.size[0] * 0.25, self.size[1] * 0.25))
                for index in get_indexes(2, i):
                    Color(0, 0, 1, 1)
                    Ellipse(pos=(self.size[0] * index * 0.25, self.size[1] * self.board.index(i) * 0.25 + self.size[1]*0.125),
                            size=(self.size[0] * 0.25, self.size[1] * 0.25))
            mylabel = CoreLabel(text="Reset", font_size=25, color=(1, 1, 1, 1))
            mylabel.refresh()
            texture = mylabel.texture
            Color(1, 1, 1, 1)
            Rectangle(pos=(self.size[0] * 0.8, self.size[1] * 0.65), size=(self.size[0] * 0.15, self.size[1] * 0.15), texture=texture)
            label2 = CoreLabel(text="Menu", font_size=25, color=(1, 1, 1, 1))
            label2.refresh()
            texture = label2.texture
            Color(1, 1, 1, 1)
            Rectangle(pos=(self.size[0] * 0.8, self.size[1] * 0.25), size=(self.size[0] * 0.15, self.size[1] * 0.15), texture=texture)

    def press(self, row, col):
        if self.move_no % 2 == 0:
            if self.board[row][col] == 2 and not self.hold_piece:
                self.temp = self.board[row][col]
                self.board[row][col] = 0
                self.hold_piece = True
            elif self.board[row][col] == 0 and self.hold_piece:
                self.board[row][col] = self.temp
                self.temp = 0
                self.hold_piece = False
                self.update_canvas()
                self.move_no += 1
            else:
                pass
        else:
            if self.board[row][col] == 1 and not self.hold_piece:
                self.temp = self.board[row][col]
                self.board[row][col] = 0
                self.hold_piece = True
            elif self.board[row][col] == 0 and self.hold_piece:
                self.board[row][col] = self.temp
                self.temp = 0
                self.hold_piece = False
                self.update_canvas()
                self.move_no += 1
                self.checkWin()
                self.wincon()
            else:
                pass

    def reset(self):

        self.board = [
        [2, 2, 2],
        [0, 0, 0],
        [1, 1, 1]]

        self.move_no = 0
        self.update_canvas()

    def checkWin(self):

        if self.board[0][0] == self.board[1][0] == self.board[2][0] == 1 or self.board[0][1] == self.board[1][1] == self.board[2][1] == 1 or self.board[0][2] == self.board[1][2] == self.board[2][2] == 1:
            self.P1win = True
        elif self.board[0][0] == self.board[0][1] == self.board[0][2] == 1 or self.board[1][0] == self.board[1][1] == self.board[1][2] == 1:
            self.P1win = True
        elif self.board[0][0] == self.board[1][1] == self.board[2][2] == 1 or self.board[0][2] == self.board[1][1] == self.board[2][0] == 1:
            self.P1win = True
        elif self.board[0][0] == self.board[1][0] == self.board[2][0] == 2 or self.board[0][1] == self.board[1][1] == self.board[2][1] == 2 or self.board[0][2] == self.board[1][2] == self.board[2][2] == 2:
            self.P2win = True
        elif self.board[2][0] == self.board[2][1] == self.board[2][2] == 2 or self.board[1][0] == self.board[1][1] == self.board[1][2] == 2:
            self.P2win = True
        elif self.board[0][0] == self.board[1][1] == self.board[2][2] == 2 or self.board[0][2] == self.board[1][1] == self.board[2][0] == 2:
            self.P2win = True
        else:
            pass

    def wincon(self):
        if self.P1win:
            print("Player 2 wins")
            pop(2)
        elif self.P2win:
            print("Player 1 wins")
            pop(1)
        else:
            pass

class p1_win():
    pass

class p2_win():
    pass

def pop(num):
    if num == 1:
        show = p1_win()
        popup = Popup(content=show, size_hint=(None, None), size =(400, 400))
    else:
        show = p2_win()
        popup = Popup(content=show, size_hint=(None, None), size=(400, 400))

    popup.open()

class WinManager(ScreenManager):
    pass


kv_file = Builder.load_string("""
WinManager:
    Menu:
    Main:
    Setting:

<Menu>:
    name: "menu"
    FloatLayout:
        Label:
            size_hint: 0.5, 0.25
            pos_hint: {"x": 0.25, "y": 0.7}
            text: "Connect 3"
            font_size: 40
            background_color: 1, 1, 1, 1
        Button:
            text: "Play"
            background_color: 0.4,1,0.4 ,1
            size_hint: 0.34, 0.16
            pos_hint: {"x":0.33, "y":0.3}
            on_press: root.manager.current = "main"
        Button:
            text: "Settings"
            background_color: 0.4, 1, 0.4, 1
            size_hint: 0.34, 0.16
            pos_hint: {"x":0.33, "y":0.1}
            on_press: root.manager.current = "setting"


<Main>:
    name: "main"
    FloatLayout:
        size: root.width, root.height

        Button:
            pos_hint:{"x":0.8 , "y":0.65}
            on_press: root.reset()
            size_hint: 0.15, 0.15

        Button:
            pos_hint:{"x":0.8 , "y":0.25}
            on_press:
                root.manager.transition.direction = 'right'
                root.manager.current = "menu"
            size_hint: 0.15, 0.15

        Button:
            pos_hint:{"x":0 , "y":0.125}
            text: "A1"
            on_press: root.press(0, 0)
            size_hint:0.25, 0.25
        Button:
            pos_hint:{"x":0 , "y":0.375}
            text: "A2"
            on_press: root.press(1, 0)
            size_hint:0.25, 0.25
        Button:
            pos_hint:{"x":0 , "y":0.625}
            text: "A3"
            on_press: root.press(2, 0)
            size_hint:0.25, 0.25
        Button:
            pos_hint:{"x":0.25 , "y":0.125}
            text: "B1"
            on_press: root.press(0, 1)
            size_hint:0.25, 0.25
        Button:
            pos_hint:{"x":0.25 , "y":0.375}
            text: "B2"
            on_press: root.press(1, 1)
            size_hint:0.25, 0.25
        Button:
            pos_hint:{"x":0.25 , "y":0.625}
            text: "B3"
            on_press: root.press(2, 1)
            size_hint:0.25, 0.25
        Button:
            pos_hint:{"x":0.5 , "y":0.125}
            text: "C1"
            on_press: root.press(0, 2)
            size_hint:0.25, 0.25
        Button:
            pos_hint:{"x":0.5 , "y":0.375}
            text: "C2"
            on_press: root.press(1, 2)
            size_hint:0.25, 0.25
        Button:
            pos_hint:{"x":0.5 , "y":0.625}
            text: "C3"
            on_press: root.press(2, 2)
            size_hint:0.25, 0.25

<Setting>:
    name: "setting"
    Label:
        size_hint: 0.5, 0.25
        pos_hint: {"x": 0.25, "y": 0.7}
        text: "I'm not smart enough to add settings"
    Button:
        text: "Go Back"
        background_color: 0.4,1,0.4 ,1
        size_hint: 0.34, 0.16
        pos_hint: {"x":0.33, "y":0.1}
        on_press:
            root.manager.transition.direction = 'right'
            root.manager.current = "menu"
""")

if __name__ == '__main__':
    #Window.fullscreen = True
    ConnectApp().run()