import tkinter as tk

#Version Variable
version = "V.0.1"

def codeeditor():
    #Window Creation
    root = tk.Tk()

    #WindowData
    root.title("Glass Engine | Code Editor " + version)
    root.iconbitmap()
    root.geometry("900x700")
    root.minsize(900, 700)


    #Window Mainloop()
    root.mainloop()