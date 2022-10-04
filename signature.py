from turtle import done
import kivy
import os
kivy.require('2.1.0') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.graphics import Color, Ellipse, Line

Window.clearcolor = (1, 1, 1, 1)

class CanvasWidget(Widget):
    def on_touch_down(self, touch):
        with self.canvas:
            Color(0, 0, 0)
            d = 10.
            #Ellipse(pos=(touch.x - d / 2, touch.y - d / 2), size=(d, d))
            touch.ud['line'] = Line(points=(touch.x, touch.y))
        print(touch)

    def on_touch_move(self, touch):
        touch.ud['line'].points += [touch.x, touch.y]


class SignatureApp(App):
    def build(self):
        #doneBtn = Button(text="Done", font_size=48)
        #doneBtn.bind(on_press=screenshot)
        return CanvasWidget()

def screenshot(instance):
    os.system('.\ShareX.exe -workflow "mailroom"')

if __name__ == '__main__':
    SignatureApp().run()