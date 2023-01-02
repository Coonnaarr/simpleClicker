### write a program that will click the left mouse button every 0.01 seconds whilst pressing a key.

import time 
import threading 
from pynput.mouse import Button, Controller 
from pynput import keyboard

delay = 0.01 
button = Button.left
start_stop_key = keyboard.Key.f1
exit_key = keyboard.Key.f2

class ClickMouse(threading.Thread):
    def __init__(self, delay, button):
        super(ClickMouse, self).__init__()
        self.delay = delay
        self.button = button
        self.running = False 
        self.program_run = True

    def start_clicking(self):
        self.running = True

    def stop_clicking(self):
        self.running = False 

    def exit_clicking(self):
        self.stop_clicking()
        self.program_run = False 

    def run(self):
        while self.program_run: 
            while self.running:
                mouse.click(self.button)
                time.sleep(self.delay)
            time.sleep(0.1)
            
mouse = Controller()
thread = ClickMouse(delay, button)
thread.start()

def on_press(key):
    if key == start_stop_key:
        if thread.running:
            thread.stop_clicking()
        else:
            thread.start_clicking()
    elif key == exit_key:
        listener.stop()
        thread.exit_clicking()

with keyboard.Listener(on_press = on_press) as listener:
    listener.join()

