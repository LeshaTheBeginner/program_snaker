"""
Docstring for frame_online
requewst from a hardcoded url frame
"""
import sys
import tkinter as tk
#sys.path.insert(1,"~/Documents/python/python_stuff/class/functions")
#from network_connection import Requsting as net
import functions.network_connection as net
class FrameNet(tk.Frame):
    """init (self explanotary)"""
    def __init__(self,window):
        super().__init__(window)
        self.window = window
        self.inter = net.Requesting()
        self.name = tk.Label(self,text="INTERNEEET")
        self.the_label_in_question = tk.Label(self,text="")
        self.button = tk.Button(self,text="Connect and get butcoin price",command=self.label_it)
        self.name.grid(row=1)
        self.button.grid(row=2)
        self.the_label_in_question.grid(row=3)
    def label_it(self):
        """Literally just label the label in question with the internet getting"""
        print(self.inter.get_it())
