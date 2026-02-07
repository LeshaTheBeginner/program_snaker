"""Class for editing apps.csv"""
import tkinter as tk
from tkinter import messagebox
from functions.importation import Importation
import os
import frames.frame1 as frame1
class AddApp(tk.Frame):
    """The Frame For Application Managment"""
    def __init__(self,window):
        super().__init__(window)
        self.window = window
        #self.config(background="#2a2a2b")
        self.AppList = tk.Listbox(self)
        self.imp = Importation()
        self.updater()
        self.selected = ""

        self.AppList.bind("<<ListboxSelect>>",self.naming)

        self.export_name = tk.Entry(self,text="export_name",)
        self.export_name_label = tk.Label(self,text="Name")
        self.export_path = tk.Entry(self,text="path")
        self.export_path_label = tk.Label(self,text="Path")
        self.export_button = tk.Button(self, text="export",command=lambda: self.app_export())
        self.filler = tk.Label(self,text=" ")
        
        #self.delete_name = tk.Entry(self,textvariable="ssnake")

        #self.import_button = tk.Button(self, text="import",command=self.app_export())
        #self.import_name = tk.Entry(self,textvariable="import_name")

        self.button1 = tk.Button(self, text="Home",command=self.Go_Home)

        self.launch_button = tk.Button(self,text="Launch",command=lambda: self.launch(self.selected))
        self.delete_button = tk.Button(self,text="Delete",command=lambda: self.delete(self.selected))
        self.change_button = tk.Button(self,text="Change",command=lambda: self.change(self.selected))
        self.change_name = tk.Entry(self)
        self.change_name_label = tk.Label(self,text="New Name")
        self.change_path = tk.Entry(self, text="New Path")
        self.change_path_label = tk.Label(self,text="New Path")

        self.filler.grid(row=1,column=0)

        self.export_button.grid(row=3,column=1,sticky="")
        #self.import_button.grid(row=5,column=1)
        self.delete_button.grid(row=12,column=2,sticky="w")
        self.launch_button.grid(row=7,column=2,sticky="w")
        self.change_button.grid(row=8,column=2,rowspan=2,sticky="w")
        self.button1.grid(row=4,column=2)
        self.export_name.grid(row=1,column=1,columnspan=2,sticky="e")
        self.export_path.grid(row=2,column=1,columnspan=2,sticky="e")
        self.change_name.grid(row=8,column=4,sticky="s")
        self.change_path.grid(row=9,column=4,sticky="n")
        #self.import_name.grid(row=4,column=1)
        #self.delete_name.grid(row=5,column=1)
        self.export_name_label.grid(row=1,column=1,sticky="w")
        self.export_path_label.grid(row=2,column=1,sticky="w")
        self.change_name_label.grid(row=8,column=3,sticky="s")
        self.change_path_label.grid(row=9,column=3,sticky="n")
        self.AppList.grid(row=7,rowspan=6,column=1,sticky="n")

    def updater(self):
        """Update AppList (after every change of the list)"""
        self.AppList.delete(0,self.AppList.size()-1)
        self.list = self.imp.importall()
        for i in self.list:
            self.AppList.insert(tk.END,i)
    def app_export(self):
        """Export based on 2 entries"""
        self.imp.export(self.export_name.get(),self.export_path.get())
        self.updater()
    def delete(self,app):
        """App Removal Based on app"""
        if messagebox.askyesno("Warning","Delete The App?"):
            self.imp.delete(app)
            self.updater()
    def Go_Home(self):
        """Go to the "Home" Frame"""
        self.window.change_frame(frame1.Frame1)
    def naming(self,event):
        """updates the current selected option in AppList"""
        try:
            self.selected = self.AppList.get(self.AppList.curselection()[0])
        except:
            return "None"
    def launch(self,app):
        """Launch an app by importing it and launching via os"""
        os.system(self.imp.importt(app))
    def change(self,app):
        """Change Based on app, and 2 entries. IF YOU CHOOSE NOTHING, IT WILL REMOVE EVERYTHING. Discovered at 2:18"""
        if messagebox.askyesno("Warning","Change The App?"):
            self.imp.change(app,self.change_name.get(),self.change_path.get())
            self.updater()
    
    