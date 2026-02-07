import tkinter as tk
import frames.frame2 as frame2
import frames.frame_online as frame_online
import frames.add_app as add_app
#import functions.buttons
class Frame1(tk.Frame):
    def __init__(self,window):
        super().__init__(window)
        self.window = window
        self.label1 = tk.Label(self, text="Home")
        self.label1.grid(row=1)
        self.button3 = tk.Button(self, text="Testing",command= self.change_frame1)
        self.button1 = tk.Button(self, text="App Manager",command= self.change_frame2)
        self.button_online = tk.Button(self, text="Go to the Internet",command= self.change_frame3)

        self.button1.grid(row=2,column=1)
        self.button3.grid(row=3,column=1)
        self.button_online.grid(row=6,column=2)
    def change_frame1(self):
        self.window.change_frame(frame2.Frame2)
    def change_frame2(self):
        self.window.change_frame(add_app.AddApp)
    def change_frame3(self):
        self.window.change_frame(frame_online.FrameNet)
    
#    def launch(self):
 #       buttons.App_Launch.launch("","snake")
    def select(self):
        pass


