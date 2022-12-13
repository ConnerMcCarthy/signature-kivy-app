import kivy
import os
kivy.require('2.1.0')

from time import sleep
from kivy.app import App
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.graphics import Color, Ellipse, Line
from kivy.uix.floatlayout import FloatLayout

Window.clearcolor = (1, 1, 1, 1)

#Displayed on a 2160 wide monitor
Window.size = (2160,400)
Window.left = True
Window.top = True

#Sets up the canvas background for the app
class CanvasWidget(Widget):
    #Creates the first point of a Line object when screen is touched 
    def on_touch_down(self, touch):
        with self.canvas:
            Color(0, 0, 0)
            #touch.ud means touch.update[name of object]
            touch.ud['line'] = Line(points=(touch.x, touch.y), width=4)

    #Adds another point to the Line object when the touch is moved
    def on_touch_move(self, touch):
        if(touch.profile != ['pos'] ):
            touch.ud['line'].points += [touch.x, touch.y]

#Builds the app
class SignatureApp(App):
    def build(self):
        
        #Window options
        Window.borderless = True
        parent = FloatLayout()
        self.painter = CanvasWidget(width=400)
        
        #Setting up done and clear buttons
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

    def clear(self, obj):
        self.painter.canvas.clear()

    #Calls shareX.exe to take a screenshot. Clears and disables the screen to prevent multiple screenshots
    def screenshot(self, obj):
        os.system('.\ShareX.exe -workflow "mailroom"')
        sleep(3)
        self.painter.canvas.clear()
        obj.disabled = False



if __name__ == '__main__':
    SignatureApp().run()