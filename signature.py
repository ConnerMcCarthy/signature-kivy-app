import kivy
import os
kivy.require('2.1.0') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.graphics import Color, Ellipse, Line
from kivy.uix.floatlayout import FloatLayout

Window.clearcolor = (1, 1, 1, 1)

class CanvasWidget(Widget):
    def on_touch_down(self, touch):
        with self.canvas:
            Color(0, 0, 0)
            touch.ud['line'] = Line(points=(touch.x, touch.y), width=2)

    def on_touch_move(self, touch):
        touch.ud['line'].points += [touch.x, touch.y]


class SignatureApp(App):
    def build(self):
        parent = FloatLayout()
        self.painter = CanvasWidget()
        doneBtn = Button(text='Sign', font_size=48, background_color='blue', size_hint=(.2,1), pos_hint={'right': 1})
        doneBtn.bind(on_release=self.screenshot)
        parent.add_widget(self.painter)
        parent.add_widget(doneBtn)
        return parent

    def screenshot(self, obj):
        os.system('.\ShareX.exe -workflow "mailroom"')
        self.painter.canvas.clear()

if __name__ == '__main__':
    SignatureApp().run()