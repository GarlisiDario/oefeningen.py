import tkinter as tk
from tkinter import messagebox

def klik():
    print("klik!")
    messagebox.showinfo("hallo","in orde")


root = tk.Tk()


l_voornaam = tk.Label(root,text="voornaam").grid(row=0,column=0)
l_achternaam = tk.Label(root,text="achternaam").grid(row=1,column=0)
l_pin = tk.Label(root,text="pin").grid(row=2,column=0)
i_pin = tk.Entry(root).grid(row=2,column=1)
i_voornaam = tk.Entry(root).grid(row=0,column=1)
i_achternaam = tk.Entry(root).grid(row=1,column=1)
btn_naam = tk.Button(root,text="lets go!",command=klik).grid(row=3,column=0)





root.mainloop()

