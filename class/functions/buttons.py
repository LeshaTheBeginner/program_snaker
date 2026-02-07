import tkinter as tk
import os
from importation import Importation

class App_Launch(tk.Button):
    def __init__(self,path,image,app):
        super.__init__()
        self.app = app
        self.path = path
        self.image = image
    
    def launch(self,app):
        os.system(Importation.importt(app,app))

        
    
    

