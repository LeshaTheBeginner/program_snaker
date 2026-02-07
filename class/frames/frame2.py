"""Frame for testing stuff"""
import tkinter as tk
import frames.frame1 as frame1
from functions.importation import Importation
class Frame2(tk.Frame):
    def __init__(self,window):
        super().__init__(window)
        self.label2 = tk.Label(self, text="Testing Frame")
        self.label2.pack(pady=20)
        self.button2 = tk.Button(self, text="Home",command=lambda: window.change_frame(frame1.Frame1))
        self.export_t = ""
        self.entry = tk.Entry(self, textvariable=self.export_t,bg='white')
        self.imp = Importation()
        self.button_list = tk.Button(self,text="Importation.change",command=lambda: self.imp.change("snake","ssnake","python3 /home/leshathebeginner/Documents/python/python_stuff/main.py"))
        self.importall_import = tk.Button(self,text="Importation.importall()",command=lambda: self.imp.importall(""))
        self.button2.pack()
        self.button_list.pack()
        self.importall_import.pack()
