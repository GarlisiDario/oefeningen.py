from tkinter import *
import tkinter as tk
import mysql.connector
from PIL import ImageTk
from tkinter import messagebox


class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

        menu = Menu(self.master)
        self.master.config(menu=menu)

        fileMenu = Menu(menu)
        fileMenu.add_command(label="Add employee",command=self.add_employee)
        fileMenu.add_command(label="Delete employee")
        fileMenu.add_command(label= "Reform employee")
        fileMenu.add_command(label="Exit", command=self.exitProgram)
        menu.add_cascade(label="employee", menu=fileMenu)

        editMenu = Menu(menu)
        editMenu.add_command(label="Undo")
        editMenu.add_command(label="Redo")
        menu.add_cascade(label="Edit", menu=editMenu)

    def exitProgram(self):
        exit()
    def add_employee(self):
        pass



root = Tk()
app = Window(root)
root.wm_title("Tkinter window")
root.mainloop()