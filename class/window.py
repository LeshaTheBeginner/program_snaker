import tkinter as tk
from frame1 import *
from frame2 import *

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("400x300")
        self.frames={}
        for i in (Frame1,Frame2):
            frame=i(self)
            self.frames[i] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.change_frame(Frame1)
    def change_frame(self,iFrame):
        temp = self.frames[iFrame]
        temp.tkraise()

iNo = Window()
iNo.mainloop()


