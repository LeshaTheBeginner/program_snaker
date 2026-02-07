"""Window for the Frames"""
import tkinter as tk
from frames.frame1 import Frame1
from frames.frame2 import Frame2
from frames.add_app import AddApp
from frames.frame_online import FrameNet
class Window(tk.Tk):
    """The Windows itself"""
    def __init__(self):
        """initialize"""
        super().__init__()
        self.geometry("600x400")
        self.frames={}
        for i in (Frame1,Frame2,AddApp,FrameNet):
            frame=i(self)
            self.frames[i] = frame
            frame.grid(row=0, column=0, sticky="nsew")  
        self.change_frame(Frame1)
    def change_frame(self,iframe):
        """change frame"""
        temp = self.frames[iframe]
        temp.tkraise()
iNo = Window()
iNo.mainloop()
