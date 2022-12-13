import kivy
import os
kivy.require('2.1.0') # replace with your current kivy version !

from time import sleep
from kivy.app import App
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.graphics import Color, Ellipse, Line
from kivy.uix.floatlayout import FloatLayout

Window.clearcolor = (1, 1, 1, 1)
Window.size = (2160,400)
Window.left = True
Window.top = True

class CanvasWidget(Widget):
    def on_touch_down(self, touch):
        with self.canvas:
            Color(0, 0, 0)
            touch.ud['line'] = Line(points=(touch.x, touch.y), width=4)

    def on_touch_move(self, touch):
        if(touch.profile != ['pos'] ):
            touch.ud['line'].points += [touch.x, touch.y]


class SignatureApp(App):
    def build(self):
        Window.borderless = True
        parent = FloatLayout()
        self.painter = CanvasWidget(width=400)
        
        doneBtn = Button(text='Sign', font_size=48, background_color='blue', size_hint=(.15,1), pos_hint={'right': 1})
        doneBtn.bind(on_release=self.screenshot)
        doneBtn.bind(on_press=self.tempDisable)
        
        clearBtn = Button(text='Clear', font_size=48, background_color='red', size_hint=(.15,1), pos_hint={'right': .85})
        clearBtn.bind(on_press=self.clear)

        parent.add_widget(self.painter)
        parent.add_widget(clearBtn)
        parent.add_widget(doneBtn)
        return parent

    def tempDisable(self, obj):
        obj.disabled = True

    def screenshot(self, obj):
        os.system('.\ShareX.exe -workflow "mailroom"')
        sleep(3)
        self.painter.canvas.clear()
        obj.disabled = False

    def clear(self, obj):
        self.painter.canvas.clear()

if __name__ == '__main__':
    SignatureApp().run()