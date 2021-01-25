from glassengine import codeide as ci
import tkinter as tk

#Version Variable
version = "V.0.1"

#Window Creation
root = tk.Tk()

#WindowData
root.title("Glass Engine " + version)
root.iconbitmap()
root.geometry("900x700")
root.minsize(900, 700)

#Access to code editor
cdB = tk.Button(text="Code Editor", command=ci.codeeditor())


#Window Mainloop()
root.mainloop()