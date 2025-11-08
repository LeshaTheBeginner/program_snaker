import tkinter as tk
import frame2
import buttons
import Importation
class Frame1(tk.Frame):
    def __init__(self,window):
        super().__init__(window)
        self.window = window
        self.label1 = tk.Label(self, text="Frame 1")
        self.label1.grid(row=1)
        self.button1 = tk.Button(self, text="Click Me",command= self.change_frame1)
        self.button2 = tk.Button(self, text="Test",command= self.launch)

        self.button1.grid(row=2,column=1)
        self.button2.grid(row=2,column=2)
        
    def change_frame1(self):
        self.window.change_frame(frame2.Frame2)
    
    def launch(self):
        buttons.App_Launch.launch("snake","snake")

