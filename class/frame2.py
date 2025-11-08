import tkinter as tk
import frame1
class Frame2(tk.Frame):
    def __init__(self,window):
        super().__init__(window)
        self.label2 = tk.Label(self, text="Frame 2")
        self.label2.pack(pady=20)
        self.button2 = tk.Button(self, text="Click Me",command=lambda: window.change_frame(frame1.Frame1))
        self.export_t = ""
        self.entry = tk.Entry(self, textvariable=self.export_t,bg='white')    
        self.button2.pack()
